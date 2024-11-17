from rest_framework import serializers
from example_app.models.enrollment import Enrollment
from example_app.models.product import Student, Course
from example_app.serializers.student import StudentSerializer
from example_app.serializers.course import CourseSerializer


class EnrollmentSerializer(serializers.ModelSerializer):
    student=StudentSerializer(read_only=True)
    course=CourseSerializer(read_only=True)
    student_id=serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), write_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['id']