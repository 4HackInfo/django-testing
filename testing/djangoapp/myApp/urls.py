from django.urls import path
from . import views

urlpatterns = [

path('', views.login_view),
path('login/', views.login_view),
path('register/', views.register_view),
path('dashboard/', views.dashboard_view),
path('feedback/', views.feedback_view),
path('adminpanel/', views.admin_panel),
path('profile/<int:id>/', views.profile),
path('logout/', views.logout_view),

]