from django.urls import path
from contact import views
app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),# type:ignore
    path('search/', views.search, name='search'),# type:ignore
    #contact crud
    path('contact/<int:contact_id>/detail', views.contact, name='contact'),# type:ignore
    path('contact/create/', views.create, name='create'),# type:ignore


]
