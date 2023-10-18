from django import forms
from .models import (
    College,
    Department,
    Course,
    SectionGroup,
    Section,
    CourseOptionGroup,
    Program,
    Student,
    StudentRole,
    Semester,
    ExternalCollege,
    TransferEquivalency,
    StudentCourse,
    Prerequisite,
    StudentDegreePlan
)

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class SectionGroupForm(forms.ModelForm):
    class Meta:
        model = SectionGroup
        fields = '__all__'

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

class CourseOptionGroupForm(forms.ModelForm):
    class Meta:
        model = CourseOptionGroup
        fields = '__all__'

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentRoleForm(forms.ModelForm):
    class Meta:
        model = StudentRole
        fields = '__all__'

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

class ExternalCollegeForm(forms.ModelForm):
    class Meta:
        model = ExternalCollege
        fields = '__all__'

class TransferEquivalencyForm(forms.ModelForm):
    class Meta:
        model = TransferEquivalency
        fields = '__all__'

class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = '__all__'

class PrerequisiteForm(forms.ModelForm):
    class Meta:
        model = Prerequisite
        fields = '__all__'

class StudentDegreePlanForm(forms.ModelForm):
    class Meta:
        model = StudentDegreePlan
        fields = '__all__'
