from django.db import models
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import AbstractUser


class User(TimeStampedModel, AbstractUser):
    pass


class Poem(TimeStampedModel):
    owner = models.ForeignKey('User', null=True, related_name="poems")
    title = models.CharField(max_length=256)


    @property
    def collaborators(self):
        return User.objects.filter(poem_lines__in=self.lines.all())


class PoemLine(TimeStampedModel):
    poem = models.ForeignKey('Poem', null=True, related_name="lines")
    author = models.ForeignKey('User', null=True, related_name="poem_lines")
    text = models.CharField(max_length=512)
