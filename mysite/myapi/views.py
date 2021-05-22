from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse


from django.db.models import Count

from .serializers import UserSerializer, QuestionSerializer, ProgressSerializer, UserSerializer1

from .models import User
from .models import Question, Progress

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('server')



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer1
    
    def get_object(self):
        return User.objects.get(id=self.kwargs['userID'])
    

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

class ProgressLevel(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    
    def get_object(self):
        userid = self.kwargs['userID']
        level = self.kwargs['level']

        logger.error("UserID: %s  Level: %s", userid, level)
        
        total_restante = len(User.objects.get(id=userid).questions.all().filter(chapter=level))
        total = len(Question.objects.filter(chapter=level))

        logger.error(total_restante)
        logger.error(total)

        aux=Progress(1-(total_restante/total))
        logger.error(aux.progress)
        
        return aux