def social_authenticate(request, token):
    adapter = GoogleOAuth2Adapter(request)
    login = adapter.complete_login(request, SocialLogin(), token)
    login.token = SocialToken(request, login)
    ret = complete_social_login(request, login)
    if not ret.user:
        return None
    return ret.user