from django.shortcuts import render
from .services import get_all_rows

def workouts(request):
  workout_data = get_all_rows("Workouts sheet")  
  workouts = {}
  current_category = ''
  for workout in workout_data:
    if workout['category']:
      current_category = workout['category']
      workouts[current_category] = []
    workouts[current_category].append(workout)  
  return render(request, 'workouts.html', {'workouts': workouts})

  