from django.db import models
from django.utils.timezone import now


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


class Voter(models.Model):
    id = models.AutoField(primary_key=True)

    photo = models.ImageField()
    name = models.CharField(max_length=100, default='')
    sno = models.CharField(max_length=18, default=0)

    date_of_birth = models.DateField(default=now)
    date_of_death = models.DateField(default=now, null=True, blank=True)
    gender = models.CharField(choices=GENDER, default='Male', max_length=10)

    father_name = models.CharField(max_length=100, default='')
    mother_name = models.CharField(max_length=100, default='')

    # Address = models.TextField(max_length=200, default='')
    present_holding_no = models.CharField(max_length=10, default='')
    present_city = models.CharField(max_length=50, default='')
    present_area_code = models.CharField(max_length=10, default=0)
    present_country = models.CharField(max_length=100, default='Bangladesh')

    permanent_holding_no = models.CharField(max_length=10, default='')
    permanent_city = models.CharField(max_length=50, default='')
    permanent_area_code = models.CharField(max_length=10, default=0)
    permanent_country = models.CharField(max_length=100, default='Bangladesh')

    date = models.DateTimeField(default=now)
