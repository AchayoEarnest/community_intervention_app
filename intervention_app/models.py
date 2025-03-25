from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

User = get_user_model()

phone_validator = RegexValidator(r'^\+?\d{10,12}$', 'Enter a valid phone number.')

class Enrollment(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_phone = models.CharField(max_length=12)
    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    guadian_phone_number = models.CharField(max_length=12)
    school= models.CharField(max_length=100)
    landmark= models.CharField(max_length=100)
    age= models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


