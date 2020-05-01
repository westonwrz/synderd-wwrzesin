from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    password = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField()
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zipcode = models.IntegerField()
    employername = models.CharField(max_length=64)

    def __str__(self):
        return self.username

class SubscriptionType(models.Model):
    subscriptiontypecode = models.IntegerField(primary_key=True)
    subscriptiontypename = models.CharField(max_length=64)

    def __str__(self):
        return self.subscriptiontypename

class Service(models.Model):
    servicecode = models.IntegerField(primary_key=True)
    servicename = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    premium = models.CharField(max_length=64)
    allocation = models.CharField(max_length=64)

    def __str__(self):
        return self.servicename

class Office(models.Model):
    officecode = models.IntegerField(primary_key=True)
    officename = models.CharField(max_length=64)
    attribution = models.CharField(max_length=64)

    def __str__(self):
        return self.officename

class Organization(models.Model):
    organizationcode = models.IntegerField(primary_key=True)
    organizationname = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    datejoined = models.DateField()
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zipcode = models.IntegerField()
    phonenumber = models.CharField(max_length=64)

    def __str__(self):
        return self.organizationname

class Subscriber(models.Model):
    subscriberID = models.IntegerField(primary_key=True)
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    subscriptiontypecode = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    servicecode = models.ForeignKey(Service, on_delete=models.CASCADE)
    requestdate = models.DateField()
    startdate = models.DateField()
    enddate = models.DateField()
    motifofcancellation = models.CharField(max_length=64)
    beneficiaryID = models.IntegerField()

#    def __str__(self):
#        return UserInfo.username

class TransferredSubscription(models.Model):
    transferID = models.IntegerField(primary_key=True)
    transferfrom = models.CharField(max_length=64)
    transferto = models.CharField(max_length=64)
    requestdate = models.DateField()
    transferdate = models.DateField()
    subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.transferfrom

class Officer(models.Model):
    officecode = models.ForeignKey(Office, on_delete=models.CASCADE)
    subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()

#    def __str__(self):
#        return Subscriber.username

class OrganizationMember(models.Model):
    organizationcode = models.ForeignKey(Organization, on_delete=models.CASCADE)
    subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    nativecountry = models.CharField(max_length=64)
    citizenship = models.CharField(max_length=64)
    isdelegate = models.CharField(max_length=64)

#    def __str__(self):
#        return Subscriber.username
