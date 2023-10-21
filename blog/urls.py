from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='blog/homepage.html'), name='home'),
    path('', views.home, name='home'),
]
