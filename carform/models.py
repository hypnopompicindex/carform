from __future__ import unicode_literals
from django.db import models


DURATION = (
    ('30DAYS' = 'Next 30 days'),
    ('3MONTHS' = 'Next 3-6 months'),
    ('6MONTHS' = 'Next 6-12 months'),
    ('UNDECIDED' = 'Undecided'),
)

PROVINCE = (
    ('AB' = 'AB'),
    ('BC' = 'BC'),
    ('MB' = 'MB'),
    ('NB' = 'NB'),
    ('NL' = 'NL'),
    ('NS' = 'NS'),
    ('ON' = 'ON'),
    ('PE' = 'PE'),
    ('QC' = 'QC'),
    ('SK' = 'SK'),
)

DEALER = (
    ('1' = 'Dealer 1'),
)

CONTACT = (
    ('PHONE' = 'Phone'),
    ('EMAIL' = 'Email')
)

class CarInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_brochure = models.EmailField()
    buy_or_lease = models.CharField(max_length=4, choices=DURATION)
    contact_by_dealer = models.BooleanField()
    province = models.CharField(max_length=4, choices=PROVINCE)
    dealer = models.CharField(max_length=4, choices=DEALER)
    contact_test_drive = models.CharField(max_length=4, choices=CONTACT)
    contact_phone = models.CharField(max_length=12)
    contact_email = models.EmailField()