from django.db import models


# Create your models here.
class Parent(models.Model):
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length = 255)
    parent_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.father_name} {self.mother_name}"


class Child(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Blog(models.Model):
   title = models.CharField(max_length=255)
   content = models.TextField()
   age_group = models.CharField(max_length=20)
   gender = models.CharField(max_length=20)
   parent_type = models.CharField(max_length=255)

   def __str__(self):
       return self.title