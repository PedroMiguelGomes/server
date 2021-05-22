# serializers.py
from rest_framework import serializers

from .models import User
from .models import Question



class RemainingQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'chapter', 'number')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer1', 'answer2', 'answer3', 'answer4', 'correct', 'score', 'chapter', 'number')

class UserSerializer1(serializers.ModelSerializer):
    questions = RemainingQuestionsSerializer(read_only=True, many=True)
    
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'score', 'questions')

class ProgressSerializer(serializers.ModelSerializer):
    questions = RemainingQuestionsSerializer(read_only=True, many=True)

    def get_questions(self, obj):
        return "%i" % obj.questions.count()

    class Meta:
        model = User
        fields = ['questions']

class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)


    def restore_object(self, attrs, instance=None):
    
        if instance is not None:
            instance.id = attrs.get('id', instance.id)
            instance.name = attrs.get('name', instance.name)
            return instance
        return UserSerializer(**attrs)