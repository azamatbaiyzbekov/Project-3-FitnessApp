from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Workout(models.Model):
    workout_name = models.CharField(max_length=50)
    exercise_name_1 = models.CharField(max_length=50)
    sets_exercise_1 = models.PositiveIntegerField(default="0")
    reps_exercise_1 = models.PositiveIntegerField(default="0")
    exercise_name_2 = models.CharField(max_length=50)
    sets_exercise_2 = models.PositiveIntegerField(default="0")
    reps_exercise_2 = models.PositiveIntegerField(default="0")
    exercise_name_3 = models.CharField(max_length=50)
    sets_exercise_3 = models.PositiveIntegerField(default="0")
    reps_exercise_3 = models.PositiveIntegerField(default="0")
    exercise_name_4 = models.CharField(max_length=50)
    sets_exercise_4 = models.PositiveIntegerField(default="0")
    reps_exercise_4 = models.PositiveIntegerField(default="0")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    
    def __str__(self):
        return f"{self.workout_name}--{self.exercise_name}"

