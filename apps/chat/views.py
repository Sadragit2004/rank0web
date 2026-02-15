from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ChatRoom, Message
import json
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

# v
def chat_page(request):


    return render(request, 'chat_app/chat.html')



@csrf_exempt  # در محیط production بردارید یا با token کار کنید
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text', '')

        if not request.session.session_key:
            request.session.create()

        session_key = request.session.session_key

        chat_room, _ = ChatRoom.objects.get_or_create(
            user_session_key=session_key,
            is_active=True
        )

        Message.objects.create(
            chat_room=chat_room,
            text=text,
            is_from_admin=False
        )

        return JsonResponse({'status': 'ok'})

    return JsonResponse({'status': 'invalid method'}, status=405)




def get_messages(request):
    session_key = request.session.session_key
    if not session_key:
        return JsonResponse([], safe=False)

    try:
        chat_room = ChatRoom.objects.get(user_session_key=session_key)
    except ChatRoom.DoesNotExist:
        return JsonResponse([], safe=False)

    messages = chat_room.messages.order_by('created_at').values(
        'text', 'is_from_admin', 'created_at'
    )
    return JsonResponse(list(messages), safe=False)


@staff_member_required
def admin_chat_dashboard(request):
    chat_rooms = ChatRoom.objects.filter(is_active=True).order_by('-created_at')
    selected_room = request.GET.get('room')

    if selected_room:
        current_room = ChatRoom.objects.get(id=selected_room)
        messages = Message.objects.filter(chat_room=current_room).order_by('created_at')
    else:
        current_room = None
        messages = None

    return render(request, 'chat_app/admin_dashboard.html', {
        'chat_rooms': chat_rooms,
        'current_room': current_room,
        'messages': messages,
    })


from django.db.models import Max, OuterRef, Subquery
from django.db.models import Exists

# در ویو unseen_data این تغییرات را اعمال کنید:
def unseen_data(request):
    # پیام‌های جدید: فقط پیام‌های کاربر که دیده نشده‌اند و آخرین پیام چت‌روم از کاربر است
    new_messages = Message.objects.filter(
        is_seen=False,
        is_from_admin=False,
        chat_room__in=ChatRoom.objects.annotate(
            last_msg_from_admin=Subquery(
                Message.objects.filter(
                    chat_room=OuterRef('pk')
                ).order_by('-created_at').values('is_from_admin')[:1]
            )
        ).filter(last_msg_from_admin=False)
    )

    new_messages_count = new_messages.count()

    # چت‌روم‌های جدید: چت‌روم‌هایی که هیچ پیام ادمین ندارند
    new_chatrooms_count = ChatRoom.objects.filter(
        messages__is_from_admin=False
    ).exclude(
        id__in=ChatRoom.objects.filter(messages__is_from_admin=True)
    ).distinct().count()

    return JsonResponse({
        'new_messages': new_messages_count,
        'new_chatrooms': new_chatrooms_count,
    })

def api_messages(request):
    messages = Message.objects.order_by('created_at').values('id', 'text', 'is_from_admin')
    messages_list = list(messages)
    return JsonResponse({'messages': messages_list})