from django.db import models


# Create your models here.


class season(models.Model):
    number = models.IntegerField()
    description = models.TextField(max_length=500, default='some text')

    def __str__(self):
        return '%s %s' % (self.number, " season")


class seriesRus(models.Model):
    obj = models.ForeignKey(season, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, default='name')
    nameEng = models.CharField(max_length=200, default='name')
    duration = models.CharField(max_length=50, default='30:25')
    season = models.IntegerField()
    number = models.IntegerField()
    description = models.TextField(max_length=1000, default='description')
    image = models.ImageField(upload_to='mirror/static/mirror/img/holder/', blank=True)
    video = models.CharField(max_length=500, default='static/')

    def save(self, *args, **kwargs):
        self.name = self.name.ljust(17)
        super(seriesRus, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.name, " ", self.season, " season ", self.number, "series")


class seriesEng(models.Model):
    obj = models.OneToOneField(seriesRus, blank=True)
    video = models.CharField(max_length=500, default='static/')
    subtitlesRus = models.ImageField(upload_to='documents/subtitlesRus', blank=True)
    subtitlesEng = models.ImageField(upload_to='documents/subtitlesEng', blank=True)
    description = models.TextField(max_length=1000, default='description', blank=True)

    def __str__(self):
        return self.name + " " + self.number + " series " + self.season + "season Eng"


class subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
