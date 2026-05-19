from django.urls import path
from . import views
urlpatterns=[
    path('',views.post_list,name= 'post_list'),
    path('post/<int:pk>/', views.post_details, name= 'post_details'),
    path('category/<str:category>/', views.category_view, name='category_view'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('add/', views.add_post, name='add_post'),
]