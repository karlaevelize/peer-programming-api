from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# Create your models here.
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    avatar_url = models.CharField(max_length=150, default='https://uploads-ssl.webflow.com/6198a2e43048192ebafec2cc/63d221403d9cfe4ced015d95_yxRQH9s6VEU6gldnFhl3PDigUW31MIHSSqavg8i9s24.png')

    class Meta:
        ordering = ['created']

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_url = models.CharField(max_length=15, default='https://uploads-ssl.webflow.com/6198a2e43048192ebafec2cc/63d221403d9cfe4ced015d95_yxRQH9s6VEU6gldnFhl3PDigUW31MIHSSqavg8i9s24.png')

    class Meta:
        ordering = ['created']
