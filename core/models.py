from django.db import models

from django.core.exceptions import ValidationError

def validate_jpeg_file(value):
    # Check if the uploaded file is a JPEG
    if not value.name.lower().endswith('.jpeg'):
        raise ValidationError('Only .jpeg files are allowed.')

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

from django.db import models
from django.core.validators import FileExtensionValidator

class Article(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to="media/articles/",
        validators=[validate_jpeg_file]  # Add the validator here
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
