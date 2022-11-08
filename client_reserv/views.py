from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from client_reserv.models import Reservation, TimeSlot
from client_reserv.serializers import ReservationSerializer, TimeSlotSerializer
from django.http.response import JsonResponse


def base(request):
  """
  The base template, that will be used for every common pages
  """
  return render(request, 'base.html')


def home(request):
  """
  Home page view
  """
  return render(request, 'home.html')


@csrf_exempt
def reservationApi(request, id=0):
  """
  Return all reservations on table Reservation and add new reservation
  """
  if request.method == 'GET':
    reservations = Reservation.objects.all()
    reservations_serializer = ReservationSerializer(reservations, many=True)
    return JsonResponse(reservations_serializer.data, safe=False)
  elif request.method == 'POST':
    reservation_data = JSONParser().parse(request)
    reservation_serializer = ReservationSerializer(data=reservation_data)
    if reservation_serializer.is_valid():
      reservation_serializer.save()
      return JsonResponse("New reservation successfully added!", safe=False)
    return JsonResponse("Failed to add reservation", safe=False)

@csrf_exempt
def timeslotApi(request, id=0):
  if request.method == 'GET':
    timeslots = TimeSlot.objects.all()
    timeslots_serializer = TimeSlotSerializer(timeslots, many=True)
    return JsonResponse(timeslots_serializer.data, safe=False)
  elif request.method == 'POST':
    timeslot_data = JSONParser().parse(request)
    timeslot_serializer = TimeSlotSerializer(data=timeslot_data)
    if timeslot_serializer.is_valid():
      timeslot_serializer.save()
      return JsonResponse("New Time Slot successfully added!", safe=False)
    return JsonResponse("Failed to add timeslot", safe=False)
