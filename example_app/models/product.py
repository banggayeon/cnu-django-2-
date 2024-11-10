from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'department'
        verbose_name = '학과'

class Student(Person):
    student_id = models.CharField(max_length=10, verbose_name="학번")
    maximum_credit = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    class Meta:
        db_table = 'student'
        verbose_name = '학생'

class Professor(Person):
    employee_id = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    class Meta:
        db_table = 'professor'
        verbose_name = '교직원'

class Course(models.Model):
    course_name = models.CharField(max_length=50, verbose_name="강의 이름")
    course_id = models.CharField(max_length=10)
    maximum_student = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'course'
        verbose_name = '강의-retest'

__all__ = ['Student', 'Professor', 'Department', 'Course']