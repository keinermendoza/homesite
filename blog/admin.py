from django.contrib import admin
from .models import Project, Certificate, Tecnology

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'release', 'importance']
    readonly_fields=('slug', )
    filter_horizontal = ['tecnologies']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'importance', 'exercises', 'project']
    readonly_fields=('slug', )
    filter_horizontal = ['topics']

admin.site.register(Tecnology)




    