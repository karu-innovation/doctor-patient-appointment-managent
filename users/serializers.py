from rest_framework import serializers

from .models import Account

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'specialization', 'is_active', 'is_admin', 'is_doctor', 'is_patient')

        def create(self, validated_data):
            user = Account(
                username=validated_data['username'],
                password=validated_data['password'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                specialization=validated_data['specialization'],
                is_active=validated_data['is_active'],
                is_admin=validated_data['is_admin'],
                is_doctor=validated_data['is_doctor'],
                is_patient=validated_data['is_patient']
            )
            user.save()
