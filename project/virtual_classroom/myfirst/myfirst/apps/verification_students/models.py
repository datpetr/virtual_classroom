from django.db import models


class Verification(models.Model):
    verification_title = models.CharField('название статьи', max_length=200)
    verification_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')


class Comment(models.Model):
    verification = models.ForeignKey(Verification, on_delete=models.CASCADE())
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)
