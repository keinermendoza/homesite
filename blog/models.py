from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse_lazy

class Tecnology(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="certificates")
    exercises = models.IntegerField()
    project = models.IntegerField()
    src = models.URLField(blank=True, null=True)
    course = models.URLField(blank=True, null=True)

    importance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    topics = models.ManyToManyField(Tecnology, related_name="certificates")

    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy("certificate_detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Certificate, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['importance'])
        ]
        ordering = ['-importance']

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    mobile_image = models.ImageField(upload_to="projects", blank=True, null=True)

    youtube_id = models.CharField(max_length=100, blank=True, null=True)
    demo = models.TextField(blank=True, null=True)
    online = models.URLField(blank=True, null=True)
    code = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    release = models.DateField()
    tecnologies = models.ManyToManyField(Tecnology, related_name="projects")
    
    importance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    
    certificate = models.ForeignKey(Certificate,
                                    on_delete=models.DO_NOTHING,
                                    related_name="available_projects",
                                    null=True,
                                    blank=True)
    
    def get_absolute_url(self):
        return reverse_lazy("project_detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['-importance', '-release'])
        ]
        ordering = ['-importance', '-release']
