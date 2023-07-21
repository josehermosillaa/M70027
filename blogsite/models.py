from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    # pk = models.AutoField(primary_key=True) -> 1, 2, 3, 4
    title = models.CharField(max_length=254, verbose_name="Titulo")
    slug = models.SlugField(unique=True,blank=True, null=True,max_length=255)
    content = models.TextField(verbose_name="Contenido")
    author = models.TextField(verbose_name="autor")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog_post_detail", args=[self.slug])
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return self.title
    