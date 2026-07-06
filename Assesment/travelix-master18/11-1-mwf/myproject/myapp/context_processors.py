from .models import User

def user_context(request):
    user = None
    if 'email' in request.session:
        try:
            user = User.objects.get(email=request.session['email'])
        except User.DoesNotExist:
            pass
    return {'app_user': user}
