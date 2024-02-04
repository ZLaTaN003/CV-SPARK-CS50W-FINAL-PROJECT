from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path('', views.profile, name='profile'),
    path('jobfromlink',views.jobfromlink,name='jobfromlink'),
    path('cv/<int:id>/', views.cv, name='cv'),
    path('cvtopdf/<int:id>/', views.cvtopdf, name='cvtopdf'),
    path('list',views.list,name='list'),
    path('like-cv/<int:cv_id>/', views.like_cv, name='like-cv'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('sections/', views.section_list, name='section_list'),
    path('sections/<int:section_id>/join/', views.join_section, name='join_section'),
    path('sections/<int:section_id>/leave/', views.leave_section, name='leave_section'),
    path('section_users/<int:section_id>/', views.section_users, name='section_users')
    



]