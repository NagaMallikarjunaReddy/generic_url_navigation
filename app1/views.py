from django.shortcuts import render

# Create your views here.
def apache(request):
    return render(request,'Apache.html')