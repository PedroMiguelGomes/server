# serializers.py
from rest_framework import serializers

from .models import Question, Progress, User, Tasks


class RemainingQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'chapter', 'number')

class RemainingTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'task', 'type')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    questions = RemainingQuestionsSerializer(read_only=True, many=True)
    tasksInst = RemainingTasksSerializer(read_only=True, many=True)
    
    class Meta:
        model = User
        fields = ('__all__')

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('__all__')