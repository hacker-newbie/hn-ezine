from django.db import models
from django.utils import timezone
from .validators import validate_file_extension

class Hnezine(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    e_zine = models.FileField(upload_to="txt/%Y/%m/%d", validators=[validate_file_extension])
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
