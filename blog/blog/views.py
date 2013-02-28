from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from blog.content.models import *

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

  
def login(request):
  username_f= request.POST.get('username','')
  password_f= request.POST.get('password','')
  #button_log = request.POST.get('log_in','')    
  user = auth.authenticate(username=username_f, password=password_f)
  v={}
  if user:
    auth.login(request, user)
    v['title']='You are logged in'
    v['message']= 'Welcome, '
    v['user']=username_f
    return render_to_response('member.html',v)
  else:
    v['title']="Fail"
    v['usern']=username_f
    v['pass']=password_f
    v['message']='Wrong username or password. Try again!'
    return render_to_response('index.html',v)
    
def root(request):
    v={}
    v['title']="Welcome to MiBlog login, sign up or learn more!"
    v['post_list']=Post.objects.all()
    return render_to_response('index.html',v)

def save_p(request):
  tit=request.POST.get('tit','')
  bod=request.POST.get('body','')
  cont=Post(title=tit,body=bod)
  cont.save()
  return HttpResponse("Post Saved!")

    
