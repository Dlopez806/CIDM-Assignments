from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} ({self.course_id})'

class SectionGroup(models.Model):
    name = models.CharField(max_length=100)
    required_credits = models.IntegerField()
    
    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    required_credits = models.IntegerField()
    section_group = models.ForeignKey(SectionGroup, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class CourseOptionGroup(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    required_credits = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    section_groups = models.ManyToManyField(SectionGroup, blank=True)
    elective_courses = models.ManyToManyField(Course, related_name='elective_programs', blank=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey('StudentRole', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.student_id})'

class StudentRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} ({self.role_id})'

class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} ({self.year})'

class ExternalCollege(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TransferEquivalency(models.Model):
    external_course_name = models.CharField(max_length=100)
    external_course_id = models.CharField(max_length=100)
    equivalent_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    external_college = models.ForeignKey(ExternalCollege, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.external_course_name} at {self.external_college.name} transfers as {self.equivalent_course.name}'

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('InProgress', 'In Progress'), ('NotStarted', 'Not Started')])
    transfer_equivalency = models.ForeignKey(TransferEquivalency, null=True, blank=True, on_delete=models.SET_NULL)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    is_completed = models.BooleanField()
    
    def __str__(self):
        return f'Student {self.student.student_id} - Course {self.course.course_id} - Status {self.status}'

class Prerequisite(models.Model):
    course = models.ForeignKey(Course, related_name='course_prerequisites', on_delete=models.CASCADE)
    prerequisite_course = models.ForeignKey(Course, related_name='prerequisite_courses', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Course {self.course.course_id} - Prerequisite {self.prerequisite_course.course_id}'

class StudentDegreePlan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=[('Major', 'Major'), ('Minor', 'Minor')])
    
    def __str__(self):
        return f'Student {self.student.student_id} - Program {self.program.program_id} - Type {self.type}'
