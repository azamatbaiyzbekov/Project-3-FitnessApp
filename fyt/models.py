from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Workout(models.Model):
    workout_name = models.CharField(max_length=50)
    exercise_name = models.CharField(max_length=50)
    sets = models.PositiveIntegerField(default="0")
    reps = models.PositiveIntegerField(default="0")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    
    def __str__(self):
        return f"{self.workout_name}--{self.exercise_name}"

