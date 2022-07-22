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


def converter(image=None, fmt=settings.CONVERTING_SAVED_IMAGE):
    rgb_image = Image.open(image).convert('RGB')
    origin_width, origin_height = rgb_image.size
    width = get_new_size(origin_width)
    height = get_new_size(origin_height)
    binary_image = BytesIO()
    rgb_image.save(binary_image, fmt)
    image_name = f'{uuid4().hex}.{fmt}'
    binary_image.seek(0)
    return InMemoryUploadedFile(
        file=binary_image,
        field_name='ImageField',
        name=image_name,
        content_type=f'image/{fmt}',
        size=rgb_image.size,
        charset=None
    ), width, height, origin_width, origin_height
