from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)
    abilities = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    schools_taught = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.full_name


class Rating(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Rating for {self.teacher.full_name} by {self.customer.full_name}"