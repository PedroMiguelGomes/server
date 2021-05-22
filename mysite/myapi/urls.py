# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'questions', views.QuestionsViewSet)
router.register(r'progress', views.ProgressLevel, basename='progress')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:userid>/', views.UserViewSet.getUser),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]