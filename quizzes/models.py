from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Answer(models.Model):
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    answers = models.ManyToManyField('Answer', blank=True, related_name='question_for', verbose_name='Ответы')
    right_answer = models.ForeignKey('Answer', blank=True, null=True, related_name='for_question', on_delete=models.DO_NOTHING, verbose_name='Правильный ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Quiz(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    theme = models.CharField(max_length=255, verbose_name='Тема')
    description = models.TextField(verbose_name='Описание')
    questions = models.ManyToManyField('Question', blank=True, verbose_name='Вопросы')
    question_points = models.IntegerField(verbose_name='Баллы за вопрос')
    question_time = models.IntegerField(verbose_name='Время ответа на вопрос')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    quiz_type = models.IntegerField(verbose_name='Тип квиза')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'



