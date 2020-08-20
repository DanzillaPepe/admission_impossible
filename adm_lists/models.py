# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admission(models.Model):
    scrape_date = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    university = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    faculty = models.CharField(max_length=50, blank=True, null=True)
    direction = models.CharField(max_length=50, blank=True, null=True)
    program = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    contract = models.CharField(max_length=50, blank=True, null=True)
    places = models.IntegerField(blank=True, null=True)
    spec_places = models.IntegerField(blank=True, null=True)
    target_places = models.IntegerField(blank=True, null=True)
    appl_count = models.IntegerField(blank=True, null=True)
    row_id = models.IntegerField(blank=True, null=True)
    reg_num = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    contract_type = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    exam_sum = models.IntegerField(blank=True, null=True)
    exam_1 = models.IntegerField(blank=True, null=True)
    exam_2 = models.IntegerField(blank=True, null=True)
    exam_3 = models.IntegerField(blank=True, null=True)
    bonus_sum = models.IntegerField(blank=True, null=True)
    agreement = models.IntegerField(blank=True, null=True)
    bonus_str = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission'


class Student(models.Model):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    exam_sum = models.IntegerField(blank=True, null=True)
    exam_1 = models.IntegerField(blank=True, null=True)
    exam_2 = models.IntegerField(blank=True, null=True)
    exam_3 = models.IntegerField(blank=True, null=True)
    bonus_sum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission'


class Direction(models.Model):
    direction = models.CharField(max_length=50, blank=True, null=True)
