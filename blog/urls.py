from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView

# for include media 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', TemplateView.as_view(template_name='blog/homepage.html'), name='home'),
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>', views.project_detail, name='project_detail'),

    path('certificates/', views.certificate_list, name='certificate_list'),
    path('certificates/<slug:slug>', views.certificate_detail, name='certificate_detail'),

    # path('blog/', views.post_list, name='post_list'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
