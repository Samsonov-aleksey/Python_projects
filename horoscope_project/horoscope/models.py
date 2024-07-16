from django.db import models
from datetime import datetime
# Create your models here.

class Elem(models.Model):
    FIR = 'FIR'
    EAR = 'EAR'
    AIR = 'AIR'
    WAT = 'WAT'
    ELEM_CHOICES = [
        (FIR, 'Fire'),
        (EAR, 'Earth'),
        (AIR, 'Air'),
        (WAT, 'Water'),
    ]
    title = models.CharField(max_length=4, choices=ELEM_CHOICES, default=FIR)
    description = models.TextField()
    image = models.FileField(upload_to = 'horoscope', null = True)

    def __str__(self):
        return self.get_title_display()

class Horoscope(models.Model):
    ARI = 'ARI'
    LEO = 'LEO'
    SAG = 'SAG'
    TAU = 'TAU'
    VIR = 'VIR'
    CAP = 'CAP'
    GEM = 'GEM'
    LIB = 'LIB'
    AQU = 'AQU'
    CAN = 'CAN'
    SCO = 'SCO'
    PIS = 'PIS'
    HOROSCOPE_CHOICES = [
        (ARI, 'Aries'),
        (LEO, 'Leo'),
        (SAG, 'Sagittarius'),
        (TAU, 'Taurus'),
        (VIR, 'Virgo'),
        (CAP, 'Capricorn'),
        (GEM, 'Gemini'),
        (LIB, 'Libra'),
        (AQU, 'Aquarius'),
        (CAN, 'Cancer'),
        (SCO, 'Scorpio'),
        (PIS, 'Pisces'),
    ]
    title = models.CharField(max_length=12, choices=HOROSCOPE_CHOICES, default = ARI )
    elem = models.ForeignKey(Elem, on_delete=models.PROTECT, null = True)
    begin_date = models.IntegerField(null = True)
    end_date = models.IntegerField(null = True)
    description = models.TextField(null = True)
    image = models.FileField(upload_to = 'horoscope', null = True)

    def __str__(self):
        return self.get_title_display()

    def get_begin_date(self):
        date_obj_begin = datetime.strptime(f'{self.begin_date}', '%j').replace(year = datetime.now().year)
        return date_obj_begin

    def get_end_date(self):
        date_obj_end = datetime.strptime(f'{self.end_date}', '%j').replace(year = datetime.now().year)
        return date_obj_end










