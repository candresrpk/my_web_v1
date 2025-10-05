from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


def index(request):
    skills = [
        {"name": "Python", "icon": "fa-brands fa-python", "color": "text-info"},
        {"name": "AWS", "icon": "fa-brands fa-aws", "color": "text-warning"},
        {"name": "SQL", "icon": "fa-solid fa-database", "color": "text-info"},
        {"name": "Excel", "icon": "fa-solid fa-file-excel", "color": "text-light"},
        {"name": "Linux", "icon": "fa-brands fa-linux", "color": "text-dark"},
        {"name": "Node.js", "icon": "fa-brands fa-node-js", "color": "text-dark"},
        {"name": "React", "icon": "fa-brands fa-react", "color": "text-info"},
    ]
    return render(request, 'carpena/index.html', {"skills": skills})
