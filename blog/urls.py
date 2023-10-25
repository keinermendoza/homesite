from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='blog/homepage.html'), name='home'),
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('certificates/', views.certificate_list, name='certificate_list'),
    path('blog/', views.post_list, name='post_list'),

]
