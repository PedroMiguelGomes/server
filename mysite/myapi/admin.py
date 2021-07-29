from django.contrib import admin
from .models import User
from .models import Question
from .models import Tasks

# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Tasks)
