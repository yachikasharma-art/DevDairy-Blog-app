from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('',views.PostList.as_view(),name= 'post_list'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name= 'post_details'),
    path('category/<str:category>/', views.category_view, name='category_view'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('add/', login_required(views.AddPostView.as_view()), name='add_post'),
]