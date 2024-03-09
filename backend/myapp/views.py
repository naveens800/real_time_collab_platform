from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
import graphene
from graphql import GraphQLError
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.models import SocialToken, SocialLogin
from allauth.socialaccount.helpers import complete_social_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .types import AuthPayload, UserType 
from .utils import social_authenticate
    


class Login(graphene.Mutation):
    """
    Log In view for alread registered user
    """
    
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
    
    auth_payload = graphene.Field(AuthPayload)
    
    
    
    @staticmethod
    def mutate(root, info, username, password):
        if user := authenticate(info.context, username=username, password=password):
            login(info.context, user)
            return Login(auth_payload=AuthPayload(user=user))
        raise GraphQLError("Authentication Failed, Please check your credentials!")


class GoogleLogin(graphene.Mutation):
    """
    Google Sign up for Social Log in
    """
    
    class Arguments:
        token = graphene.String(required=True)
    
    user = graphene.Field(UserType)
    
    def mutate(self, info, token):
        user = social_authenticate(request=info.context, token=token)
        if user is None:
            raise GraphQLError("Authentication Failed")
        return GoogleLogin(user=user)
