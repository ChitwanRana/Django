from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Chaivarity(models.Model):
     VARIETY=[('ML','Machine Learning'),
              ('DL','Deep Learning'),
              ('NLP','Natural Language Processing'),
              
              ]
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to='chais/')
     date=models.DateTimeField(default=timezone.now)
     type=models.CharField(max_length=3,choices=VARIETY)
     desc=models.TextField(default='')
     
     def __str__(self):
          return self.name

#Types Of Relations 

#One to Many (For One to many we use Foreign Key)
class ChaiReview(models.Model):
     chai=models.ForeignKey(Chaivarity,on_delete=models.CASCADE,related_name='reviews')
     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
     rating=models.IntegerField()
     comment=models.TextField()
     date_added=models.DateTimeField(default=timezone.now)

     def __str__(self):
          return f'{self.user.username} and review for {self.chai.name}'
     
# Many to Many (for many to many we use ManyToManyField )
class store(models.Model):
     name=models.CharField(max_length=50)
     location=models.CharField(max_length=100)
     chai_varieties=models.ManyToManyField(Chaivarity,related_name='store')

     def __str__(self):
          return f'{self.name } is store name at location {self.location}'
     
# One to One(for Oen to One we use OneToOneField )

class ChaiCertificate(models.Model):
     chai=models.OneToOneField(Chaivarity,on_delete=models.CASCADE,related_name='certificate')
     certificate_number=models.CharField(max_length=100)
     issued_date=models.DateTimeField(default=timezone.now)
     valid_until=models.DateTimeField()

     def __str__(self):
          return f'Certtificate earned by {self.name.chai}'




 