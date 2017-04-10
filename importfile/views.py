from django.shortcuts import render

# Create your views here.
def importfile(request):
	return render(request, 'importPage.html')