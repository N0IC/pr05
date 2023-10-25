from django.shortcuts import render

def page1_view(request):
    return render(request, 'page1.html')

def page2_view(request):
    return render(request, 'page2.html')

def page3_view(request):
    return render(request, 'page3.html')