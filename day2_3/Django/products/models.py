from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=60) #이름
  location = models.CharField(max_length=60) #위치
  active = models.BooleanField(default=True) #활동
  
  def __str__(self):
      return self.name

class Book(models.Model): # Book Product
  author = models.ForeignKey(Author, 
                             on_delete=models.CASCADE, # CASCADE : 연결되 요소가 삭제되면 같이 삭제됨
                             related_name="books")
  name = models.CharField(max_length=80)
  description = models.CharField(max_length=120)
  price = models.IntegerField()
  shipping_price = models.IntegerField()
  quantity = models.PositiveIntegerField()
  
  def __str__(self):
      return f'{self.name} by {self.author.name}' 
  