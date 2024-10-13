from django.urls import path

from . import views
app_name = 'dashboard'
urlpatterns = [
    path("home/", views.dashboard_view, name='dashboard-home'),
    path("login/", views.login_view, name='login')
]
