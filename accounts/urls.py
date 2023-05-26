from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('', ProfileView.as_view()),
    # path('likes/', LikedListView.as_view()),
    # path('health/', HealthView.health)
]