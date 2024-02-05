# blog/admin.py

from django.contrib import admin

from .models import Post

# Register your models here.
admin.site.register(Post)

# this will make the Post Model show up in the admin page