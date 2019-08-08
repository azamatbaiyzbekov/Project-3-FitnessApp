from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Workout
from .forms import WorkoutForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return HttpResponse('This is home')

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workout_list.html', {"workouts": workouts})

def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    return render(request, 'workout_detail.html', {"workout": workout})

# NOTE Create workout controller

def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_detail', pk=workout.pk)
    else: 
        form = WorkoutForm()
    return render(request, 'workout_form.html', {'form': form, 'header': 'New Workout'})

# NOTE Edit Workout Controller

def workout_edit(request, pk):
    workout = Workout.objects.get(id=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workout_form.html', {'form': form, 'header':f'Edit {workout.workout_name}'})

# NOTE Delete Workout Controller

def workout_delete(request, pk):
    Workout.objects.get(id=pk).delete()
    return redirect('workout_list')
  
# NOTE User Profile Controller

def profile(request):
    user = request.user
    workouts = Workout.objects.filter(user=user)
    return render(request, 'profile.html', {'workouts': workouts})
