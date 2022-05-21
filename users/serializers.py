from rest_framework import serializers
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username','email','first_name','last_name','phone_no','password','password2']

        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        user = Account(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            phone_no = self.validated_data['phone_no']
        )
        password = self.validated_data['password']
        password2 = self.validates_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        user.set_password(password)
        user.save()
        return user
