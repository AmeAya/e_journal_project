from django.contrib import admin
from .models import *
from django import forms
from django.urls import reverse
from django.utils.html import urlencode, format_html

# Register your models here.
admin.site.register(Group)
admin.site.register(Grade)
admin.site.register(Exams)
admin.site.register(Attendance)
admin.site.register(Subject)

class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_name(self):
        if self.cleaned_data['name'] == 'Banana':
            raise forms.ValidationError('Banana is not a Name!')

        return self.cleaned_data['name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = ('name', 'surname', 'group_link', 'average_grade')
    list_filter = ('group',)
    search_fields = ('surname__startswith', )

    class Meta:
        ordering = ('surname', 'name')
        # sorting by fields

    def average_grade(self, obj):
        from django.db.models import Avg
        result = Grade.objects.filter(student=obj).aggregate(Avg('points'))
        return format_html('<b>{}</b>', result['points__avg'])

    def group_link(self, obj):
        url = (
            reverse("admin:e_journal_app_group_changelist") + str(obj.group.id)
        )
        return format_html("<a href=" + url + ">" + obj.group.name + "</a>")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    filter_horizontal = ('subject',)
