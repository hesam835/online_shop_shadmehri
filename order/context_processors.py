from . views import CartAdd

def cart(request):
    return {'cart':CartAdd(request)}