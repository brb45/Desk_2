# 1.  admin.py
from django.contrib import admin
from .models import Post

# admin.site.register(Post)
class  PostAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields=('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_hierarchy='publish'
    ordering=['status', 'publish']

admin.site.register(Post, PostAdmin)
# python manage.py createsuperuser
# localhost:8000/admin
#2. models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES  = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering=('-publish', ) # sort in descending order
        # specify descending order using the negative prefix
    def __str__(self):
        return self.title


# Slug: this is a field intended to be used in URLs. A slug is a short label containing only letters,
# numbers underscores or hyphens. We will use the slug field to build beautiful SCO-friendly URLs
# for our blog posts. We have added the unique for_date parameter to this field, so we can build URLs
# for posts using the date and slug of the post. Django will prevent multiple posts having the same slugs
# for the same date

class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments')
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('created')

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

# forms
from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email=forms.EmailField()
    to= forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

























