from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Admission


class IndexView(generic.ListView):
    template_name = 'adm_lists/index.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        students = Admission.objects.all().order_by("-exam_sum")
        return students


