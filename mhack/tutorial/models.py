from django.db import models

class Test(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']
