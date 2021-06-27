
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import DroneCategory
from .models import Drone
from .models import Pilot
from .models import Competition
from .serializers import DroneCategorySerializer
from .serializers import DroneSerializer
from .serializers import PilotSerializer
from .serializers import PilotCompetitionSerializer

# Add filtering, searching and ordering
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    filter_fields = (
        'name',
        )
    search_fields = ( # enable searching
        '^name',
        )
    ordering_fields = (
        'name',
        )

# No filtering
# class DroneCategoryList(generics.ListCreateAPIView):
#     queryset = DroneCategory.objects.all()
#     serializer_class = DroneCategorySerializer
#     name = 'dronecategory-list'


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_competed',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        'manufacturing_date',
        )
# No Filtering
# class DroneList(generics.ListCreateAPIView):
#     queryset = Drone.objects.all()
#     serializer_class = DroneSerializer
#     name = 'drone-list'


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'

class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    filter_fields = (
        'name',
        'gender',
        'races_count',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        'races_count'
        )
# No Filtering
# class PilotList(generics.ListCreateAPIView):
#     queryset = Pilot.objects.all()
#     serializer_class = PilotSerializer
#     name = 'pilot-list'


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'

# Add customized filter for competition
# class CompetitionFilter(filters.FilterSet):
#     from_achievement_date = DateTimeFilter(
#         name='distance_achievement_date', lookup_expr='gte') # >= specified DateTime value
#     to_achievement_date = DateTimeFilter(
#          name='distance_achievement_date', lookup_expr='lte') # <= specified DateTime value
#     min_distance_in_feet = NumberFilter(
#          name='distance_in_feet', lookup_expr='gte') # >=
#     max_distance_in_feet = NumberFilter(
#          name='distance_in_feet', lookup_expr='lte')
#     drone_name = AllValuesFilter( # whose drone's name match specified string value, double underscores: name field
#          name='drone__name')  # drone__name can be replaced as drone.name
#     pilot_name = AllValuesFilter(
#          name='pilot__name')
#
#     class Meta:
#         model = Competition
#         fields = (
#             'distance_in_feet',
#             'from_achievement_date',
#             'to_achievement_date',
#             'min_distance_in_feet',
#             'max_distance_in_feet',
#             # drone__name will be accessed as drone_name
#             'drone_name',
#             # pilot__name will be accessed as pilot_name
#             'pilot_name',
#         )
#

class CompetitionFilter(filters.FilterSet):
    from_achievement_date = DateTimeFilter(
        field_name='distance_achievement_date', lookup_expr='gte') # >= specified DateTime value
    to_achievement_date = DateTimeFilter(
         field_name='distance_achievement_date', lookup_expr='lte') # <= specified DateTime value
    min_distance_in_feet = NumberFilter(
         field_name='distance_in_feet', lookup_expr='gte') # >=
    max_distance_in_feet = NumberFilter(
         field_name='distance_in_feet', lookup_expr='lte')
    drone_name = AllValuesFilter( # whose drone's name match specified string value, double underscores: name field
         field_name='drone__name')  # drone__name can be replaced as drone.name
    pilot_name = AllValuesFilter(
         field_name='pilot__name')

    class Meta:
        model = Competition
        fields = (
            'distance_in_feet',
            'from_achievement_date',
            'to_achievement_date',
            'min_distance_in_feet',
            'max_distance_in_feet',
            # drone__name will be accessed as drone_name
            'drone_name',
            # pilot__name will be accessed as pilot_name
            'pilot_name',
        )



class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'
    filter_class = CompetitionFilter
    ordering_fields = (
        'distance_in_feet',
        'distance_achievement_date',
    )

# class CompetitionList(generics.ListCreateAPIView):
#      queryset = Competition.objects.all()
#      serializer_class = PilotCompetitionSerializer
#      name = 'competition-list'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name,
            request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
            })
