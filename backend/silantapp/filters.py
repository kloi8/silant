from django_filters import rest_framework as filters

from .models import Machine, Maintenance, Reclamation

class MachineFilters(filters.FilterSet):
    class Meta:
        model = Machine
        fields = ['machineModel', 'engineModel', 'transmissionModel', 'driveBridgeModel', 'controlledBridgeModel', 'machineNumber']


class MaintenanceFilter(filters.FilterSet):
    class Meta:
        model = Maintenance
        fields = ['maintType', 'machine', 'serviceCompany']


class ReclamationFilter(filter.FilterSet):
    class Meta:
        model = Reclamation
        fields = ['refusalPoint', 'recoveryMethod', 'serviceCompany']