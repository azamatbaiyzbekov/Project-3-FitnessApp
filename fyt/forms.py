from django import forms
from .models import Workout, Exercise


class WorkoutForm(forms.ModelForm):

    class Meta: 
        model = Workout 
        fields = ('workout_name',)


class ExerciseForm(forms.ModelForm):
    
    class Meta: 
        model = Exercise
        fields = ('exercise_name', 'sets', 'reps')


