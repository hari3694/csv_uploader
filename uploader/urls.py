from django.conf.urls import url
from uploader import views

urlpatterns = [
    url(r'^uploader', views.UploaderView.as_view(), name='dashboard_new'),
        ]
