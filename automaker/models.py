from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Master(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    certification = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100)

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)


class PhotoReport(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    before_photo = models.ImageField(upload_to='before_photos/')
    after_photo = models.ImageField(upload_to='after_photos/')