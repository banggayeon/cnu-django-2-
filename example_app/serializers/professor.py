from rest_framework import serializers
from example_app.models.product import Professor, Department
from example_app.serializers.department import DepartmentSerializer

class ProfessorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),write_only=True)    
    
    class Meta:
        model = Professor
        fields = '__all__'
        #특정 필드를 읽기 전용으로 설정할 때 사용됨
        read_only_fields = ['id']
        
