from django.shortcuts import render

def home(request):
    links = [
        {
            "label": "Home",
            "url": "#home",
        },
        {
            "label": "Projects",
            "url": "#projects",
        },
        {
            "label": "Courses",
            "url": "#courses",
        },
        {
            "label": "FAQ",
            "url": "#faq",
        },
        {
            "label": "Blog",
            "url": "#blog",
        },
    ]

    return render(request, "blog/homepage.html", {"links": links})
