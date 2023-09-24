from django.db import models


class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    RoleID = models.ForeignKey('UserRole', on_delete=models.CASCADE)


class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Credits = models.IntegerField()
    CategoryID = models.ForeignKey('CourseCategory', on_delete=models.CASCADE)


class DegreePlan(models.Model):
    DegreePlanID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    DepartmentID = models.ForeignKey('Department', on_delete=models.CASCADE)
    ElectiveGroupID = models.ForeignKey(
        'ElectiveGroup', on_delete=models.CASCADE)


class StudentCourse(models.Model):
    StudentID = models.ForeignKey('Student', on_delete=models.CASCADE)
    CourseID = models.ForeignKey('Course', on_delete=models.CASCADE)
    Status = models.CharField(max_length=20, choices=[(
        'Completed', 'Completed'), ('InProgress', 'In Progress'), ('NotStarted', 'Not Started')])
    SemesterID = models.ForeignKey('Semester', on_delete=models.CASCADE)
    IsCompleted = models.BooleanField()


class College(models.Model):
    CollegeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)


class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    CollegeID = models.ForeignKey('College', on_delete=models.CASCADE)


class Semester(models.Model):
    SemesterID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Year = models.IntegerField()


class Prerequisite(models.Model):
    CourseID = models.ForeignKey(
        'Course', related_name='course_prerequisites', on_delete=models.CASCADE)
    PrerequisiteCourseID = models.ForeignKey(
        'Course', related_name='prerequisite_courses', on_delete=models.CASCADE)


class ElectiveGroup(models.Model):
    ElectiveGroupID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)


class UserRole(models.Model):
    RoleID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)


class CourseCategory(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)


class DepartmentRequirement(models.Model):
    DepartmentID = models.ForeignKey('Department', on_delete=models.CASCADE)
    Requirement = models.CharField(max_length=100)


class StudentDegreePlan(models.Model):
    StudentID = models.ForeignKey('Student', on_delete=models.CASCADE)
    DegreePlanID = models.ForeignKey('DegreePlan', on_delete=models.CASCADE)
    Type = models.CharField(max_length=20, choices=[
                            ('Major', 'Major'), ('Minor', 'Minor')])
