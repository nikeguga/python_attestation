import csv
import logging
import argparse

class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
        - name (str): ФИО студента
        - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

    Методы:
        - __init__(self, name, subjects_file): конструктор класса
        - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
        - __getattr__(self, name): получение значения атрибута
        - __str__(self): возвращает строковое представление студента
        - load_subjects(self, subjects_file): загрузка предметов из файла CSV
        - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
        - get_average_grade(self): возвращает средний балл по всем предметам
        - add_grade(self, subject, grade): добавление оценки по предмету
        - add_test_score(self, subject, test_score): добавление результата теста по предмету
    """

    subjects = ["Математика", "Физика", "История", "Литература"]  # Доступные предметы

    def __init__(self, name, subjects_file):
        """
        Конструктор класса.
        """
        self.name = name
        self.subjects = {}

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        try:
            self.load_subjects(subjects_file)
        except FileNotFoundError as e:
            logger.error(f"Ошибка при загрузке файла предметов: {e}")
            raise
        except Exception as e:
            logger.exception(f"Непредвиденная ошибка: {e}")
            raise

    def __setattr__(self, name, value):
        """
        Дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
        """
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        """
        Получение значения атрибута
        """
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        """
        Возвращает строковое представление студента
        """
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        """
        Загрузка предметов из файла CSV
        """
        with open(subjects_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def get_average_test_score(self, subject):
        """
        Возвращает средний балл по тестам для заданного предмета
        """
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        """
        Возвращает средний балл по всем предметам
        """
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_
