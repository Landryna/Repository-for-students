from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
 articles = Article.objects.all().order_by('grupa','nazwa')
 return render(request,'articles/article_list.html',{'articles':articles})
 
def article_detail(request,slug):
 #return HttpResponse(slug)
 article = Article.objects.get(slug=slug)
 return render(request,'articles/article_detail.html',{'article':article})
#POTEM ZROB GROUPS
#def article_group(request,group):
 #artgroup = Article.objects.get(group=group)
 #return render(request,'articles/article_detail.html',{'artgroup':artgroup}) 
  #return HttpResponse(group)
@login_required(login_url="/accounts/login/")
def article_create(request):
 if request.method == 'POST':
  form=forms.CreateArticle(request.POST,request.FILES)
  if form.is_valid():
   instance = form.save(commit=False)
   instance.autor = request.user
   instance.save()
   return redirect('articles:list')
 else: 
  form = forms.CreateArticle()
 return render(request,'articles/article_create.html',{'form':form })  