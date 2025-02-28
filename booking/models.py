from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

TIMES = (
    (12, '12:00 - 13:00'),
    (13, '13:00 - 14:00'),
    (14, '14:00 - 15:00'),
    (15, '15:00 - 16:00'),
    (16, '16:00 - 17:00'),
    (17, '17:00 - 18:00'),
    (18, '18:00 - 19:00'),
    (19, '19:00 - 20:00'),
    (20, '20:00 - 21:00'),
    (21, '21:00 - 22:00'),
    (22, '22:00 - 23:00'),
)


class Allergen(models.Model):
    """
    Stores a single allergen.
    """
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Stores a single booking request.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user"
    )
    date = models.DateField()
    time_slot = models.IntegerField(choices=TIMES)
    guests = models.PositiveIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(12)
        ])
    allergies = models.ManyToManyField(Allergen, blank=True)
    booking_notes = models.TextField(blank=True)

    class Meta:
        ordering = ["date"]

    @property
    def name(self):
        return self.user.first_name

    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return f"Booking for {self.name} on {self.date}"

    def clean(self):
        """
        Custom validation to ensure the date is not in the past.
        """
        if not self.date:
            raise ValidationError("This field is required.")

        if self.date < timezone.now().date():
            raise ValidationError("The booking date cannot be in the past.")
