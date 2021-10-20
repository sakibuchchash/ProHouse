from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import student_required
#from ..forms import StudentInterestsForm, StudentSignUpForm, TakeQuizForm,ProgrammersChangeForm
#from ..models import Quiz, Student, TakenQuiz, User
from ..models import  User,Problemslist,Train
from ..forms import  StudentSignUpForm,ProgrammersChangeForm,TrainForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth import update_session_auth_hash
from ..models import cf,cc,tag

import time
from django.db.models import Max,Avg
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from ..fusioncharts import FusionCharts
from ..problist import getProb


def lis(request,user):
    pro=User.objects.get(username=user)
    prob=Problemslist.objects.get(pro=pro.id)
    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Your Most Accepted Problems Type "
    #chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Problem Tags"
    chartConfig["yAxisName"] = "Accepted  Count  Streak"
    #chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
    chartData = OrderedDict()
    chartData["implementation"] = prob.implementation
    chartData["data structures"] = prob.data_structures
    chartData["divide and conquer"] = prob.divide_and_conquer
    chartData["greedy"] = prob.greedy
    chartData["dp"] = prob.dp
    chartData["graphs"] = prob.graphs
    chartData["bfs dfs"] = prob.bfs_dfs
    chartData["math"] = prob.math
    chartData["strings"] = prob.strings
    chartData["geometry"] = prob.geometry
    chartData["probabilities"] = prob.probabilities
    chartData["algorithms"] = prob.algorithms
    chartData["ad_hoc"] = prob.ad_hoc
    chartData["others"] = prob.others
 
    dataSource["chart"] = chartConfig
    dataSource["data"] = []

 
    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    li={}
    mx=0
    val=[0]*15
    for key, value in chartData.items():
        if value !=None:
           if value > mx:
                mx=value
                li[0]=key
    mx=0
    for key, value in chartData.items():
        if key != li[0]:
            if value !=None:
                if value > mx:
                    mx=value
                    li[1]=key
    mx=0
    for key, value in chartData.items():
        if key != li[0] and key != li[1]:
            if value !=None:
                if value > mx:
                    mx=value
                    li[2]=key
    top={}
    i=0  
             
    for x in li:
        top[i]=getProb(user,li[x])
        i+=1


    return render(request, 'list.html',{'top':top,'li':li,'pro':pro} )



def prosugg(request,user):
    pro=User.objects.get(username=user)
    prob=Problemslist.objects.get(pro=pro.id)
    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Your Most Accepted Problems Type "
    #chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Problem Tags"
    chartConfig["yAxisName"] = "Accepted  Count  Streak"
    #chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
    chartData = OrderedDict()
    chartData["implementation"] = prob.implementation
    chartData["data structures"] = prob.data_structures
    chartData["divide and conquer"] = prob.divide_and_conquer
    chartData["greedy"] = prob.greedy
    chartData["dp"] = prob.dp
    chartData["graphs"] = prob.graphs
    chartData["bfs dfs"] = prob.bfs_dfs
    chartData["math"] = prob.math
    chartData["strings"] = prob.strings
    chartData["geometry"] = prob.geometry
    chartData["probabilities"] = prob.probabilities
    chartData["algorithms"] = prob.algorithms
    chartData["ad_hoc"] = prob.ad_hoc
    chartData["others"] = prob.others
 
    dataSource["chart"] = chartConfig
    dataSource["data"] = []

 
    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
   
    for key, value in chartData.items():
        
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "myFirstChart", "1100", "600", "myFirstchart-container", "json", dataSource)


    return render(request, 'prosugg.html',{'output': column2D.render() ,'pro':pro} )


def proupdate(request,user):
    #tag()
    cf()
    cc()
   # print(Problemslist.objects.all().aggregate(Max('math')))
   
    return redirect('ProgrammersProfile',user=user)

def update(request):
    cf()
    cc()
    return redirect('ranks')

def train(request):
    posts = Train.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    by = Train.objects.all        
    return render(request, 'train.html', {'posts': posts,'by':by})

def train_new(request):
    if request.method == "POST":
        form = TrainForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('train')
    else:
        form = TrainForm()
    return render(request, 'train_edit.html', {'form': form})

def train_edit(request, pk):
    post = get_object_or_404(Train, pk=pk)

    if request.method == "POST":
        form = TrainForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save() 
            return redirect('train')
    else:
        form = TrainForm(instance=post)
    return render(request, 'train_edit.html', {'form': form})



def teacher(request):

    posts = User.objects.filter().order_by('username').exclude(student_Id__isnull=False)    
    return render(request, 'teachers.html', {'posts': posts})


class ProgrammersPassword(PasswordContextMixin,FormView):
    form_class = PasswordChangeForm
    success_url = ('/posts')
    template_name = 'Password.html'
    title = ('Password change')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

def Contests(request):

    posts = User.objects.filter().exclude(is_student=False)  
    return render(request, 'contests.html', {'posts': posts})


def Programmers(request):

    posts = User.objects.filter().order_by('student_Id').exclude(student_Id__isnull=True)    
    return render(request, 'Programmers.html', {'posts': posts})


def ranks(request):

    posts = User.objects.filter().order_by('-codeforces_Rating').exclude(student_Id__isnull=True)
    return render(request, 'ranks.html', {'posts': posts})

"""
def codeforces(request, pk):
    out=C("SAdrulToaha")
    return render(request, 'registration/profile.html',{'out':out}) """



def ProgrammersProfile(request,user):
        pro=User.objects.get(username=user)
        #prob=Problemslist.objects.get(pro=pro.id)

        codeforces=pro.codeforces_Rating
        codechef=pro.codechef_Rating
        username=pro.username
        first_name=pro.first_name
        last_name=pro.last_name
        email=pro.email
        mobile_No=pro.mobile_No 
        student_Id=pro.student_Id
        cf_title="Codeforces Rating:"
        cc_title="Codechef Rating:"
        id_title="Student Id:"
        if pro.is_student:
            return render(request,'profile.html',{'pro': pro,'username':username,'id_title':id_title,'cc_title':cc_title,'cf_title':cf_title,'student_Id':student_Id,'codechef':codechef ,'codeforces':codeforces ,'first_name':first_name,'last_name':last_name,'email':email,'mobile_No':mobile_No})
        else :
            return render(request,'profile.html',{'username':username,'first_name':first_name,'last_name':last_name,'email':email,'mobile_No':mobile_No})

def ProgrammersProfile_edit(request,user):
    user = request.user
    if request.method == 'POST':

        form = ProgrammersChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('ProgrammersProfile',user=user)
    else:
        form = ProgrammersChangeForm(instance=user)
    context = {'form': form}
    return render(request, 'profile_edit.html', context)

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)            
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        tag()
        cf()
        cc()
        return redirect('ProgrammersProfile',user=user)
