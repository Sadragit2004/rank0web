from django.db import models
from django.contrib.auth.models import User  # کاربر پیش‌فرض جنگو
import uuid
from django.utils import timezone


class ChatRoom(models.Model):
    """
    اتاق چت بین کاربر (بر اساس session_key) و ادمین
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
        verbose_name='شناسه چت'
    )
    user_session_key = models.CharField(
        max_length=40,
        verbose_name='شناسه سشن کاربر'
    )
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='ادمین پاسخ‌دهنده',
        related_name='assigned_chats',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='تاریخ ایجاد'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال؟'
    )
    
    
    sms_sent = models.BooleanField(
    default=False,
    verbose_name='پیامک ارسال شده؟'
)

    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"چت {self.id}"

    class Meta:
        verbose_name = 'اتاق چت'
        verbose_name_plural = 'اتاق‌های چت'


class Message(models.Model):
    chat_room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        verbose_name='اتاق چت',
        related_name='messages'
    )
    text = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='زمان ارسال'
    )
    is_from_admin = models.BooleanField(
        default=False,
        verbose_name='از طرف ادمین؟'
    )
    is_seen = models.BooleanField(
        default=False,
        verbose_name='دیده شده؟'
    )
    answer = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='replies',
        verbose_name='پاسخ به پیام'
    )
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{'ادمین' if self.is_from_admin else 'کاربر'}: {self.text[:20]}..."
