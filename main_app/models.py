from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Complaint(models.Model):

    completed = "completed"
    under_process = "under process"
    issue_received = "issue received"

    classroom = "classroom"
    laboratories = "laboratories"
    restrooms = "restrooms"
    library = "library"
    common_areas = "common areas"
    cafeteria = "cafeteria"
    outdoor = "outdoor"
    transport = "transport"
    halls = "halls"

    status_choices = [
        (completed, "completed"),
        (under_process, "under process"), (issue_received, "issue received")
    ]

    category_choices = [(classroom, "classroom"),
                        (laboratories, "laboratories"),
                        (restrooms, "restrooms"),
                        (library, "library"),
                        (common_areas, "common areas"),
                        (cafeteria, "cafeteria"),
                        (outdoor, "outdoor"),
                        (transport, "transport"),
                        (halls, "halls")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    category=models.CharField(choices=category_choices)
    description = models.TextField()
    images=models.ImageField(upload_to="complaint_images/",blank=True,)
    date_created=models.DateField(editable=True)
    status = models.CharField(choices=status_choices, default=issue_received)

    def __str__(self):
        return self.title
