from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework import routers

#UserInfo, SubscriptionType, Service, Office, Organization, Subscriber, TransferredSubscription, Officer, OrganizationMember 


router = routers.DefaultRouter()
router.register('userinfo', views.UserInfoView)
router.register('subscriptiontype', views.SubscriptionTypeView)
router.register('service', views.ServiceView)
router.register('office', views.OfficeView)
router.register('organization', views.OrganizationView)
router.register('subscriber', views.SubscriberView)
router.register('transferredsubscription', views.TransferredSubscriptionView)
router.register('officer', views.OfficerView)
router.register('organizationmember', views.OrganizationMemberView)


urlpatterns = [
    path('', include(router.urls))
]
