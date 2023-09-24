from django.contrib import admin
from quizzes.models import Quiz, Question, Answer, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer')
    list_filter = ('id', 'answer')
    search_fields = ('id', 'answer')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'right_answer')
    list_filter = ('id', 'question', 'right_answer')
    search_fields = ('id', 'question', 'right_answer')


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'theme', 'description', 'question_points', 'question_time', 'category', 'quiz_type')
    list_filter = ('id', 'name', 'theme', 'description', 'question_points', 'category', 'quiz_type')
    search_fields = ('id', 'name', 'theme')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category, CategoryAdmin)
