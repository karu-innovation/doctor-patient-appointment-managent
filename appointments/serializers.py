
from rest_framework import serializers

from appointments.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('doctor', 'patient', 'time_slot')
    
    def create(self, validated_data):
        apointments = Appointment(
            doctor=validated_data['doctor'],
            patient=validated_data['patient'],
            time_slot=validated_data['time_slot']
        )
        apointments.save()