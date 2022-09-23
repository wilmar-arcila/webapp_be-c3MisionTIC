from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hecApp.serializers.enfermeroSerializer import EnfermeroSerializer
from hecApp.serializers.usuarioSerializer import UsuarioSerializer
from hecApp.models.enfermero import Enfermero

class EnfermeroListCreateView(generics.ListCreateAPIView):
    queryset = Enfermero.objects.all()
    serializer_class = EnfermeroSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Enfermeros")
        queryset = self.get_queryset()
        serializer = EnfermeroSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Enfermero")
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU  = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        enfData = request.data
        enfData.update({"usuario":usuario.id})
        serializerEnf = EnfermeroSerializer(data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)

        """ tokenData = {
                     "username":request.data["username"],
                     "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) """

class EnfermeroRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Enfermero.objects.all()
    serializer_class = EnfermeroSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Enfermero")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Enfermero")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)