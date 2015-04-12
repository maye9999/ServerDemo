from tastypie.resources import ModelResource
from myApp.models import InfoPack
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization


class InfoPackResource(ModelResource):

    class Meta:
        queryset = InfoPack.objects.all()
        resource_name = "infopack"
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()