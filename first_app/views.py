from django.template.context_processors import request
from rest_framework.response import Response
from rest_framework.views import APIView
from first_app.models import UserModel
from django.forms import model_to_dict

class First_App_View(APIView):
    def get(self, *args, **kwargs):
        users = UserModel.objects.all()
        users = [model_to_dict(user) for user in users]
        return Response(users)
    def post(self, *args, **kwargs):
        data = self.request.data
        user = UserModel.objects.create(**data)
        return Response(model_to_dict(user))

class First_App_Second_View(APIView):
    def get(self, *args, **kwargs):
        return Response('Hello Get')
    def put(self, *args, **kwargs):
        return Response('Hello put')
    def patch(self, *args, **kwargs):
        return Response('Hello patch')
    def delete(self, *args, **kwargs):
        return Response('Hello delete')