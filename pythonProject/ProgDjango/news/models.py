from django.db import models
import os


class Articales(models.Model):
    @staticmethod
    def file_path(self, filename):
        media_path = 'articles/'
        ext = filename.split('.')[-1]
        new_filename = f'{self.title}.{ext}'
        full_path = os.path.join(media_path, new_filename)
        return full_path

    title = models.CharField('название', max_length=50)
    anons = models.CharField('анонс', max_length=250)
    text = models.TextField('статья')
    time = models.DateTimeField('время публикации')
    picture = models.FileField(upload_to=file_path.__func__, null=True)

    def str(self):
        return self.title

