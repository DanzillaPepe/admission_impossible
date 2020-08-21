# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from datetime import datetime


class Admission(models.Model):
    scrape_date = models.DateTimeField()
    url = models.CharField(max_length=50)
    updated = models.DateTimeField()
    university = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    contract = models.CharField(max_length=50)
    places = models.IntegerField()
    spec_places = models.IntegerField()
    target_places = models.IntegerField()
    appl_count = models.IntegerField()
    row_id = models.IntegerField()
    reg_num = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    birthday = models.DateField()
    contract_type = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    total = models.IntegerField()
    exam_sum = models.IntegerField()
    exam_1 = models.IntegerField()
    exam_2 = models.IntegerField()
    exam_3 = models.IntegerField()
    bonus_sum = models.IntegerField()
    agreement = models.IntegerField()
    bonus_str = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'admission'


class Exam(models.Model):
    subject_name = models.CharField(max_length=50, default='')
    average = models.IntegerField(default=0)


class Student(models.Model):
    name = models.CharField(max_length=50, default='')
    birthday = models.DateTimeField(default=timezone.now())
    exams = models.ManyToManyField(Exam)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Direction(models.Model):
    d_id = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=50, default='')
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
