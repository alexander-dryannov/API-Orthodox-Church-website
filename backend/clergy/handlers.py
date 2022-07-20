import sys
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


def convert_image(image=None, fmt=settings.CONVERTING_SAVED_IMAGE,
                  field_name='image'):
    rgb_image = Image.open(image).convert('RGB')
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
    )


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
        image = convert_image(Path('word/media').glob('*').__next__())
        shutil.rmtree('word')
        return image
    else:
        return None


def get_cleric_data(docx_file):
    data = get_data(docx_file)
    image = get_image(docx_file)
    return data, image


if __name__ == '__main__':
    file = sys.argv[-1]
    get_cleric_data(file)
