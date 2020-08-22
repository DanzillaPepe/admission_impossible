id = 'id'
full_name = 'student.name'
name = 'name'
birthday = 'birthday'
total = 'total'
exam_sum = 'exam_sum'
exam_1 = 'exam_1'
exam_2 = 'exam_2'
exam_3 = 'exam_3'
bonus_sum = 'bonus_sum'
title = 'title'
students = 'students'
directions = 'direction_set'

HEADINGS = {
    'number': '№',
    'id': 'ID',
    'name': 'Имя',
    'full_name': 'Имя',
    'birthday': 'День рождения',
    'total': 'Сумма баллов',
    'exam_sum': 'Сумма ЕГЭ',
    'exam_1': '1 экзамен',
    'exam_2': '2 экзамен',
    'exam_3': '3 экзамен',
    'bonus_sum': 'Доп. баллы',
    'title': 'Название',
    'students': 'Подавшие заявление',
    'direction_set': 'Направления',
}


class IndexColumns:
    columns = [id, full_name, birthday, total, exam_sum, exam_1, exam_2, exam_3, bonus_sum]


class StudentColumns:
    columns = [id, name, birthday, directions]


class DirectionColumns:
    columns = [title, students]
