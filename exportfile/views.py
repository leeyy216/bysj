from django.shortcuts import render

# Create your views here.
def exportfile(request):
	return render(request, 'exportPage.html')