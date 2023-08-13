from django.urls import path
from myapp import views

urlpatterns = [
    path('add_user/',views.add_user,name='add_user'),
    path('user_list/',views.user_list,name='user_list'),
    path('delete_user',views.delete_user,name='delete_user'),
    path('data_update',views.data_update,name='data_update'),
]