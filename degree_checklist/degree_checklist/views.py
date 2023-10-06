from django.shortcuts import render
from .models import (
    College, Department, Course, SectionGroup,
    Section, CourseOptionGroup, Program, Student,
    StudentRole, Semester, ExternalCollege, TransferEquivalency,
    StudentCourse, Prerequisite, StudentDegreePlan
)

def cis_records_view(request):
    context = {
        'colleges': College.objects.all(),
        'departments': Department.objects.all(),
        'courses': Course.objects.all(),
        'section_groups': SectionGroup.objects.all(),
        'sections': Section.objects.all(),
        'course_option_groups': CourseOptionGroup.objects.all(),
        'programs': Program.objects.all(),
        'students': Student.objects.all(),
        'student_roles': StudentRole.objects.all(),
        'semesters': Semester.objects.all(),
        'external_colleges': ExternalCollege.objects.all(),
        'transfer_equivalencies': TransferEquivalency.objects.all(),
        'student_courses': StudentCourse.objects.all(),
        'prerequisites': Prerequisite.objects.all(),
        'student_degree_plans': StudentDegreePlan.objects.all(),
    }
    return render(request, 'cis_records.html', context)
