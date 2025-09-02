from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    media = models.FileField(upload_to="media/", null=True, blank=True)
    catagory = models.ManyToManyField("Catagory", related_name="posts", blank=True)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def delete_old_file_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_file = Post.objects.get(pk=instance.pk).image
        old_file_media = Post.objects.get(pk=instance.pk).media
    except Post.DoesNotExist:
        return
    if old_file and old_file != instance.image:
        old_file.delete(save=False)
    if old_file_media and old_file_media != instance.media:
        old_file_media.delete(save=False)


@receiver(post_delete, sender=Post)
def delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

    if instance.media:
        instance.media.delete(save=False)


class Catagory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"
