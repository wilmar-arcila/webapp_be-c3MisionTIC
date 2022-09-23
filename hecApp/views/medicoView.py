from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hecApp.serializers.medicoSerializer import MedicoSerializer
from hecApp.serializers.usuarioSerializer import UsuarioSerializer
from hecApp.models.usuario import Usuario
from hecApp.models.medico import Medico

class MedicoListCreateView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los medicos")
        queryset = self.get_queryset()
        serializer = MedicoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print("POST a Medico")
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU  = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        mdData = request.data
        mdData.update({"usuario":usuario.id})
        serializerMd = MedicoSerializer(data=mdData)
        serializerMd.is_valid(raise_exception=True)
        serializerMd.save()
        return Response(status=status.HTTP_201_CREATED)

        """ tokenData = {
                     "username":request.data["username"],
                     "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) """

class MedicoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Medico")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("DELETE a Medico")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)