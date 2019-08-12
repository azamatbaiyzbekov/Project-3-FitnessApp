from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Workout(models.Model):
    workout_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    
    def __str__(self):
        return f"{self.id}"


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=50)
    sets = models.PositiveIntegerField(default="0")
    reps = models.PositiveIntegerField(default="0")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return f"{self.exercise_name}"


