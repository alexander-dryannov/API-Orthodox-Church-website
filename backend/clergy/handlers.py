import json
import shutil
import zipfile
from PIL import Image
from io import BytesIO
from uuid import uuid4
from pathlib import Path
from docx import Document
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


def get_data(docx_file):
    data = {}
    document = Document(docx_file)
    for row in document.tables[0].rows:
        header, body = row.cells
        if header.text == 'Награды':
            data.update(
                {header.text: [text.strip() for text in body.text.split(',')]}
            )
        else:
            data.update({header.text: body.text})
    return json.dumps(data, ensure_ascii=False, indent=2)


def get_image(docx_file):
    archive = zipfile.ZipFile(docx_file)
    for item in archive.filelist:
        if not item.filename.startswith('word/media'):
            continue
        else:
            archive.extract(item)
            break
    if Path('word/media').exists():
        image = converter(Path('word/media').glob('*').__next__())
        shutil.rmtree('word')
        return image
    else:
        return None


def get_cleric_data(docx_file):
    data = get_data(docx_file)
    image, *_ = get_image(docx_file)
    return data, image
