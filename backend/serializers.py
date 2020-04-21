from rest_framework import serializers
from .models import UserInfo, SubscriptionType, Service, Office, Organization, Subscriber, TransferredSubscription, Officer, OrganizationMember 

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class TransferredSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferredSubscription
        fields = '__all__'

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = '__all__'

class OrganizationMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMember
        fields = '__all__'