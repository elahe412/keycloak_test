from keycloak import KeycloakOpenID
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from keycloak import KeycloakAdmin

from client.migrations.serializers import ClientSerializer

keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                               username='example-admin',
                               password='secret',
                               realm_name="master",
                               user_realm_name="only_if_other_realm_than_master",
                               client_secret_key="client-secret",
                               verify=True)


keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                    client_id="example_client",
                    realm_name="example_realm",
                    client_secret_key="secret")


config_well_know = keycloak_openid.well_know()


class ClientView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        token = keycloak_openid.token(username, password)
        return Response(token)


class CreateUser(APIView):
    def post(self,request):
        username=request.data['username']
        password = request.data['password']
        new_user = keycloak_admin.create_user({
                                               "username": username,
                                               "enabled": True,
                                               "credentials": [{"value": password, "type": "password", }]})


        return Response(new_user)



