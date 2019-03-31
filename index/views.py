from django.contrib.auth.decorators import login_required

from lib.http_decorators import http_response

@login_required
@http_response('index.html')
def index(request):
    user = request.user
    print(user)
    return dict(user=user)

