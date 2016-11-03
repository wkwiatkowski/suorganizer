from django.db import models
from django.utils import timezone

from organizer.models import Startup, Tag

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=31,
        db_index=True)
    slug = models.SlugField(
        max_length=61,
        unique_for_month='pub_date',
        help_text="A label for URL config.")
    text = models.TextField()
    pub_date = models.DateField('date published',
            auto_now_add=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='blog_post')
    startups = models.ManyToManyField(
        Startup,
        related_name='blog_post')
    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))
    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

