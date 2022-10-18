from django.shortcuts import render

# Create your views here.
def model(request):
    
    return render(request, 'kalkulator/index.html')

