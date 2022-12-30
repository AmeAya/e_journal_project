from rest_framework import serializers
from e_journal_app.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'group']
