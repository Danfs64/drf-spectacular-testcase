from oauth2_provider.contrib.rest_framework import TokenHasScope

class TokenHasScope1(TokenHasScope):
    def get_scopes(self, request, view):
        return ['scope1']

class TokenHasScope2(TokenHasScope):
    def get_scopes(self, request, view):
        return ['scope2']
