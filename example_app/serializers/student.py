from rest_framework import serializers
from example_app.models.product import Student, Department
from example_app.serializers.department import DepartmentSerializer

class StudentSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']
        
