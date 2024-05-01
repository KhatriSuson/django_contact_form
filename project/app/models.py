from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="default@gmail.com")
    subject = models.TextField()

    def __str__(self):
        return self.name


class Student_detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.TextField()
    state = models.TextField()

    def __str__(self):
        return str(self.name)


class About_Me(models.Model):
    title = models.CharField(max_length=50)
    dis = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.title)


class Stu_manage(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    dis = models.TextField()
    title = models.CharField(max_length=200)
    product_dis = models.TextField()

    def __str__(self):
        return str(self.title)
