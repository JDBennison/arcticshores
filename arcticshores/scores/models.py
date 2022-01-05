from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


# Candidate model for storing the name and reference number.
class Candidate(models.Model):
    name = models.CharField(max_length=200, null=True)
    candidate_ref = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(
            regex='^\w{8}$',
            message='Candidate Reference must be 8 alphanumeric characters.',
            code='invalid'
        )]
    )

    def __str__(self):
        return str(self.name)


# Scores model must be able to store multiple scores per candidate.
class Scores(models.Model):
    candidate_id = models.ForeignKey(
        Candidate,
        related_name='scores',
        on_delete=models.CASCADE
    )
    score = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
    )

    class Meta:
        ordering = ['score']

    def __str__(self):
        return str(self.score)
