from django.db import models
from apps.util.models import AbstractBaseModel


class Category(AbstractBaseModel):

    name = models.CharField(max_length=256)

    description = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"




class MenuItem(AbstractBaseModel):

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='menu_items'
    )

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='menu_items/',
        blank=True,
        null=True
    )

    is_available = models.BooleanField(default=True)

    is_vegetarian = models.BooleanField(default=False)

    preparation_time = models.PositiveIntegerField(default=15)
