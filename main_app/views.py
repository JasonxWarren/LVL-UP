import imp
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name ="home.html"

class Goal:
    def __init__(self,name,description,dailyz,duration,redeemed):
        self.name = name
        self.description = description
        self.dailyz = dailyz
        self.duration = duration
        self.redeemed = redeemed
        #self.sponsor = sponsor
        #self.user = User.objects
    
goals=[
    Goal("Push-ups","10 sets a day","5","30","False"),
    Goal("Meditate","30 minutes a day","10","30","False"),
    Goal("Leetcode","hour a day","15","30","False"),
]

class GoalList(TemplateView):
    template_name='goallist.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["goals"]= goals
        return context
