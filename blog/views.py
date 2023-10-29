from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Certificate, Project

links = [
    {
        "label": "Home",
        "url": "#home",
    },
    {
        "label": "About",
        "url": "#about",
    },
    {
        "label": "Projects",
        "url": "#projects",
    },
    {
        "label": "Certificates",
        "url": "#certificates",
    },
    {
        "label": "Contact",
        "url": "#contact",
    },
]

posts = [
    {
        'id':1,
        'title': 'saliendo para la casa',
        'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil omnis vitae blanditiis et eius nulla, ut dolorum.',
    },
]

def home(request):

    certificates = Certificate.objects.all()[:2]
    projects = Project.objects.all()[:4]

    return render(
        request,
        "blog/homepage.html",
        {
            "links": links,
            "projects": projects,
            "certificates": certificates,
            'current':'homepage'
        },
    )

def project_list(request):
    projects = Project.objects.all()

    return render(
        request,
        'blog/projects/project_list.html',
        {
            "projects": projects,
            'current':'projects'
        }
    )

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
   
    return render(
        request,
        'blog/projects/project_detail.html',
        {
            "project": project,
            'current':'projects',
            'detail':project.title,
        }
    )

def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(
        request,
        'blog/certificates/certificate_list.html',
        {
            "certificates": certificates,
            'current':'certificates'
        }
    )

def certificate_detail(request, slug):
    certificate = get_object_or_404(Certificate, slug=slug)
    return render(
        request,
        'blog/certificates/certificate_detail.html',
        {
            "certificate": certificate,
            'current':'certificates',
            'detail':certificate.title,
        }
    )


def post_list(request):
    return render(
        request,
        'blog/blog/post_list.html',
        {
            "posts": posts,
            'current':'blog'
        }
    )