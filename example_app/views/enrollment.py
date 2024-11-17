from example_app.models.enrollment import Enrollment
from example_app.serializers.enrollment import EnrollmentSerializer
from example_app.models.product import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

class EnrollmentListAPIView(APIView):
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        queryset = Enrollment.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = EnrollmentSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        student_id = request.data.get('student_id')

        if not course_id or not Course.object.filter(id=course_id):
            return Response({"error":"유효하지 않은 course_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        if Enrollment.objects.filter(course_id=course_id, student_id=student_id).exists():
            return Response({"error":"이미 수강신청함"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = EnrollmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EnrollmentDetailAPIView(APIView):

    def get_queryset(self):
        queryset = Enrollment.objects.all()
        return queryset
    
    def get_object(self,pk, student_id, course_id):
        try:
            obj = self.get_queryset().get(pk=pk, student_id=student_id, course_ide=course_id)
            return obj
        except Enrollment.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')

        obj = self.get_object(pk, student_id, course_id)
        serializer = EnrollmentSerializer(obj)

        return Response(serializer.data)

    def delete(self, request, pk):
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')
        
        obj = self.get_object(pk, student_id, course_id)
        obj.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)