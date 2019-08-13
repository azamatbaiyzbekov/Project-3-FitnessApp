from django import forms
from .models import Workout, Exercise


class WorkoutForm(forms.ModelForm):

    class Meta: 
        model = Workout 
        fields = ('workout_name',)


class ExerciseForm(forms.ModelForm):
    
    class Meta: 
        model = Exercise
        fields = ('exercise_name_1', 'sets_1', 'reps_1', 'exercise_name_2', 'sets_2', 'reps_2', 'exercise_name_3', 'sets_3', 'reps_3')


