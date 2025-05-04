from django.urls import path
from . import views
urlpatterns = [
    path('', views.page,name='page'),
    path('login',views.login,name='login'),
    path('addtask',views.addtask,name='addtask'),
    path('tasklist',views.tasklist,name='tasklist'),
    path('delete_task/<int:task_id>',views.delete_task,name='delete_task'),
    path('complete_task/<int:task_id>',views.complete_task,name='complete_task'),
    path('register', views.register,name='register')
]
