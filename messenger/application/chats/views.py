from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
def custom_handler405(request, exception):
    # Call when Http404 raised
    return HttpResponseNotAllowed('Этот метод запрещён!')

def index(request):
    return render(request, "chats/index.html")

def chat_create(request):
    if request.method == "POST": 
        return JsonResponse({"method":"create chat"}) 
    else:        
        return HttpResponse(status=405)

def chat_list(request):
    if request.method == "GET": 
        return JsonResponse({"method":"chat list"}) 
    else: 
        return HttpResponse(status=405)

def chat_detail(request, chat_id):
    if request.method == "GET": 
        return JsonResponse({"method":"chat detail", "chat_id":f"{chat_id}"}) 
        '''try:
            chat_id = request.GET.get('chat_id')
            chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            raise Http404
        return HttpResponse(chat.description, content_type='text/plain')'''
    else: 
        return HttpResponse(status=405)
    