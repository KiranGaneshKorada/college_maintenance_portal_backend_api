from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Issue(models.Model):

    completed="completed"
    under_process="under process"
    issue_received="issue received"

    status_choices = [
        (completed, "completed"),
        (under_process, "under process"),(issue_received,"issue received")
        ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=75)
    description=models.TextField()
    status=models.CharField(choices=status_choices,default=issue_received)
    

    def __str__(self) :
        return self.title
