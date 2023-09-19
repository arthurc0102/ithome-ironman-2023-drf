from rest_framework import response, views


class HealthView(views.APIView):
    def get(self, request):
        return response.Response({"health": True})
