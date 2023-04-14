from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Door
# Create your views here.
@csrf_exempt
def date(request):
    with connection.cursor() as c:
        c.execute("select date from echarts_door")
        date = c.fetchall()
    return JsonResponse(date, safe=False)
@csrf_exempt
def door(request):
    with connection.cursor() as c:
        c.execute("select door from echarts_door")
        door = c.fetchall()
    return JsonResponse(door, safe=False)
def get_door(request):
    all_info = Door.objects.all()
    date_list = []
    door_list = []
    for info in all_info:
        date_list.append(info.date)
        door_list.append(info.door)
    return render(request,
                    {'date_list': date_list, 'door_list': door_list})
