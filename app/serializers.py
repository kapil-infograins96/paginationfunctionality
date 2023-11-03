from rest_framework import serializers
from app.models import Student
from rest_framework import status
from rest_framework.response import Response


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

    