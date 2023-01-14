from django.db import models


class Hero(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "남성")
        FEMALE = ("female", "여성")
        UNKNOWN = ("unknown", "알수없음")

    class TypeChoices(models.TextChoices):
        COMBAT = ("combat", "컴뱃")
        SPEED = ("speed", "스피드")
        BLAST = ("blast", "블래스트")
        UNIVERSAL = ("universal", "유니버설")

    class RaceChoices(models.TextChoices):
        HUMAN = ("human", "인간")
        INHUMAN = ("inhuman", "인휴먼")
        MUTANT = ("mutant", "뮤턴트")
        ALIEN = ("alien", "외계인")
        UNKNOWN = ("unknown", "알수없음")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "한국어")
        EN = ("en", "English")

    index = models.PositiveSmallIntegerField()
    charIndex = models.PositiveSmallIntegerField(default=1)
    latestUniform = models.BooleanField(default=False)
    uniformName = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=140)
    type = models.CharField(max_length=20, choices=TypeChoices.choices)
    description = models.TextField()
    profileImage = models.ImageField(null=True)
    gender = models.CharField(max_length=20, choices=GenderChoices.choices, blank=True)
    race = models.CharField(max_length=20, choices=RaceChoices.choices, blank=True)
    language = models.CharField(
        max_length=10, choices=LanguageChoices.choices, blank=True
    )

    def __str__(self):
        return f"{self.name}:{self.uniformName}"
