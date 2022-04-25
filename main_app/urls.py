from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('goals/', views.GoalList.as_view(), name="goal-list"),
    path('goals/new/', views.Goals_Create.as_view(), name="goals-create"),
    path('goals/<int:pk>/', views.GoalDetail.as_view(), name="goal-detail"),
    path('goals/update/<int:pk>/', views.GoalUpdate.as_view(), name="goal-update"),
    path("goals/<int:pk>/delete", views.GoalDelete.as_view(), name="goal-delete"),
    path('user/<username>', views.profile, name='profile'),
    path('sponsors/', views.sponsors_index, name='sponsors-index'),
    path('sponsors/<int:sponsor_id>/', views.sponsors_show, name='sponsors-show'),
    path('sponsors/<int:pk>/update/', views.SponsorUpdate.as_view(), name="sponsor-update"),
    path('accounts/signup/', views.signup_view, name="signup"),
]