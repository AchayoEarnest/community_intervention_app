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
    ward = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    guadian_phone_number = models.CharField(max_length=12)
    school= models.CharField(max_length=100)
    landmark= models.CharField(max_length=100)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


class Intervention(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='interventions')
    intervention_name = models.CharField(max_length=100)
    intervention_cartegory = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    date_of_intervention = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.intervention_name} belonging to {self.enrollment.name}"