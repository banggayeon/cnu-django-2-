from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from example_app.models.product import Professor, Department
from django.http import Http404
from example_app.serializers.department import DepartmentSerializer

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        #특정 필드를 읽기 전용으로 설정할 때 사용됨
        read_only_fields = ['id']
        
