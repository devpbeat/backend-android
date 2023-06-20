from .models import Patient
from django.contrib.auth.models import User
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Patient
        fields = ("__all__")

    
    def create(self, validated_data):
        # Create patient user
        user = User.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        validated_data.pop('password')
        validated_data['user'] = user
        patient = Patient.objects.create(**validated_data)
        return patient
    
    def update(self, instance, validated_data):
        patient = super().update(instance, validated_data)
        return patient
    
    

