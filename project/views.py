from django.shortcuts import render

def home(request):
    tempelate_name = "index.html"
    content = {"name":"noor"}
    return render(request,tempelate_name,content)