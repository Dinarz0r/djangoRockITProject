import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    STATUS_INACTIVE = 0
    STATUS_ACTIVE = 1
    STATUS_DRAFT = 2
    STATUSES = (
        (STATUS_INACTIVE, 'Неактивный'),
        (STATUS_ACTIVE, 'Опубликованный'),
        (STATUS_DRAFT, 'Черновик'),
    )
    hash = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    name = models.CharField('Наименование', max_length=255)
    content = models.TextField('Контент')
    published_at = models.DateTimeField('Дата публикации', db_index=True)
    status = models.SmallIntegerField('Статус', default=STATUS_DRAFT, choices=STATUSES)

    class Meta:
        ordering = ['id']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.name
