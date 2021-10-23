from functools import singledispatch
from typing import List

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet


def common_schema_decorator(tags: List[str]):
    """
    Декоратор позволяющий вносить и редактировать информацию в схеме SWAGER
    При использовании необходимо обернуть представление
    :param tags: аргумент позволяющий в Swager добавить заголовок класса
    """
    @singledispatch
    def wrapper(origin_class_type):
        return origin_class_type

    @wrapper.register(type(ViewSet))
    def _(origin_class_type):
        method_decorator(
            name='list',
            decorator=swagger_auto_schema(
                tags=tags, operation_summary='Список'
            ),
        )(origin_class_type)
        method_decorator(
            name='create',
            decorator=swagger_auto_schema(
                tags=tags, operation_summary='Создание'
            ),
        )(origin_class_type)
        method_decorator(
            name='retrieve',
            decorator=swagger_auto_schema(
                tags=tags, operation_summary='Получение'
            ),
        )(origin_class_type)
        method_decorator(
            name='update',
            decorator=swagger_auto_schema(
                tags=tags, operation_summary='Обновление', auto_schema=None
            ),
        )(origin_class_type)
        method_decorator(
            name='partial_update',
            decorator=swagger_auto_schema(
                tags=tags, operation_summary='Частичное обновление'
            ),
        )(origin_class_type)
        method_decorator(
            name='destroy',
            decorator=swagger_auto_schema(
                tags=tags, operation_summary='Удаление'
            ),
        )(origin_class_type)

        return origin_class_type

    return wrapper
