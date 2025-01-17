from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    categoryName=(
        ('HTML','HTML'),
        ('CSS','CSS'),
        ('Javascript','Javascript'),
        ('Angular','Angular'),
        ('Flask','Flask'),
        ('Django','Django'),
        ('Java','Java'),
        ('Android','Android'),
    )
    category=models.CharField(max_length=10,choices=categoryName)
    # count=.count(category)

    def __str__(self):
        return self.category

class Question(models.Model):
    user=models.ForeignKey(User)
    title=models.CharField(max_length=10)
    content=models.TextField(blank=True)
    snippet=models.ImageField(upload_to='question/',blank=True)
    category=models.ForeignKey(Category)

    def __str__(self):
        return self.title
  

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/')
    email=models.EmailField(blank=True)

    def __str__(self):
        return self.user.username

class Answer(models.Model):
    user=models.ForeignKey(Profile)
    question=models.ForeignKey(Question)
    answer=models.TextField()
    

    def __str__(self):
        return self.answer

class Approved(models.Model):
    name=models.OneToOneField(Profile,on_delete=models.CASCADE)
    answer=models.OneToOneField(Answer)
    approve=models.BooleanField()
    score=models.IntegerField()

    def __str__(self):
        return self.name.user.username

class Vote(models.Model):
    name=models.ForeignKey(Profile,on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    vote=models.IntegerField()


    def __str__(self):
        return self.name.user.username

class Invitation(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()



