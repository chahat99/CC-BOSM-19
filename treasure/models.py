from django.db import models
import uuid
import random
from django.contrib.auth.models import User


def generatecode():
    return random.randint(1000, 9999)


class Question(models.Model):
    # unique_id = models.UUIDField("Question UUID", primary_key=True,
    #                              default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=500)
    myid = models.IntegerField(blank=False)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    times_answered = models.PositiveIntegerField(default=0)


class Team(models.Model):
    name = models.CharField(max_length=100)
    code = models.PositiveIntegerField(default=generatecode, blank=False, unique=True)
    state = models.PositiveIntegerField(default=1)
    participant_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name+' team'


class Participant(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    unique_id = models.UUIDField("Participant UUID", primary_key=True,
                                 default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=100, blank=False)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
