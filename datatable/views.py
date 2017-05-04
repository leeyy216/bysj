from django.shortcuts import render
#from django.shortcuts import render_to_response
#0421
from datatable import forms
from datatable.forms import enrollForm
from datatable.models import enroll    #插入enroll表
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def datatable(request):
	return render(request, 'dataPage.html')

def table(request):
	table_form = forms.enrollForm()#forms.py中设置的样式
	students = enroll.objects.all()#models即数据库中的内容存到变量
	#return render(request,'table.html',{'form':table_form})
	return render_to_response("dataPage.html",locals()) #必须用这个return

# def enroll(request):
# 	form = None
# 	if request.method == 'POST':说
#         form = enorllForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             stu_info(
#                 cd['from_sch'],
#                 cd['message'],
#                 cd.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')#需要在urls.py中配置路径
#     else:
#         form = enorllForm()
#     return render_to_response('contact_form.html', {'form': form})

# def test1(request):
# 	#定义函数明

# 	seq_a = request.POST.get('seq_a', '').upper()
# 	#从浏览器端获取值，这里使用的是POST，表示不在浏览器地址中传值，避免由于值太大而影响功能，同时将序列转换为大写，为了方便统计。
# 	seq_c = request.POST.get('seq_c', '').upper()

# 	seq_count = 0
# 	#设置初始值
# 	seq_position = 0
# 	#设置初始值
# 	seq_positions = ''
# 	#设置初始值

# 	if seq_a and seq_c:
# 	#如果两个文本框中都有值则执行

# 		seq_count = seq_a.count( seq_c )
# 		#统计序列中key的个数

# 		seq_position = seq_a.find( seq_c )
# 		#统计位置

# 		while seq_position != -1:
# 		#由于find只返回第一个值，所以此循环进行位置的累加

# 			seq_positions += str(seq_position)+'|'

# 			seq_position = seq_a.find( seq_c, seq_position+1 )

# 			#注：这是为了顺利往下累加，如果不加，程序将进入死循环

# 	else:
# 	#如果条件不成立则为空值
# 		seq_a = ''
# 		seq_c = ''

# 	return render_to_response("test1.html",{'seq_a':seq_a, 'seq_c':seq_c, 'seq_count':seq_count, 'seq_positions':seq_positions}) 
# 	#返回的值，其中count_sequence.html为模板文件，后面的一个dictionary分别为返回的键值和此函数中真实的值，即’seq_a’表示模板中调用的名称，而seq_a则为此函数中的值，’seq_a’可以为其他名称，模板中调用正确即可。

	# def test2(request):
	# #定义函数明

	# seq_a = request.POST.get('seq_a', '').upper()
	# #从浏览器端获取值，这里使用的是POST，表示不在浏览器地址中传值，避免由于值太大而影响功能，同时将序列转换为大写，为了方便统计。
	# seq_c = request.POST.get('seq_c', '').upper()

	# seq_count = 0
	# #设置初始值
	# seq_position = 0
	# #设置初始值
	# seq_positions = ''
	# #设置初始值

	# if seq_a and seq_c:
	# #如果两个文本框中都有值则执行

	# 	seq_count = seq_a.count( seq_c )
	# 	#统计序列中key的个数

	# 	seq_position = seq_a.find( seq_c )
	# 	#统计位置

	# 	while seq_position != -1:
	# 	#由于find只返回第一个值，所以此循环进行位置的累加

	# 		seq_positions += str(seq_position)+'|'

	# 		seq_position = seq_a.find( seq_c, seq_position+1 )

	# 		#注：这是为了顺利往下累加，如果不加，程序将进入死循环

	# else:
	# #如果条件不成立则为空值
	# 	seq_a = ''
	# 	seq_c = ''

	# return render_to_response("test1.html",{'seq_a':seq_a, 'seq_c':seq_c, 'seq_count':seq_count, 'seq_positions':seq_positions}) 