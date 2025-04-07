from django.db import models
from core.base.models import CreatorModels, BaseModels
from django.db import models


class Person(CreatorModels):
    name = models.CharField(max_length=70)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("unknown", "Unknown"),
        ],
        default="unknown",
    )
    bio = models.TextField(blank=True, null=True)
    father = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children_father",
    )
    mother = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children_mother",
    )
    partners = models.ManyToManyField(
        "self", blank=True, related_name="partnerships", symmetrical=True
    )
    photo = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "People"


class Marriage(BaseModels):
    person1 = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="marriage1"
    )
    person2 = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="marriage2"
    )
    marriage_date = models.DateField(blank=True, null=True)
    divorce_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Marriages"