from django.contrib import admin
from posts.models import Post, Image

# Register your models here.
class ImageInLine(admin.StackedInline):
    model = Image
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]


admin.site.register(Post, PostAdmin)