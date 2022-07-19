from io import BytesIO
from uuid import uuid4
from PIL import Image
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile


def convert_image(image=None, fmt=settings.CONVERTING_SAVED_IMAGE,
                  field_name='image'):
    rgb_image = Image.open(image).convert('RGB')
    width, height = rgb_image.size
    binary_image = BytesIO()
    rgb_image.save(binary_image, fmt)
    image_name = f'{uuid4().hex}.{fmt}'
    binary_image.seek(0)
    return InMemoryUploadedFile(
        file=binary_image,
        field_name=field_name,
        name=image_name,
        content_type=f'image/{fmt}',
        size=rgb_image.size,
        charset=None
    ), width, height
