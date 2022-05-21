
from rest_framework import serializers


from .models import Specialisation


class specialisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialisation
        fields = ('name',)

        def create(self, validated_data):
            specialisation = Specialisation(
                name=validated_data['name']
            )
            specialisation.save()

        