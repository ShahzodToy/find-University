from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = 'image', 'Image'
        VIDEO = 'video', 'Video'

    file = models.FileField(upload_to='univer_media/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'doc', 'pdf'])
    ])
    type = models.CharField(max_length=120, choices=MediaType.choices)

    def __str__(self):
        return str(self.id) + " " + str(self.file.name.split("/")[-1])
    
    def clean(self):
        if self.type == self.MediaType.IMAGE:
            if not self.file.name.endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError("File type is not image")
        if self.type == self.MediaType.VIDEO:
            if not self.file.name.endswith(['mp4']):
                raise ValidationError('File is not video type')
                 
