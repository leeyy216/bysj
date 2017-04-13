from django.shortcuts import render

# Create your views here.
def datatable(request):
	return render(request, 'dataPage.html')