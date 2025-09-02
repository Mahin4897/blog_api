from django.contrib import admin
from .models import Post, Catagory, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Catagory)
admin.site.register(Tag)
