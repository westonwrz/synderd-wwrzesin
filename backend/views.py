from django.shortcuts import render
from rest_framework import viewsets
from .models import UserInfo, SubscriptionType, Service, Office, Organization, Subscriber, TransferredSubscription, Officer, OrganizationMember 
from .serializers import UserInfoSerializer, SubscriptionTypeSerializer, ServiceSerializer, OfficeSerializer, OrganizationSerializer, SubscriberSerializer, TransferredSubscriptionSerializer, OfficerSerializer, OrganizationMemberSerializer

# Create your views here.
class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class SubscriptionTypeView(viewsets.ModelViewSet):
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class OfficeView(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class SubscriberView(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class TransferredSubscriptionView(viewsets.ModelViewSet):
    queryset = TransferredSubscription.objects.all()
    serializer_class = TransferredSubscriptionSerializer

class OfficerView(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer

class OrganizationMemberView(viewsets.ModelViewSet):
    queryset = OrganizationMember.objects.all()
    serializer_class = OrganizationMemberSerializer
