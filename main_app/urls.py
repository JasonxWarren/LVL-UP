from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('goals/', views.GoalList.as_view(), name="goal-list"),
    path('goals/new/', views.Goals_Create.as_view(), name="goals-create")
]