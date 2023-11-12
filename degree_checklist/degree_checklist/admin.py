from django import forms
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from django.template.response import TemplateResponse
from .models import College, Department, Course, SectionGroup, Section, CourseOptionGroup, Program, Student, StudentRole, Semester, ExternalCollege, TransferEquivalency, StudentCourse, Prerequisite, StudentDegreePlan
from .import_data import import_students_from_csv
import csv
import io


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.action(description='Import CSV')
def import_csv_general(modeladmin, request, queryset):
    if 'apply' in request.POST:
        form = CsvImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = io.TextIOWrapper(
                request.FILES['csv_file'].file, encoding=request.encoding)
            reader = csv.reader(csv_file)
            for row in reader:
                # Here, process each row as needed
                pass
            modeladmin.message_user(request, "CSV file has been imported")
            return redirect("..")
    return render(request, 'admin/csv_form.html', {'form': CsvImportForm()})


@admin.action(description='Export to CSV')
def export_csv_general(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    for obj in queryset:
        # Adjust these fields according to your model
        writer.writerow([obj.name])
    return response


class MyModelAdmin(admin.ModelAdmin):
    change_list_template = "admin/student_changelist.html"
    actions = [import_csv_general, export_csv_general]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            import_students_from_csv(csv_file)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return TemplateResponse(request, "admin/csv_form.html", payload)


class StudentAdmin(admin.ModelAdmin):
    change_list_template = "admin/student_changelist.html"
    actions = [import_csv_general, export_csv_general]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            import_students_from_csv(csv_file)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return TemplateResponse(request, "admin/csv_form.html", payload)


# Register models here.
admin.site.register(College, MyModelAdmin)
admin.site.register(Department, MyModelAdmin)
admin.site.register(Course, MyModelAdmin)
admin.site.register(SectionGroup, MyModelAdmin)
admin.site.register(Section, MyModelAdmin)
admin.site.register(CourseOptionGroup, MyModelAdmin)
admin.site.register(Program, MyModelAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentRole, MyModelAdmin)
admin.site.register(Semester, MyModelAdmin)
admin.site.register(ExternalCollege, MyModelAdmin)
admin.site.register(TransferEquivalency, MyModelAdmin)
admin.site.register(StudentCourse, MyModelAdmin)
admin.site.register(Prerequisite, MyModelAdmin)
admin.site.register(StudentDegreePlan, MyModelAdmin)
