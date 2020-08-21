from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Admission, Student, Direction
from adm_lists.headings import HEADINGS, IndexColumns, StudentColumns, DirectionColumns


def get_headings(columns):
    headings = list()
    for column in columns:
        headings.append(HEADINGS[column])
    return headings


def get_list(columns, data, numeration=False):
    if numeration:
        columns = ['number'] + columns
        i = 1
        for row in data:
            row.number = i
            i += 1
    data_list = list(data)
    final_list = list()
    for row in data_list:
        to_add = list()
        for column in columns:
            if column == "students":
                students_list = str()
                for student in getattr(row, column).all():
                    students_list += str(student)
                to_add.append(students_list)
                continue
            to_add.append(getattr(row, column))
        final_list.append(to_add)

    return final_list, columns


def IndexView(request):
    columns = IndexColumns.columns
    data = Admission.objects.order_by('full_name')

    final_list, columns = get_list(columns, data, numeration=True)

    context = {
        'headings': get_headings(columns),
        'data': final_list,
    }

    return render(request, 'adm_lists/index.html', context)


def DirectionsView(request):
    columns = DirectionColumns.columns
    dir_list = Direction.objects.all()

    final_list, columns = get_list(columns, dir_list, numeration=True)

    context = {
        'headings': get_headings(columns),
        'dir_list': final_list,
    }

    return render(request, 'adm_lists/directions.html', context)


def StudentsView(request):
    columns = StudentColumns.columns
    stud_list = Student.objects.all()

    final_list, columns = get_list(columns, stud_list, numeration=True)

    context = {
        'headings': get_headings(columns),
        'stud_list': final_list,
    }

    return render(request, 'adm_lists/students.html', context)
