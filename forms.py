from django import forms
from universities.models import RequiredExam


class exam_form(forms.Form):
    for code, exam_name in RequiredExam.EXAMS:
        exec(code + '= forms.IntegerField(100, 0, label=exam_name)')
