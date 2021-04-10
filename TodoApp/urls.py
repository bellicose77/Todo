from django.urls import path
from TodoApp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('updatetask/<int:pk>/',views.update_taks,name='updatetask'),
    path('delete/<int:pk>/',views.delete_item,name='delete_task'),
]