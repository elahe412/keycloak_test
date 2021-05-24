from keycloak import KeycloakOpenID


# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

# from keycloak import KeycloakAdmin



# keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
#                                username='admin',
#                                password='admin',
#                                realm_name="master",
#                                # user_realm_name="myrealm",
#                                client_secret_key="0c720a33-63cb-4068-944e-341e4c970cc6",
#                                verify=True)


keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                    client_id="myclient",
                    realm_name="myrealm",
                    client_secret_key="0c720a33-63cb-4068-944e-341e4c970cc6")


config_well_know = keycloak_openid.well_know()


class ClientView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        token = keycloak_openid.token(username, password)
        return Response(token)


# class CreateUser(APIView):
#     def post(self,request):
#         username=request.data['username']
#         password = request.data['password']
#         new_user = keycloak_admin.create_user({
#                                                "username": username,
#                                                "enabled": True,
#                                                "credentials": [{"value": password, "type": "password", }]})
#
#
#         return Response(new_user)



