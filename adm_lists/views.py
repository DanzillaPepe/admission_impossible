from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Admission, Student


def IndexView(request):
    columns = ['number',
               'id',
               'full_name',
               'birthday',
               'total',
               'exam_sum',
               'exam_1',
               'exam_2',
               'exam_3',
               'bonus_sum',
               ]
    headings = ['№',
                'ID',
                'Имя',
                'День рождения',
                'Общая сумма',
                'Сумма ЕГЭ',
                'Экзамен 1',
                'Экзамен 2',
                'Экзамен 3',
                'Доп. баллы',
                ]
    n = Student.objects.count()
    students = Student.objects.order_by('full_name')
    i = 1
    for student in students:
        student.number = i
        i += 1
    students_list = list(students)
    final_list = list()
    for student in students_list:
        to_add = list()
        for element in columns:
            to_add.append(getattr(student, element))
        final_list.append(to_add)
    context = {
        'headings': headings,
        'data': final_list,
    }

    return render(request, 'adm_lists/index.html', context)


def DirectionsView(request):
    dir_list = Admission.objects.values_list('direction')
    context = {
        'dir_list': dir_list,
    }

    return render(request, 'adm_lists/directions.html', context)
