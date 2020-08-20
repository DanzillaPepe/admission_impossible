from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Admission

ELEMENTS = ['number',
            'full_name',
            'birthday',
            'exam_sum',
            'exam_1',
            'exam_2',
            'exam_3',
            'priority',

            ]
HEADINGS = ['№',
            'Имя',
            'День прждения',
            'Сумма ЕГЭ',
            'Экзамен 1',
            'Экзамен 2',
            'Экзамен 3',
            'Приоритет']

def IndexView(request):
    n = Admission.objects.count()
    students = Admission.objects.order_by('-exam_sum')
    i = 1
    for student in students:
        student.number = i
        i += 1
    students_list = list(students)
    final_list = list()
    for student in students_list:
        to_add = list()
        for element in ELEMENTS:
            to_add.append(getattr(student, element))
        final_list.append(to_add)
    a = 0
    context = {
        'headings': HEADINGS,
        'data': final_list,
    }

    return render(request, 'adm_lists/index.html', context)
