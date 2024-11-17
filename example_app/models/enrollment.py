from django.db import models
from django.conf import settings
from .product import Student, Course

class Enrollment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date=models.DateField(auto_now_add=True)
    student=models.ForeignKey(Student, on_delete=models.PROTECT)
    course=models.ForeignKey(Course, on_delete=models.PROTECT)

    class Meta:
        db_table = 'enrollment'
        verbose_name = '등록'
        #중복 등록 방지
        unique_together = ('student', 'course')

    # 호출 시 보기 편하도록 하기
    def __str__(self):
        return f"{self.student.name}-{self.course.course_name}"