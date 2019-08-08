from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Workout
from .forms import WorkoutForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return HttpResponse('This is home')

def json_res(request):
    return render({"status": "Ok"})

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workout_list.html', {"workouts": workouts})


def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    return render(request, 'workout_detail.html', {"workout": workout})

# SECTION Create exercise controller
