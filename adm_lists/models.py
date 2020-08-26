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


class Subject(models.Model):
    name = models.CharField(max_length=50, default='')


class Student(models.Model):
    name = models.CharField(max_length=50, default='')
    birthday = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Score(models.Model):
    subject = models.ForeignKey(Subject, default=0, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.IntegerField(default=0)


class University(models.Model):
    title = models.CharField(max_length=50, default='')


class Faculty(models.Model):
    faculty_id = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=50, default='')
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Direction(models.Model):
    direction_id = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=50, default='')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Program(models.Model):
    program_id = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=50, default='')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    places = models.IntegerField()  # Кол-во мест
    spec_places = models.IntegerField()  # Места по особой квоте
    target_places = models.IntegerField()  # Целевые места
    appl_count = models.IntegerField()  # Кол-во поданных заявлений

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    # CHARACTERISTICS
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, models.CASCADE)
    direction = models.ForeignKey(Direction, models.CASCADE)
    program = models.ForeignKey(Program, models.CASCADE)
    level = models.CharField(max_length=50)  # Бакалавриат etс
    type = models.CharField(max_length=50)  # Очный / заочный
    contract = models.CharField(max_length=50)  # Платка / Бюджет
    contract_type = models.CharField(max_length=50)  # БВИ, договор, вне конкурса etc

    # PERSONAL
    reg_num = models.CharField(max_length=50)  # Рег. номер
    priority = models.CharField(max_length=50)  # Приоритет
    agreement = models.IntegerField()  # Наличие согласия

    # EXAM POINTS
    total = models.IntegerField()
    exam_sum = models.IntegerField()
    exam_1 = models.IntegerField()
    exam_2 = models.IntegerField()
    exam_3 = models.IntegerField()
    bonus_sum = models.IntegerField()
    bonus_str = models.CharField(max_length=50)  # Олимпиады
    comment = models.CharField(max_length=50)  # Комментарий (олимпиада БВИ etc)

    # RATING
    row_id = models.IntegerField()  # Место в списке

    # TECHNICAL
    scrape_date = models.DateTimeField()
    url = models.CharField(max_length=50)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admission'
