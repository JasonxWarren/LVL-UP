import imp
import re
from token import GREATER
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Goals
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.views.generic import DeleteView
# Create your views here.
class Home(TemplateView):
    template_name ="home.html"

# class Goal:
#     def __init__(self,name,description,dailyz,duration,redeemed):
#         self.name = name
#         self.description = description
#         self.dailyz = dailyz
#         self.duration = duration
#         self.redeemed = redeemed
        #self.sponsor = sponsor
        #self.user = User.objects
    
# goals=[
#     Goal("Push-ups","10 sets a day","5","30","False"),
#     Goal("Meditate","30 minutes a day","10","30","False"),
#     Goal("Leetcode","hour a day","15","30","False"),
# ]

class GoalList(TemplateView):
    template_name='goallist.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["goals"]=Goals.objects.filter(name__icontains=name)
        else: 
            context["goals"]= Goals.objects.all()
        return context

class Goals_Create(CreateView):
    model = Goals
    fields = ['name','description','dailyz',]
    template_name='goals_create.html'
    def get_success_url(self):
        return reverse("goal-detail", kwargs={'pk':self.object.pk})
    # success_url = "/goals/"

class GoalDetail(DetailView):
    model=Goals
    template_name='goal_detail.html'

class GoalUpdate(UpdateView):
    model=Goals
    fields = ['name','description','dailyz']
    template_name='goal_update.html'
    success_url="/goals/"
    def get_success_url(self):
        return reverse("goal-detail", kwargs={'pk':self.object.pk})
    # success_url = "/goals/"

class GoalDelete(DeleteView):
    model= Goals
    template_name='goal-delete-confirmation.html'
    success_url="/goals/"