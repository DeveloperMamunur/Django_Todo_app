from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_complete', '-created']