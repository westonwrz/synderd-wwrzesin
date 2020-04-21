from django.contrib import admin
from .models import UserInfo, SubscriptionType, Service, Office, Organization, Subscriber, TransferredSubscription, Officer, OrganizationMember 


# Register your models here.
admin.site.register(UserInfo)
admin.site.register(SubscriptionType)
admin.site.register(Service)
admin.site.register(Office)
admin.site.register(Organization)
admin.site.register(Subscriber)
admin.site.register(TransferredSubscription)
admin.site.register(Officer)
admin.site.register(OrganizationMember)
