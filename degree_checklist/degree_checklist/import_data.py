import csv
from .models import (College, Department, Course, SectionGroup, Section, CourseOptionGroup, Program,
                     Student, StudentRole, Semester, ExternalCollege, TransferEquivalency, StudentCourse,
                     Prerequisite, StudentDegreePlan)

def import_colleges_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name = row[0]
        College.objects.update_or_create(name=name)

def import_departments_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name, college_name = row
        college, _ = College.objects.get_or_create(name=college_name)
        Department.objects.update_or_create(name=name, defaults={'college': college})

def import_courses_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name, credits = row
        Course.objects.update_or_create(name=name, defaults={'credits': credits})

def import_section_groups_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name, required_credits = row
        SectionGroup.objects.update_or_create(name=name, defaults={'required_credits': required_credits})

def import_sections_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name, code, required_credits, section_group_name = row
        section_group, _ = SectionGroup.objects.get_or_create(name=section_group_name)
        Section.objects.update_or_create(name=name, defaults={'code': code, 'required_credits': required_credits, 'section_group': section_group})


def import_students_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name, email, role_name = row
        role, _ = StudentRole.objects.get_or_create(name=role_name)
        Student.objects.update_or_create(name=name, defaults={'email': email, 'role': role})

def import_student_roles_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name = row[0]
        StudentRole.objects.update_or_create(name=name)


def import_semesters_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name, year = row
        Semester.objects.update_or_create(name=name, defaults={'year': year})

def import_external_colleges_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        name = row[0]
        ExternalCollege.objects.update_or_create(name=name)

def import_transfer_equivalencies_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        external_course_name, external_course_id, equivalent_course_name, external_college_name = row
        equivalent_course, _ = Course.objects.get_or_create(name=equivalent_course_name)
        external_college, _ = ExternalCollege.objects.get_or_create(name=external_college_name)
        TransferEquivalency.objects.update_or_create(
            external_course_name=external_course_name, 
            defaults={'external_course_id': external_course_id, 'equivalent_course': equivalent_course, 'external_college': external_college}
        )

def import_student_courses_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        student_name, course_name, grade, status, semester_name = row
        student, _ = Student.objects.get_or_create(name=student_name)
        course, _ = Course.objects.get_or_create(name=course_name)
        semester, _ = Semester.objects.get_or_create(name=semester_name)
        StudentCourse.objects.update_or_create(
            student=student, course=course,
            defaults={'grade': grade, 'status': status, 'semester': semester}
        )

def import_prerequisites_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        course_name, prerequisite_course_name = row
        course, _ = Course.objects.get_or_create(name=course_name)
        prerequisite_course, _ = Course.objects.get_or_create(name=prerequisite_course_name)
        Prerequisite.objects.update_or_create(course=course, defaults={'prerequisite_course': prerequisite_course})

def import_student_degree_plans_from_csv(file):
    reader = csv.reader(file.read().decode('utf-8').splitlines())
    next(reader)  # Skip header
    for row in reader:
        student_name, program_name, degree_type = row
        student, _ = Student.objects.get_or_create(name=student_name)
        program, _ = Program.objects.get_or_create(name=program_name)
        StudentDegreePlan.objects.update_or_create(
            student=student, program=program,
            defaults={'type': degree_type}
        )


