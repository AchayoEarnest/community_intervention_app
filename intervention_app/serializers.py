from rest_framework import serializers
from .models import Enrollment

# Serializer for enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        # model to serialize
        model = Enrollment

        # Include all fields
        fields = '__all__'
