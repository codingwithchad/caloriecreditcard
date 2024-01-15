from django.shortcuts import render
from .services import get_workout_rows, get_member_rows

def workouts(request):
  workout_data = get_workout_rows("Workouts sheet")  
  workouts = {}
  current_category = ''
  for workout in workout_data:
    if workout['category']:
      current_category = workout['category']
      workouts[current_category] = []
    workouts[current_category].append(workout)  
  return render(request, 'workouts.html', {'workouts': workouts})

def debt(request):
  debt = get_member_rows("Workouts sheet")  
  print(debt)
  return render(request, 'debt.html', { 'debt' : debt})