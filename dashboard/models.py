from django.db import models
from django.utils.timezone import now

# Create your models here.

BUYING = (
    ('3', 'v-high'),
    ('2', 'high'),
    ('1', 'med'),
    ('0','low'))

MAINT = (
    ('3', 'v-high'),
    ('2', 'high'),
    ('1', 'med'),
    ('0','low'))

DOORS = (
    ('3', '5-more'),
    ('2', '4'),
    ('1', '3'),
    ('0','2'))

PERSON = (
    ('2', 'more'),
    ('1', '4'),
    ('0','2'))

LUG_BOOT =(
    ('2', 'big'),
    ('1', 'med'),
    ('0', 'small')
)


SAFETY = (
    ('2', 'high'),
    ('1', 'med'),
    ('0', 'low')
)

class CarEvaluation(models.Model):
    buying = models.CharField(max_length=20, choices=BUYING, default='low')
    maint = models.CharField(max_length = 20, choices=MAINT, default='low')
    doors = models.CharField(max_length=20, choices=DOORS, default='2')
    persons = models.CharField(max_length=20, choices=PERSON, default='2')
    lug_boot = models.CharField(max_length=20, choices=LUG_BOOT, default='small')
    safety = models.CharField(max_length=20, choices=SAFETY, default='low')
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.predictions

    class Meta:
        pass
        ordering = ['-date']

   