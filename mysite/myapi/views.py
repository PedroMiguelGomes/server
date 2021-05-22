from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response


from django.db.models import Count

from .serializers import UserSerializer, QuestionSerializer, ProgressSerializer

from .models import User
from .models import Question


class UserViewSet(viewsets.ModelViewSet):
    def getUser(request, userid=1):
        queryset = User.objects.all().filter(id=1)
        post_list = serializers.serialize('json',
                                      list(data),
                                      fields=('emp_name','email','phone'))
        return HttpResponse(post_list)
    

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

class ProgressLevel(viewsets.ModelViewSet):
    queryset = User.objects.filter(id=1).only('questions')
    queryset2 = Question.objects.all()
    serializer_class = ProgressSerializer
