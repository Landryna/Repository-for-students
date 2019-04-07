from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Article(models.Model):
 nazwa = models.CharField(max_length=30)
 slug = models.SlugField()
 komentarz = models.TextField(default = "-",max_length=70)
 date = models.DateTimeField(auto_now_add=True)
 grupa = models.PositiveIntegerField(default = 1)
 file = models.FileField(default = 'Żaden,załaduj go ponownie',blank=False)
 autor = models.ForeignKey(User,on_delete=models.CASCADE,default = None)
 ocena = models.CharField(max_length=1,default = "-")
 #ZROB OCENE, ALE NIE POOKAZUJ JEJ PRZY DODAWANIU PLIKU ocena = models.PositiveIntegerField(default = )
 def __str__(self):
  return self.nazwa
  
 def snippet(self):
   return self.komentarz[:20] 