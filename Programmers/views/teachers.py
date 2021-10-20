from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import teacher_required
#from ..forms import BaseAnswerInlineFormSet, QuestionForm, TeacherSignUpForm
from ..forms import TeacherSignUpForm,TeachersChangeForm
from ..models import  User
#from ..models import Answer, Question, Quiz, User

from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic.edit import FormView
from django.contrib.auth import update_session_auth_hash

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        #return redirect('teachers:quiz_change_list')
        return redirect('ProgrammersProfile',user=user)


class TeachersPassword(PasswordContextMixin,FormView):
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

def TeachersProfile(request,user):
    return redirect('ProgrammersProfile',user=user)


def TeachersProfile_edit(request,user):
    user = request.user
    if request.method == 'POST':

        form = TeachersChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('ProgrammersProfile',user=user)
    else:
        form = TeachersChangeForm(instance=user)
    context = {'form': form}
    return render(request, 'profile_edit.html', context)
