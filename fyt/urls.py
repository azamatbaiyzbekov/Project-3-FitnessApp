from django.urls import path
from . import views

# SECTION URL Patterns and routes

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('workouts/<int:pk>', views.workout_detail, name='workout_detail'),
    path('workouts/<int:pk>/edit', views.workout_edit, name='workout_edit'),
    path('workouts/<int:pk>/delete', views.workout_delete, name='workout_delete'),
    path('workouts/new', views.workout_create, name='workout_create'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
]

