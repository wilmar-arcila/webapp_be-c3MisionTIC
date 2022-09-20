from rest_framework import generics, status
from rest_framework.response import Response

class LandingView(generics.ListAPIView):
    def list(self, request):
        print("GET a Landing Page")
        mensaje = 'HOSPITALIZACIÓN EN CASA'
        return Response(mensaje, status=status.HTTP_200_OK)