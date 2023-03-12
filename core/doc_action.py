import datetime
from core.exception import ClientException
from modules.tags.models import Tag
from modules.document.models import Document, DocumentType
from django.conf import settings


def get_document(doc_id: int) -> Document:
    """ Получить документ по id

    :param doc_id: id документа
    :return: Инстанс Document
    """
    return Document.objects.get(id=doc_id)


def register_tags(tags: list[str], max_tags: int | None = None) -> list:
    """ Регистрация тегов

    :param max_tags: Максимальное количество тегов
    :param tags: Список строк (тегов)
    :return: Список моделей тегов
    """
    added_tags = []
    cnt_tags = len(tags)
    if cnt_tags > settings.MAX_TAGS_PER_ENTITY or (max_tags is not None and cnt_tags > max_tags):
        raise ClientException("Максимальное число тегов для одной записи: 10")
    for tag in tags:
        added_tags.append(Tag.objects.get_or_create(name=tag)[0])
    return added_tags


def register_document(doc_type: str, data: dict, create_by: int, tags: list = None) -> Document:
    """ Регистрация документа в базе данных

    :param doc_type: Тип документа по DocumentType
    :param data: Дата из validated_data в формате dict
    :param create_by: ID инициатора создания документа
    :param tags: Список строк тегов (["Тег1", "Тег2"])
    :return: Инстанс Document
    """
    doc_type_model = DocumentType.objects.get(doc_type=doc_type)
    if not doc_type_model.is_active_type:
        raise ClientException("Данный тип документа выведен из оборота")
    if data.get("user"):
        data.pop("user")
    doc = Document.objects.create(doc_type_id=doc_type, json_data=data, create_by_id=create_by)
    if doc_type_model.is_accept_for_tags and tags is not None:
        registered_tags = register_tags(tags)
        doc.tags.set(registered_tags)
    if doc.doc_type.is_need_approve:
        doc.is_ready_for_publish = False
        doc.is_moderated = False
    doc.save()
    return doc


def update_document(doc: Document, data: dict, update_by: int, tags: list = None) -> Document:
    """ Обновление зарегестрированного документа

    :param doc: Инстанс Document
    :param data: Дата из validated_data в формате dict
    :param update_by: ID инициатора обновления документа
    :param tags: Список строк тегов (["Тег1", "Тег2"])
    :return: Инстанс Document
    """
    if not doc.doc_type.is_active_type:
        raise ClientException("Данный тип документа выведен из оборота")
    doc.update_by_id = update_by
    doc.json_data = data
    doc.update_at = datetime.datetime.now()
    if data.get("user"):
        data.pop("user")
    if doc.doc_type.is_accept_for_tags and tags is not None:
        registered_tags = register_tags(tags)
        doc.tags.set(registered_tags)
    if doc.doc_type.is_need_approve:
        doc.is_ready_for_publish = False
        doc.is_moderated = False
    doc.save()
    return doc


