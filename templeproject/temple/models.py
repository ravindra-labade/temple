from django.db import models


class Temple(models.Model):
    temple_name = models.CharField(max_length=20)
    famous_for = models.CharField(max_length=20)
    temple_address = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    devotees_per_day = models.IntegerField()
    choice = [('Online', 'ONLINE'), ('Cash', 'Cash')]
    donation_mode = models.CharField(max_length=10, choices=choice)

