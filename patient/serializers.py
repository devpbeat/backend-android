from .models import Patient
from django.contrib.auth.models import User
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Patient
        fields = ("__all__")

    
    def create(self, validated_data):

        user_ = User.objects.filter(username=validated_data['email']).exists()
        # Create patient user
        if not user_:
            user = User.objects.create_user(
                username=validated_data['email'],
                password=validated_data['password'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False
            user.save()
            validated_data.pop('password')
            validated_data['user'] = user
            patient = Patient.objects.create(**validated_data)
            return patient
        else:
            raise serializers.ValidationError({"email": "Email already exists"})
    
    def update(self, instance, validated_data):
        # Update patient user
        user_ = User.objects.filter(username=validated_data['email']).exists()
        if not user_:
            patient = super().update(instance, validated_data)
            return patient
        else:
            raise serializers.ValidationError({"email": "Email already exists"})
    

