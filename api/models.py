from django.db import models

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator,MaxValueValidator


class Album(models.Model):

    title = models.CharField(max_length=200)

    year = models.PositiveIntegerField

    director = models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    @property
    def track_count(self):

        return Tracks.objects.filter(album=self).count()

    @property
    def tracks(self):

        return Tracks.objects.filter(album=self)
    
    @property
    def reviews(self):

        return Review.objects.filter(album=self)

    def __str__(self) -> str:

        return self.title


class Tracks(models.Model):

    title = models.CharField(max_length=200)

    singers = models.CharField(max_length=200)

    options = (
        ("pop","pop"),
        ("jazz","jazz"),
        ("melody","melody"),
        ("hip hop","hip hop"),
        ("others","others")
    )

    genre = models.CharField(max_length=200,choices=options,default="others")

    duration = models.DurationField()

    track_num = models.PositiveIntegerField()

    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:

        return self.title
    

class Review(models.Model):

    comment = models.CharField(max_length=200)

    rating = models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)