from rest_framework import serializers
from quizzes.models import Quiz, Question, Answer, Category


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)
    right_answer = AnswerSerializer(required=False)

    class Meta:
        model = Question
        fields = ('id', 'question', 'answers', 'right_answer')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Quiz
        fields = ('id', 'name', 'theme', 'description', 'questions', 'question_points', 'question_time', 'category', 'quiz_type')
