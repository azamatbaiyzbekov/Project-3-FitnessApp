from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm
from django.contrib.auth.decorators import login_required
import operator
from django.db.models import Q


# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

@login_required
def workout_list(request):
    query = ""
    if request.GET:
        query = request.GET['q']
    workouts = search(query)

    return render(request, 'workout_list.html', {"workouts": workouts, "query": query})
 
@login_required
def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    return render(request, 'workout_detail.html', {"workout": workout})


@login_required
def workout_detail(request, pk):
    workout = Workout.objects.get(id=pk)
    return render(request, 'workout_detail.html', {"workout": workout})

# NOTE Create workout controller
@login_required
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        e_form = ExerciseForm(request.POST)
        if form.is_valid() and e_form.is_valid():
            workout = form.save(commit=False)
            e_workout = e_form.save(commit=False)
            workout.user = request.user
            workout.save()
            e_workout.user = request.user
            e_workout.workout = workout
            e_workout.save()
            return redirect('workout_list')
    else: 
        form = WorkoutForm()
        e_form = ExerciseForm()
    return render(request, 'workout_form.html', {'form': form, 'e_form':e_form ,'header': 'New Workout'})

# NOTE Edit Workout Controller
@login_required
def workout_edit(request, pk):
    workout = Workout.objects.get(id=pk)
    exercise = Exercise.objects.get(id=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        e_form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid() and e_form.is_valid():
            workout = form.save()
            exercise = e_form.save()

            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
        e_form = ExerciseForm(instance=exercise)
    return render(request, 'workout_form.html', {'form': form, 'e_form':e_form, 'header':f'Edit {workout.workout_name}'})

# NOTE Delete Workout Controller
@login_required
def workout_delete(request, pk):
    Workout.objects.get(id=pk).delete()
    return redirect('profile')
  
# NOTE User Profile Controller
@login_required
def profile(request):
    user = request.user
    workouts = Workout.objects.filter(user=user)
    return render(request, 'profile.html', {'workouts': workouts})

# NOTE Likes
@login_required 
def like_workout(request):
    workout_id = request.GET.get('workout_id', None)

    likes = 0
    if (workout_id):
        workout = Workout.objects.get(id=int(workout_id))
        if workout is not None:
            likes = workout.likes + 1
            workout.likes = likes
            workout.save()
    return HttpResponse(likes)

def search(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Workout.objects.filter(
            Q(workout_name__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))
