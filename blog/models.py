from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.username


from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import UEditorEventHandler

class Blog(models.Model):
    Name = models.CharField(max_length = 100, blank = True)
    Content = UEditorField('内容	', width=600, height=300, toolbars="full", imagePath="uploads/images",
                           filePath="uploads/files",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None,  blank=True)


class Essay(models.Model):
    username = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=20)
    essay = models.TextField(max_length=4096)

    def __str__(self):
        return self.essay
