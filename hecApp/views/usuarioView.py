from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from hecApp.serializers.usuarioSerializer import UsuarioSerializer
from hecApp.models.usuario import Usuario

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los usuarios")
        print(request.user) # Información del usuario asociada a la petición
        print(request.auth) # Token usado para la petición
        user=Usuario.objects.get(id=request.user.id)
        rol = user.rol
        print(rol)
        if (rol.tipo_usuario=='AUX'):
            queryset = self.get_queryset()
            serializer = UsuarioSerializer(queryset, many=True)
            return Response(serializer.data)
        response = "Los usuarios con perfil " + rol.tipo_usuario + " no pueden listar Usuarios."
        return Response(response, status.HTTP_403_FORBIDDEN)


class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Usuario")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        print("PUT a Usuario")
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("DELETE a Usuario")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)