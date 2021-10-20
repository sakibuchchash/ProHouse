from django.shortcuts import redirect, render,get_object_or_404
from django.views.generic import TemplateView

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('index')
        else:
            return redirect('index')
    return render(request, 'home.html')


class SignUpView(TemplateView):
    template_name = 'signup.html'

def cof():
	oute=User.objects.get(username=User.username)
	if oute.codeforces_Handle == None :
		oute.codeforces_Handle= " You Have No CF Id "
	else:    
		ge=C(oute.codeforces_Handle)
		User.objects.filter(username=User.username).update(codeforces_Rating=ge)           


		