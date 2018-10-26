from django.db import models

#person
class person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    profile_picture=models.FileField()
    relative_number=models.IntegerField()

    def  __str__(self):
        return self.first_name+'-'+self.last_name


#area_affected
class areas_affected(models.Model):
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    street_number=models.IntegerField()
    photo=models.FileField()

    def __str__(self):
        return self.city+ ' street number ' + str(self.street_number) + ' pin code ' + str(self.pincode)


class address_search(models.Model):
    address= models.CharField(max_length=100)
    def __str__(self):
        return self.address

