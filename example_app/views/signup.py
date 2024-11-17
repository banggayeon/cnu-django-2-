from rest_framework import status
from rest_framework.views import APIView
from example_app.models.product import Student, Professor
from rest_framework.response import Response

from rest_framework.permissions import AllowAny
from django.db import transaction
from example_app.serializers.user import UserSerializer

from example_app.models.roles import Role, UserRole

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class StudentSignupView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'student_id': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['student_id'],
        ),
        responses={
            201: "Post successful", 
            400: "Bad request",
            404: "Student with provied ID does not exist"
        }
    ) #201이 상태 관련임
    def post(self, request):
        student_id = request.data.get("student_id")
        try:
            with transaction.atomic():
                student = Student.objects.get(student_id=student_id)

                if student.user:
                    return Response({"error": "This student is already linked to a user"},
                                    status = status.HTTP_404_BAD_REQUEST)

                serializer = UserSerializer(data=request.data)

                if serializer.is_valid():
                    user = serializer.save()
                    student.user=user
                    student.save()

                    return Response({"message": "Student signup successful"}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        except Student.DoesNotExist:
            return Response({"error": "Student with provided ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
        

class ProfessorSignupView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'employee_id': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['employee_id'],
        ),
        responses={
            201: "Post successful", 
            400: "Bad request",
            404: "Professor with provied ID does not exist",
        }
    )

    def post(self, request):
        employee_id = request.data.get("employee_id")
        try:
            with transaction.atomic():
                professor = Professor.objects.get(employee_id=employee_id)
                if professor.user:
                    return Response({"error": "This professor is already linked to a user"},
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    user = serializer.save()
                    professor.user = user
                    professor.save()
                    
                    professor_role = Role.objects.get(name="Professor")
                    UserRole.objects.create(user=user, role=professor_role)

                    return Response({"message": "Professor signup successful"}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Professor.DoesNotExist:
            return Response({"error": "Professor with provided ID does not exist"}, status=status.HTTP_404_NOT_FOUND)

