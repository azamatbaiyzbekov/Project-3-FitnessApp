from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Workout(models.Model):
    workout_name = models.CharField('Workout ', max_length=50)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    
    def __str__(self):
        return f"{self.workout_name}"


class Exercise(models.Model):
    exercise_name_1 = models.CharField('Exercise ', max_length=50)
    sets_1 = models.PositiveIntegerField('Sets ', default="0")
    reps_1 = models.PositiveIntegerField('Reps',default="0")

    exercise_name_2 = models.CharField('Exercise ',max_length=50)
    sets_2 = models.PositiveIntegerField('Sets ',default="0")
    reps_2 = models.PositiveIntegerField('Reps ',default="0")

    exercise_name_3 = models.CharField('Exercise ',max_length=50)
    sets_3 = models.PositiveIntegerField('Sets ',default="0")
    reps_3 = models.PositiveIntegerField('Reps ',default="0")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    
    def __str__(self):
        return f"{self.exercise_name}"