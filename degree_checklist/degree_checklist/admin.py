from django.contrib import admin
from .models import College, Department, Course, SectionGroup, Section, CourseOptionGroup, Program, Student, StudentRole, Semester, ExternalCollege, TransferEquivalency, StudentCourse, Prerequisite, StudentDegreePlan

# Register your models here.

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(SectionGroup)
admin.site.register(Section)
admin.site.register(CourseOptionGroup)
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(StudentRole)
admin.site.register(Semester)
admin.site.register(ExternalCollege)
admin.site.register(TransferEquivalency)
admin.site.register(StudentCourse)
admin.site.register(Prerequisite)
admin.site.register(StudentDegreePlan)
