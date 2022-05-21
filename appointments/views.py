from django.shortcuts import render
from rest_framework.decorators import api_view
from .serialization import AppointmentSerializer
from .models import Appointment
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def appointment_view(request):
    if request.method == 'GET':
        serializer = AppointmentSerializer(Appointment, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentSerializer(data = request.data)
        if serializer.is_valid():

          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, uuid):
    try:
      appointment = Appointment.objects.get(uuid=uuid)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      serializer = AppointmentSerializer(appointment)
      return Response(serializer.data)

    elif request.method == 'PUT':
      serializer = AppointmentSerializer(appointment, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      appointment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
