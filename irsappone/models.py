# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Import Django’s built-in User model
from django.core.validators import MinLengthValidator


class Incident(models.Model):
    # This is the ForeignKey - linking to the user/controller
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Dropdown choices
    # CALLSIGN_CHOICES = [
    #     ('DRK', 'DRK'),
    #     ('BTN', 'BTN'),
    # ]

    AIRCRAFT_TYPE_CHOICES = [
        ('ATR42', 'ATR42'),
        ('A319', 'A319'),
        ('A320neo', 'A320neo'),
    ]

    RUNWAY_CHOICES = [
        ('15', '15'),
        ('33', '33'),
    ]

    # OCCURRENCE_CHOICES = [
    #     ('Go Around', 'Go Around'),
    #     ('Miss Approach', 'Miss Approach'),
    #     ('Bird Strike', 'Bird Strike'),
    #     ('Technical Issue', 'Technical Issue'),
    # ]

    # Fields for data entry
    date = models.DateField()  # Date of the incident
    time = models.TimeField()  # Time of the incident
    call_sign = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)],
        help_text="Enter call sign (e.g., DRK, BTN)"
    )
    aircraft_type = models.CharField(max_length=20, choices=AIRCRAFT_TYPE_CHOICES)
    runway = models.CharField(max_length=3, choices=RUNWAY_CHOICES)
    occurrence = models.CharField(
        max_length=30,
        help_text="Describe the occurrence (e.g., Go Around, Bird Strike)"
    )
    operator = models.CharField(
        max_length=50,
        help_text="Enter operator name (e.g., Bhutan Airlines)",
     
    )
    place = models.CharField(
    max_length=50,
    help_text="Enter location/place of incident",
  
    )
    detail_report = models.TextField(null=True, blank=True)  # Long text area
    controller_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} | {self.call_sign} | {self.occurrence}"

    class Meta:
        ordering = ['-date', '-time']  # Newest incidents first


    