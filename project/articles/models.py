from django.db import models


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    text = models.TextField('Текст статьи')

    def __str__(self):
        return f'{self.title[:32]} - {self.text[:32]}'
