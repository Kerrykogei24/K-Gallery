from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.pics,name='pics'),
        url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^location/(\d+)',views.viewPics_by_location,name='locationpic'),
    url(r'^category/(\d+)',views.viewPics_by_category, name = 'categorypic')
    ]