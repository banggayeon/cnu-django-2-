from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from example_app.models.product import Department
from django.http import Http404

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['id']

        
