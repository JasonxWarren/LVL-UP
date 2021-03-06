import imp
from plistlib import PlistFormat
import re
from token import GREATER
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Goals, Sponsor
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
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
@method_decorator(login_required, name='dispatch')
class GoalList(TemplateView):
    template_name='goallist.html'


    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        # user = self.request.GET.get('user')
        
        if name != None:
            context["goals"]=Goals.objects.filter(name__icontains=name).filter(user = self.request.user)
        else: 
            context["goals"]= Goals.objects.filter(user = self.request.user)
        return context
@method_decorator(login_required, name='dispatch')
class Goals_Create(CreateView):
    model = Goals
    fields = ['name','description','dailyz','sponsors']
    template_name='goals_create.html'
    def get_success_url(self):
        return reverse("goal-detail", kwargs={'pk':self.object.pk})
    # success_url = "/goals/"
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/goals/')
@method_decorator(login_required, name='dispatch')
class GoalDetail(DetailView):
    model=Goals
    template_name='goal_detail.html'
    # def get_context_data(self,*args, **kwargs):
    #     context = super(GoalDetail, self).get_context_data(*args,**kwargs)
    #     context['Sponsor']=Sponsor.objects.all()
    #     return context
@method_decorator(login_required, name='dispatch')
class GoalUpdate(UpdateView):
    model=Goals
    fields = ['name','description','dailyz','sponsors']
    template_name='goal_update.html'
    success_url="/goals/"
    def get_success_url(self):
        return reverse("goal-detail", kwargs={'pk':self.object.pk})
    # success_url = "/goals/"
@method_decorator(login_required, name='dispatch')
class GoalDelete(DeleteView):
    model= Goals
    template_name='goal-delete-confirmation.html'
    success_url="/goals/"
@login_required
def profile(request, username):
    user=User.objects.get(username=username)
    goals=Goals.objects.filter(user=user)
    return render(request, 'profile.html', {'username':username, 'goals':goals})

def sponsors_index(request):
    sponsors=Sponsor.objects.all()
    return render(request, 'sponsor_index.html', {'sponsors':sponsors})

def sponsors_show(request, sponsor_id):
    sponsor=Sponsor.objects.get(id=sponsor_id)
    return render(request, 'sponsor_show.html',{'sponsor':sponsor})


class SponsorUpdate(UpdateView):
    model= Sponsor
    fields=['sponsor_name']
    template_name='sponsor_update.html'
    success_url = "/sponsors/"

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hello', user.username)
            return HttpResponseRedirect('/user/'+ str(user))
        else:
            return render(request, 'signup.html', {"form": form})
    else: 
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})
