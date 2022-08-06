from django.shortcuts import render

# Create your views here.
def index_view(request):
    # if request.user.is_authenticated:
    #     context={
    #         'user'
    #     }
    return render(request, 'home/main.html')