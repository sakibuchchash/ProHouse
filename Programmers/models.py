from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from .cf import C
from .cc import CC
from .cfrank import rating
from .tags import List


class Posts(models.Model):
        author = models.ForeignKey('User', on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        is_contest=models.BooleanField(default=False)
        link = models.URLField(blank=True, null=True)
        soln = models.URLField(blank=True, null=True)
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()
            
        def __str__(self):
            return self.title


class Contests(models.Model):
    publisher = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    link = models.URLField(blank=True, null=True)
    soln = models.TextField(max_length=400)
    
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    student_Id=models.IntegerField(null=True, unique=True,)
    mobile_No=models.CharField(max_length=11,null=True)
    uVa_Handle=models.CharField(max_length=100,null=True,blank=True)
    codeforces_Handle=models.CharField(max_length=100,null=True,blank=True)
    codechef_Handle=models.CharField(max_length=100,null=True,blank=True)
    uVa_Rating=models.IntegerField(null=True)
    codeforces_Rank=models.CharField(max_length=100,null=True,blank=True)
    codeforces_Rating=models.IntegerField(null=True)
    codeforces_MaxRating=models.IntegerField(null=True)
    codechef_Rating=models.IntegerField(null=True)
    

    def rate(self):
            self.codeforces_Rating
            self.save()
            

    def __str__(self):
        return self.username

class Problemslist(models.Model):
    pro=models.OneToOneField('User',on_delete=models.CASCADE,null=True)
    implementation=models.IntegerField(null=True)
    data_structures=models.IntegerField(null=True)
    divide_and_conquer=models.IntegerField(null=True)
    greedy=models.IntegerField(null=True)
    dp=models.IntegerField(null=True)
    graphs=models.IntegerField(null=True)
    bfs_dfs=models.IntegerField(null=True)
    math=models.IntegerField(null=True)
    strings=models.IntegerField(null=True)
    geometry=models.IntegerField(null=True)
    probabilities=models.IntegerField(null=True)
    algorithms=models.IntegerField(null=True)
    ad_hoc=models.IntegerField(null=True)
    others=models.IntegerField(null=True)
    total_solve=models.IntegerField(null=True)


class Train(models.Model):
        author = models.ForeignKey('User', on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        link = models.URLField(blank=True, null=True)
        created_date = models.DateTimeField(blank=True, null=True)

        def publish(self):
            self.created_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title



def tag():
    pros=User.objects.all().values_list('username','codeforces_Handle', flat=False)
    for u in pros:
        if u[1] != None:
            user = User.objects.filter(username=u[0]).values('id',)
            solved=List(u[1])
            imp=[0]*15 
            for x in solved[1]:
                if x=='implementation':
                    imp[0]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(implementation=imp[0])

                elif x=='data structures' or x=='sortings' or x=='matrices' or x=='dsu' or x=='hashing' :
                    imp[1]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(data_structures=imp[1])
 
                elif x=='divide and conquer' or x=='binary search' or x=='ternary search':
                    imp[2]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(divide_and_conquer=imp[2])

                elif x=='greedy':
                    imp[3]+=solved[1][x]
                    Problemslist.objects.filter(pro__in=user).update(greedy=imp[3])

                elif x=='dp':
                    imp[4]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(dp=imp[4])

                elif x=='trees' or x=='graphs' or x=='shortest paths' or x=='graph matchings':
                    imp[5]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(graphs=imp[5])
 
                elif x=='dfs and similar':
                    imp[6]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(bfs_dfs=imp[6])

                elif x=='math' or x=='number theory' or x=='combinatorics':
                    imp[7]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(math=imp[7])

                elif x=='strings':
                    imp[8]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(strings=imp[8])


                elif x=='geometry':
                    imp[9]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(geometry=imp[9])
 
                elif x=='probabilities':
                    imp[10]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(probabilities=imp[10])

                elif x=='constructive algorithms' or x=='bitmasks' or x=='fft' or x=='two pointers' or x=='string suffix structures' or x=='flows' :
                    imp[11]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(algorithms=imp[11])

                elif x=='meet-in-the-middle' or  x=='games' or x=='brute force' or x=='chinese remainder theorem' or x=='expression parsing' or x=='2-sat':
                    imp[12]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(ad_hoc=imp[12])

                else:
                    imp[13]+=solved[1][x] 
                    Problemslist.objects.filter(pro__in=user).update(others=imp[13])


def cf():
    oute=User.objects.all().values_list('codeforces_Handle', flat=True)
    for out in oute:
        if out == None :
            out= " "
        else:    
            ge=rating(out)

            User.objects.filter(codeforces_Handle=out).update(codeforces_Rating=ge['rating'])
            User.objects.filter(codeforces_Handle=out).update(codeforces_Rank=ge['rank'])            
            User.objects.filter(codeforces_Handle=out).update(codeforces_MaxRating=ge['maxRating'])

def cc():
    oute=User.objects.all().values_list('codechef_Handle', flat=True)
    for out in oute:
        if out == None :
            out= " "
        else:    
            ge=CC(out)
            User.objects.filter(codechef_Handle=out).update(codechef_Rating=ge)            
