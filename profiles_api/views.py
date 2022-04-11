from rest_framework.views import APIView
from rest_framework.response import Response


class HalloApiView(APIView):
    """Tets API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'API view'
            'This is an API View'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
