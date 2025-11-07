from django.urls import path
from App1 import views

urlpatterns=[
    path('home',views.HomeView.as_view(),name="home"),
    path('create_todo',views.CreateTodo.as_view(),name='create_todo'),
    path('detail<int:id>',views.DetailView.as_view(),name='detail'),
    path('update<int:id>',views.UpdateView.as_view(),name='todo_update'),
    path('delete<int:id>',views.DeleteView.as_view(),name='todo_delete'),


    path('assign',views.AssignCreateView.as_view(),name='assign'),


    path('',views.LoginView.as_view(),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('register',views.RegisterView.as_view(),name='register')


]