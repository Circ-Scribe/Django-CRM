from django.db import models

# Create your models here., these are the database models, let us do the migrations.
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
#the next shows what one is to get if we get to call any of the above, in our case, it would be best if we just called the first and the last name.
    def __str__(self):
        return (f"First Name: {self.first_name}"
                f"Last Name: {self.last_name}")
