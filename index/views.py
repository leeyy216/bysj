from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from index.models import User

# Create your views here.
def index(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用 户 名',max_length=100)
    password = forms.CharField(label='密    码',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')

def register(request):
	if request.method == "POST":
		uf = UserForm(request.POST)
		if uf.is_valid():
		#获取表单信息
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			email = uf.cleaned_data['email']
			#将表单写入数据库
			user = User()
			user.username = username
			user.password = password
			user.email = email
			user.save()
			 #返回注册成功页面
			return render(request, 'success.html', {'username':username})
	else:
		uf = UserForm()
		return render(request, 'register.html', {'uf':uf})
	#return render(request, 'register.html')