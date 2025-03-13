from django.db import models

class Admin_Details(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Admin_Details'  

class User_Details(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Dob = models.CharField(max_length=50,default=None)
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField(default=None)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
      
    class Meta:
        db_table = 'User_Details'


class Missing_Complaint(models.Model):
    Uid = models.CharField(max_length=50)
    FullName = models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)
    Email = models.CharField(max_length=50,default=None)
    Address = models.CharField(max_length=10)
    City = models.CharField(max_length=100)
    State = models.EmailField()
    Country = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=100)
    MissingDetails = models.CharField(max_length=100)
    Photo = models.ImageField(upload_to='img/images/ComplaintImages')
    Status = models.CharField(max_length=100,default=None)
    DateofComplaint = models.DateField(default=None)

    class Meta:
        db_table = 'Missing_Complaint'



class Complaints(models.Model):
    Userid = models.CharField(max_length=50)
    FullName = models.CharField(max_length=100)
    Contact = models.CharField(max_length=50)
    Email = models.CharField(max_length=50,default=None)
    Address = models.CharField(max_length=500)
    City = models.CharField(max_length=100)
    State = models.EmailField()
    Country = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=100)
    Complaint = models.CharField(max_length=100)
    ComplaintType = models.CharField(max_length=100)
    Status = models.CharField(max_length=100,default=None)
    DateofComplaint = models.DateField(default=None)
    
    class Meta:
        db_table = 'Complaints'


