from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from quickstart.models import SalesMan, Agency


class Location(models.Model):
    salesman = models.ForeignKey(SalesMan, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    point = models.PointField(default='POINT(0 0)', srid=4326)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def longtitude(self):
        return self.point[0]

    @property
    def latitude(self):
        return self.point[1]


class AgencyLocation(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    point = models.PointField(default='POINT(0 0)', srid=4326)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def longtitude(self):
        return self.point[0]

    @property
    def latitude(self):
        return self.point[1]
