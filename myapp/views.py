from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_user(request):
    if request.method == "POST":
        user_data = json.loads(request.body)
        user_name = user_data.get('user_name')
        age = user_data.get('age')
        sex = user_data.get('sex')

        if not user_name or not age or not sex:
            return JsonResponse({'error': 'All fields are required.'}, status=400)
        user = User.objects.create(user_name=user_name,age=age,sex=sex)
        return JsonResponse({'massage':'User registered seccessfully.'},status=201)
    return JsonResponse({'error':'Invalid request method.'},status=405)

def user_list(request):
    users = User.objects.all()
    user_data=[]
    for user in users:
        user_data.append({'user_name':user.user_name,
                          'age':user.age,
                          'sex':user.sex,
                          })
    return JsonResponse({'user_data':user_data})

@csrf_exempt
def delete_user(request,user_id):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found.'}, status=404)
    
    if request.method == "DELETE":
        user.delete()
        return JsonResponse({'message': 'User deleted successfully.'}, status=200)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def data_update(request,user_id):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error':'User not found'})
    
    if request.method == "PUT":
        user_data = json.loads(request.body)
        user_name = user_data.get('user_name')
        age = user_data.get('age')
        sex = user_data.get('sex')

        if user_name:
            user.user_name = user_name
        if age:
            user.age = age
        if sex:
            user.sex = sex

        user.save()
        return JsonResponse({'massage':'User updated successfully.'},status=200)
    return JsonResponse({'error':'Invalid request method.'},status=405)
    