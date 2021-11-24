from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from pinterest.models import Pin,User
from .serializers import PinSerializer,UserSerializer,PinListSerializer
from rest_framework import permissions
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': reverse('userlist',request=request),
        'Pins': reverse('pinlist', request=request),
    })

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class PinList(generics.ListAPIView):

    # queryset = Pin.objects.filter(owner__username='israa1').all()
    queryset = Pin.objects.all()
    serializer_class = PinListSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]



class PinCreate(generics.CreateAPIView):

    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


#
# class PinList(APIView):
#
#     def get(self,request,format=None):
#         try:
#             pins = Pin.objects.all()
#         except Exception as e:
#             return Response({'massegs': 'id not available'},status=status.HTTP_400_BAD_REQUEST)
#         serializedPins = PinSerializer(pins, many=True)
#         return Response(serializedPins.data)
#
#
#     def post(self,request):
#         serializedPin= PinSerializer(data=request.data)
#         if serializedPin.is_valid():
#             serializedPin.save()
#             return Response(serializedPin.data,status=status.HTTP_201_CREATED)
#         return Response(serializedPin.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class PinDetail(APIView):
#
#     def get(self,request,id):
#         try:
#             pin = Pin.objects.get(pk=id)
#         except Exception as e:
#             return Response({'massegs': 'id not available'},status=status.HTTP_400_BAD_REQUEST)
#         serializedPins = PinSerializer(pin)
#         return Response(serializedPins.data)
#
# #     def patch(self,request,id):
#         try:
#             pin = Pin.objects.get(pk=id)
#         except Exception as e:
#             return Response({'massegs': 'id not available'},status=status.HTTP_400_BAD_REQUEST)
#         serializedPin = PinSerializer(data=request.data, instance=pin)
#         if serializedPin.is_valid():
#             serializedPin.save()
#             return Response(serializedPin.data, status=status.HTTP_201_CREATED)
#         return Response(serializedPin.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,id):
#         try:
#             pin = Pin.objects.get(pk=id)
#         except Exception as e:
#             return Response({'massegs': 'id not available'}, status=status.HTTP_400_BAD_REQUEST)
#         pin.delete()
#         return Response({'massegs': '{} is deleted'.format(pin.title)}, status=status.HTTP_200_OK)


@api_view(['GET'])
def hello(request):
    pass