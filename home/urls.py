from django.urls import path
from .views import home,details,deletes,create,updates

urlpatterns = [
    path('',home,name='home'),
    path('details/<int:todo_id>/',details,name='details'),
    path('detelets/<int:todo_id>',deletes,name='deletes'),
    path('create/',create,name='create'),
    path('updates/<int:todo_id>',updates,name='updates'),

]
