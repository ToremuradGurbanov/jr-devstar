from django.shortcuts import render
from . models import Project, Blog, Course

def homepage(request):
    project = Project.objects.all()
    blog = Blog.objects.all()
    course = Course.objects.all()
    context = {
        'projects': project,
        'blogs' : blog,
        'courses' :course
    }

    
    return render(request, 'main/home.html', context=context )
