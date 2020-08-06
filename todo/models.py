from django.db import models

class todo(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    create_date = models. DateField(auto_now=False)
    completion_date = models. DateField(auto_now=False)
    last_modified = models. DateField(auto_now=True)
    important_flag = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

