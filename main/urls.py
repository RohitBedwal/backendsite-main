
from django.urls import path
from . import views

urlpatterns = [
    path('contact-crud/', views.contact_crud_view, name='contact_crud'),
    path('edit-contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact/', views.contact_view, name='contact'),
    path('response-taken/', views.response_taken_view, name='response_taken'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('contact-crud/', views.contact_crud_view, name='contact_crud'),
    path('edit-contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact/', views.contact_view, name='contact'),
    path('response-taken/', views.response_taken_view, name='response_taken'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]
