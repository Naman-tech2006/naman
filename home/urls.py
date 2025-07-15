from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('contact-entries/', views.contact_entries_view, name='contact_entries'),
    path('contact/update/<int:pk>/', views.update_contact, name='update_contact'),
    path('contact/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
