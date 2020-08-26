from django.db import models
from django.utils import timezone
import uuid
from datetime import datetime


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for Subject")
    name = models.CharField(max_length=50, default='')


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for Student")
    name = models.CharField(max_length=50, default='')
    birthday = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Score(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for Score")
    subject = models.ForeignKey(Subject, default=0, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.IntegerField(default=0)


class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for University")
    title = models.CharField(max_length=50, default='')


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for Faculty")
    title = models.CharField(max_length=50, default='')
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Direction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for Direction")
    title = models.CharField(max_length=50, default='')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for Program")
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                          help_text="Unique ID for Admission")

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
        # managed = False

        verbose_name = 'admission'
        verbose_name_plural = 'admissions'
