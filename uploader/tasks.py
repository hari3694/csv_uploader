from .models import ProductDetails
from csv_uploader import celery_app
from datetime import datetime
import csv


@celery_app.task
def process(fileurl):
    '''
    function to update the productdetails model from the csv
    :param fileurl:
    :return: None
    '''
    with open(fileurl, 'r') as up_file:
        try:
            csv_reader = csv.DictReader(up_file)
            line = 0
            for row in csv_reader:
                if line == 0:
                    line += 1
                in_key = row['inventory_key']
                on_sale = False
                sale_enddate = row['sale_end_datetime']
                if sale_enddate is not '':
                    sale_enddate = datetime.strptime(sale_enddate, '%b %d %Y %I:%M%p')
                    if datetime.now() < sale_enddate:
                        on_sale = True
                        catalog_price = row['case_sale_price']
                else:
                    catalog_price = row['case_price']
                ProductDetails.objects.create(inventory_key=row['inventory_key'], catalog_no=row['catalog_no'],
                                              catalog_color=row['catalog_color'], size=row['size'],
                                              quantity=row['quantity'], is_on_sale=on_sale, catalog_price=catalog_price)
                line += 1
        except Exception as e:
            print(e)
    print("Process Completed!")
    return True