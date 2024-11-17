from rest_framework import serializers
from example_app.models.product import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['id']

        
