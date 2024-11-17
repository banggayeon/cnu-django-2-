from rest_framework import serializers
from example_app.models.product import Course, Department, Professor
from example_app.serializers.department import DepartmentSerializer
from example_app.serializers.professor import ProfessorSerializer

class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all(), write_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id']
    
    def create(self, validated_data):
        department_id = validated_data.pop('department_id')
        professor_id = validated_data.pop('professor_id')

        department = Department.objects.get(id=department_id.id)
        professor = Professor.objects.get(id=professor_id.id)
        
        course = Course.objects.create(department=department, professor=professor, **validated_data)
        return course
    
    def validate_course_name(self, value):
        if "badword" in value:
            raise serializers.ValidationError("Invalid course name.")
        return value
    
    def validate(self, data):
        if data['department'].id == data['professor'].id:
            raise serializers.ValidationError("Department and professor cannot be the same.")
        return data
