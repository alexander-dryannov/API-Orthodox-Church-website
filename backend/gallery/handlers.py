from PIL import Image
from io import BytesIO
from uuid import uuid4
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile


def get_new_size(size: int) -> int:
    if size >= 600:
        return int(round(size / 1000))
    else:
        return 1


def convert_image(image=None, fmt=settings.CONVERTING_SAVED_IMAGE,
                  field_name='image'):
    rgb_image = Image.open(image).convert('RGB')
    w, h = rgb_image.size
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
    ), get_new_size(w), get_new_size(h), w, h
