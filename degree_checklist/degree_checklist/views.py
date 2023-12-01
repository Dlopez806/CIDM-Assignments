from .models import (
    College, Department, Course, SectionGroup,
    Section, CourseOptionGroup, Program, Student,
    StudentRole, Semester, ExternalCollege, TransferEquivalency,
    StudentCourse, Prerequisite, StudentDegreePlan
)
from .forms import (
    CollegeForm, DepartmentForm, CourseForm, SectionGroupForm,
    SectionForm, CourseOptionGroupForm, ProgramForm, StudentForm,
    StudentRoleForm, SemesterForm, ExternalCollegeForm, TransferEquivalencyForm,
    StudentCourseForm, PrerequisiteForm, StudentDegreePlanForm
)
from django.shortcuts import render, redirect


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


def add_model(request, form_class, template_name, redirect_view):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_view)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def add_college(request):
    return add_model(request, CollegeForm, 'add_college.html', 'cis_records')


def add_department(request):
    return add_model(request, DepartmentForm, 'add_department.html', 'cis_records')


def add_course(request):
    return add_model(request, CourseForm, 'add_course.html', 'cis_records')


def add_section_group(request):
    return add_model(request, SectionGroupForm, 'add_section_group.html', 'cis_records')


def add_section(request):
    return add_model(request, SectionForm, 'add_section.html', 'cis_records')


def add_course_option_group(request):
    return add_model(request, CourseOptionGroupForm, 'add_course_option_group.html', 'cis_records')


def add_program(request):
    return add_model(request, ProgramForm, 'add_program.html', 'cis_records')


def add_student(request):
    return add_model(request, StudentForm, 'add_student.html', 'cis_records')


def add_student_role(request):
    return add_model(request, StudentRoleForm, 'add_student_role.html', 'cis_records')


def add_semester(request):
    return add_model(request, SemesterForm, 'add_semester.html', 'cis_records')


def add_external_college(request):
    return add_model(request, ExternalCollegeForm, 'add_external_college.html', 'cis_records')


def add_transfer_equivalency(request):
    return add_model(request, TransferEquivalencyForm, 'add_transfer_equivalency.html', 'cis_records')


def add_student_course(request):
    return add_model(request, StudentCourseForm, 'add_student_course.html', 'cis_records')


def add_prerequisite(request):
    return add_model(request, PrerequisiteForm, 'add_prerequisite.html', 'cis_records')


def add_student_degree_plan(request):
    return add_model(request, StudentDegreePlanForm, 'add_student_degree_plan.html', 'cis_records')
