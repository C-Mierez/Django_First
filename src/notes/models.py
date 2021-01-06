from django.db import models

class Note(models.Model):
    title           = models.CharField(max_length=60, null=False)
    content         = models.TextField()
    is_Completed    = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
