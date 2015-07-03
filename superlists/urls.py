from django.conf.urls import include, url
from lists import views as list_views

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/new$', list_views.new_list, name='new_list'),
    url(r'^lists/(\d+)/$', list_views.view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$', list_views.add_item, name='add_item'),
]
