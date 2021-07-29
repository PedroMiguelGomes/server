# myapi/urls.py
from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionsViewSet)
router.register(r'tasks', views.TasksViewSet)
router.register(r'users', views.Users)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    re_path('^user/(?P<userID>.+)/$', views.UserViewSet.as_view({'get': 'retrieve'})),
    re_path('^progressUser/(?P<userID>.+)/$', views.Progress.list),
    re_path('^questionLevel/(?P<level>.+)/(?P<question>.+)/$', views.Questions.list),
    re_path('^questionXLevel/(?P<userID>.+)/(?P<level>.+)/(?P<question>.+)/$', views.QuestionX.list),
    re_path('^updateUserQuestion/(?P<userID>.+)/(?P<questionID>.+)/$', views.UpdateUserQuestion.list),
    re_path('^updateUserTaskInst/(?P<userID>.+)/(?P<taskID>.+)/$', views.UpdateUserTask.list),
    re_path('^addUser/(?P<name>.+)/$', views.AddUser.list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]