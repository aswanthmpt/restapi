from django.urls import path
from. import views

urlpatterns = [
    path('',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('details/<str:pk>',views.details,name='details'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
]
