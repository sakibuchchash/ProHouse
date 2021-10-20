from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from Programmers.models import User,Problemslist,Train,Posts,Contests



class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'text','is_contest','link','soln',)

    def __str__(self):
        return self.author


class ContestForm(forms.ModelForm):

    class Meta:
        model = Contests
        fields = ('link', 'soln',)

    def __str__(self):
        return self.publisher


class TrainForm(forms.ModelForm):

    class Meta:
        model = Train
        fields = ('title','text','link',)

    def __str__(self):
        return self.author


class ProgrammersChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','mobile_No','uVa_Handle','codeforces_Handle','codechef_Handle')

        

class TeachersChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name','mobile_No')


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email','first_name','last_name','mobile_No')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'student_Id','email','first_name','last_name','mobile_No','uVa_Handle','codeforces_Handle','codechef_Handle')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        #student = Student.objects.create(user=user)
        problemslist= Problemslist.objects.create(pro=user)
        return user
