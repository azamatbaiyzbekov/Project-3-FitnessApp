from django import forms
from .models import Workout


class WorkoutForm(forms.ModelForm):

    class Meta: 
        model = Workout 
        fields = ('workout_name', 'exercise_name_1', 'sets_exercise_1', 'reps_exercise_1',
         'exercise_name_2', 'sets_exercise_2', 'reps_exercise_2',
         'exercise_name_3', 'sets_exercise_3', 'reps_exercise_3',
         'exercise_name_4', 'sets_exercise_4', 'reps_exercise_4',
        )