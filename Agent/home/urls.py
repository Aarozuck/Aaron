from django.urls import path
from . import views

urlpatterns = [
    path('teacher_signup/', views.teacher_signup, name='teacher_signup'),
    path('customer_signup/', views.customer_signup, name='customer_signup'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('customer_login/', views.customer_login, name='customer_login'),
    path('home/', views.home, name='home'),
    path('', views.intro, name='intro'),
    path('about/', views.about, name='about'),
    path('teacher_profile/<int:teacher_id>', views.teacher_profile, name='teacher_profile'),
    path('customer_profile/<int:customer_id>', views.customer_profile, name='customer_profile'),
    path('rate_teacher/<int:teacher_id>', views.rate_teacher, name='rate_teacher'),
    path('comment_teacher/<int:teacher_id>', views.comment_teacher, name='comment_teacher'),
]