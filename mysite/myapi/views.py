from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.db.models import Count

from .serializers import UserSerializer, QuestionSerializer, ProgressSerializer, TasksSerializer

from .models import User, Question, Progress, Tasks

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('server')



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    
    def get_object(request):
        return User.objects.get(id=request.kwargs['userID'])

class Users(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer    

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all().order_by('id')
    serializer_class = TasksSerializer


class ProgressLevel(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    
    @api_view(['GET'])
    def list(request, userID, level):

        logger.error("UserID: %s  Level: %s", userID, level)
        
        total_restante = len(User.objects.get(id=userID).questions.all().filter(chapter=level))
        total = len(Question.objects.filter(chapter=level))

        aux=1-(total_restante/total)
        
        data = {'progress': int(aux*100)}
        return Response(data)

    
class Progress(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer

    @api_view(['GET'])
    def list(request, userID):
        total_restante1 = len(User.objects.get(id=userID).questions.all().filter(chapter=1))
        total1 = len(Question.objects.filter(chapter=1))
        aux1 = 1-(total_restante1/total1)

        total_restante2 = len(User.objects.get(id=userID).questions.all().filter(chapter=2))
        total2 = len(Question.objects.filter(chapter=2))
        aux2 = 1-(total_restante2/total2)

        total_restante3 = len(User.objects.get(id=userID).tasksInst.filter(centerService="general"))
        total3 = len(Tasks.objects.filter(centerService="general"))
        aux3 = 1-(total_restante3/total3)

        total_restante4 = len(User.objects.get(id=userID).questions.all().filter(chapter=3))
        total4 = len(Question.objects.filter(chapter=3))
        aux4 = 1-(total_restante4/total4)


        data = {'progress': {'1': int(aux1*100), '2': int(aux2*100), '3': int(aux3*100), '4': int(aux4*100)}}
        return Response(data)


class Questions(viewsets.ViewSet):
    
    serializer_class = QuestionSerializer

    @api_view(['GET'])
    def list(request, level, question):
        data = {'question': Question.objects.filter(chapter=level, number=question).values('id','question','answer1','answer2','answer3','answer4','chapter','correct','score','number')}
        return Response(data)

class QuestionX(viewsets.ViewSet):
    
    serializer_class = QuestionSerializer

    @api_view(['GET'])
    def list(request, userID, level, question):
        aux = User.objects.get(id=userID).questions.all().filter(chapter=level, number=question).values('id','chapter','number')
        
        logger.error(aux)

        if aux.exists():
            data = {'question': 'false'}
        else:
            data = {'question': 'true'}
        return Response(data)

class UpdateUserQuestion(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    @api_view(['POST'])
    def list(request, userID, questionID):
        aux = User.objects.get(id=userID).questions.all().get(id=questionID)
        User.objects.get(id=userID).questions.remove(aux)
        scoreAux = User.objects.get(id=userID)
        scoreAux.score += int(aux.score)
        scoreAux.save()
        logger.error(aux)

        return Response(status=status.HTTP_200_OK)

class UpdateUserTask(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    @api_view(['POST'])
    def list(request, userID, taskID):
        aux = User.objects.get(id=userID).tasksInst.all().get(id=taskID)
        User.objects.get(id=userID).tasksInst.remove(aux)
        scoreAux = User.objects.get(id=userID)
        scoreAux.score += int(aux.score)
        scoreAux.save()
        logger.error(aux)

        return Response(status=status.HTTP_200_OK)


class AddUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    @api_view(['GET'])
    def list(request, namePar):
        perguntas = Question.objects.all()
        aux = User(namePar, 'mail@email.com', 'pass', 'score', perguntas)
        aux.save()

        data = {'user': User.objects.get(name=namePar)}

        return Response(data)