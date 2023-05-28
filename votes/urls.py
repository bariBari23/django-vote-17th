from django.urls import path
from .views import *

app_name = 'votes'

urlpatterns = [
    path('team/', TeamVoteView.as_view()),

]
