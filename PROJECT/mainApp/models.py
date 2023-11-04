from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Audio(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    duration = models.DurationField()
    size = models.FloatField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name