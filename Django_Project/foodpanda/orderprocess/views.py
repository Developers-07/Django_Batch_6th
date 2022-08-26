from django.shortcuts import render

# Create your views here.

def mypage(request):
    return render(request, "homepage.html")

def about(request):
    return render(request, "about.html")

def main(request):
    return render(request, "main.html")