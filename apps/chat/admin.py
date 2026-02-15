from django import forms
from django.contrib import admin
from .models import ChatRoom, Message

class MessageAdminForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # اگر chat_room مشخص شده باشه، فقط پیام‌های همون اتاق برای فیلد answer قابل انتخاب باشند
        if 'chat_room' in self.data:
            try:
                chat_room_id = self.data.get('chat_room')
                self.fields['answer'].queryset = Message.objects.filter(chat_room_id=chat_room_id)
            except (ValueError, TypeError):
                self.fields['answer'].queryset = Message.objects.none()
        elif self.instance.pk and self.instance.chat_room:
            self.fields['answer'].queryset = Message.objects.filter(chat_room=self.instance.chat_room)
        else:
            self.fields['answer'].queryset = Message.objects.none()

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_session_key', 'admin', 'created_at', 'is_active')
    search_fields = ('user_session_key', 'admin__username')
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('id', 'created_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    form = MessageAdminForm
    list_display = ('id', 'chat_room', 'short_text', 'is_from_admin', 'is_seen', 'created_at', 'answer')
    list_filter = ('is_from_admin', 'is_seen', 'created_at')
    search_fields = ('text', 'chat_room__user_session_key')
    readonly_fields = ('created_at',)

   

    def short_text(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    short_text.short_description = 'متن پیام'
