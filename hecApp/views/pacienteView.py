from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from hecApp.serializers.historiaSerializer import HistoriaSerializer
from hecApp.serializers.pacienteSerializer import PacienteSerializer
from hecApp.serializers.usuarioSerializer import UsuarioSerializer
from hecApp.models.paciente import Paciente


class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Pacientes")
        queryset = self.get_queryset()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Paciente")
        print(request.data)
        # Se extrae la información del Usuario (para separarla de la información del Paciente)
        usuarioData = request.data.pop('usuario')
        serializerU  = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        # Se separa la información necesaria para crear el token de usuario
        tokenData = {
                     "email":usuarioData["email"],
                     "password":usuarioData["password"]
                    }
        # Se verifica la información para crear el token de usuario
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        # Si todo lo correspondiente al usuario es correcto, se crea el objeto Usuario
        usuario = serializerU.save()

        pData = request.data
        pData.update({"usuario":usuario.id})
        serializerP = PacienteSerializer(data=pData)
        serializerP.is_valid(raise_exception=True)
        paciente=serializerP.save()
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class PacienteRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Paciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Paciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)