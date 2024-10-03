from django.db import models
from django.utils import timezone


class Chaivarity(models.Model):
     VARIETY=[('ML','Machine Learning'),
              ('DL','Deep Learning'),
              ('NLP','Natural Language Processing'),
              
              ]
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to='chais/')
     date=models.DateTimeField(default=timezone.now)
     type=models.CharField(max_length=3,choices=VARIETY)
     
     def __str__(self):
          return self.name
 