import sys
from docx import Document


def get_donation_data(docx_file):
    data = {}
    document = Document(docx_file)
    for row in document.tables[0].rows:
        header, body = row.cells
        data.update({header.text: body.text})
    return data


if __name__ == '__main__':
    file = sys.argv[-1]
    get_donation_data(file)