from rest_framework import serializers

from pinterest.models import Pin,User
# from .serializers import PinSerializer
# from rest_framework.serializers import HyperlinkedIdentityField

# pinDetailURL= HyperlinkedIdentityField(view_name= 'pinterest:pindetails',lookup_field='title')



#pinList
class PinSerializer(serializers.ModelSerializer):
    owner= serializers.HyperlinkedRelatedField(
                    read_only=True,
                    view_name='userdetails'
                )
    # owner= {
    #     'username': serializers.ReadOnlyField(source='owner.username'),
    #     'Url' : serializers.HyperlinkedRelatedField(
    #                 many=True,
    #                 read_only=True,
    #                 view_name='userdetails'
    #             )
    # }
    # url=pinDetailURL
    class Meta:
        model = Pin
        # fields= ['id', 'title', 'alt_description', 'owner','url']
        fields= ['id', 'title', 'alt_description', 'owner']

        # fields ='__all__'


class PinListSerializer(serializers.ModelSerializer):
    owner= serializers.HyperlinkedRelatedField(
                    read_only=True,
                    view_name='userdetails'
                )

    url= serializers.HyperlinkedIdentityField(view_name='pindetails')

    ownerName=serializers.SerializerMethodField(method_name= 'get_ownerName')

    profilePic=serializers.SerializerMethodField(method_name= 'get_profilePic')


    def get_ownerName(self,obj):
        return obj.owner.username

    def get_profilePic(self,obj):
        try:
            image= obj.owner.kkk
        except:
            image= None     #we will put the default pic, or we will store it in the frontend to prevent reloading
        return image

    class Meta:
        model = Pin

        fields= ['url', 'title','owner','ownerName' ,'profilePic','salma']




class UserSerializer(serializers.ModelSerializer):
    # pins= serializers.PrimaryKeyRelatedField(many=True, queryset=Pin.objects.all())
    # pins=PinSerializer(many=True)

    pins=PinListSerializer(many=True)

    # pins = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='pindetails'
    # )

    followers= serializers.ReadOnlyField(source='followers.username')

    class Meta:
        model = User
        # fields='__all__'
        fields=['id','username','pins','followers']
