from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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


def home(request):
    certificates = Certificate.objects.all()
    projects = Project.objects.all()[:6]

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
            'current':{'title':'projects', 'url':reverse('project_list')},
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
            'current':{'title':'certificates', 'url':reverse('certificate_list')},
            'detail':certificate.title,
        }
    )


