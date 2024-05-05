from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from PIL import Image
import os


def validate_image_dimensions(image):
    if image.width != 600 or image.height != 800:
        raise ValidationError("Image dimensions must be exactly 600 x 800 pixels.")


def validate_pdf_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = [".pdf"]  # List of valid extensions

    if not ext.lower() in valid_extensions:
        raise ValidationError("Please upload a PDF file. ")


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to="your_upload_path", validators=[validate_image_dimensions]
    )
    description = models.CharField(max_length=100)  # Optional description
    sub_title = models.CharField(max_length=200, null=True, default=None)
    time_spent = models.CharField(max_length=100, default=None)
    Brochure = models.FileField(
        upload_to="your_upload_path",
        validators=[validate_pdf_extension],
        null=True,
        default=None,
    )
    About = models.TextField(null=True)
    Visit = models.TextField(null=True)
    Tours = models.TextField(null=True)
    Programs = models.TextField(null=True)
    Image_bk_1 = models.ImageField(
        upload_to="your_upload_path",
    )
    Image_bk_2 = models.ImageField(
        upload_to="your_upload_path",
    )
    Image_bk_3 = models.ImageField(
        upload_to="your_upload_path",
    )
    is_active = models.BooleanField(default=True)  # Control item visibility
    id = models.AutoField(primary_key=True)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
