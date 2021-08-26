import json
import os

from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

from models import Card

formats = ['jpeg', 'png', 'gif', 'tiff', 'heif', 'hevc']
names = []


def load_full_names():
    with open('names.json', 'r', encoding='UTF-8') as source:
        global names
        names = json.loads(source.read())
        source.close()


def generate_remark(card: Card, name=None):
    load_full_names()
    doc = DocxTemplate('remark_template.docx')
    attachments = None
    if card.attachments:
        attachments = []
        for attachment in card.attachments:
            if str(attachment).split('.')[-1] in formats:
                attachments.append(
                    InlineImage(doc, image_descriptor=f'board/attachments/{attachment.lower()}', width=Mm(200),
                                height=Mm(100)))
    context = {'name': names.get(card.label) if names.get(card.label) else card.label, 'description': card.desc,
               "due_date": card.due,
               'attachments': attachments[0] if attachments else None}
    doc.render(context)
    doc.save(f'docs/{card.label}_{card.name}_{card.id}.docx')
