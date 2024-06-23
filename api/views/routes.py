from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class getRoutes(APIView):
    def get(self,request):
        routes = [
            {'POST','/api/token'},
            {'POST','/api/refresh_token'},
            
            
            {'POST','api/register'}
        ]
        return Response(routes)