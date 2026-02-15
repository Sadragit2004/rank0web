from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, ChatRoom
from sms_ir import SmsIr

@receiver(post_save, sender=Message)
def send_sms_on_new_message(sender, instance, created, **kwargs):
    if created and not instance.is_from_admin:
        chat_room = instance.chat_room
        
        # اگر پیامک قبلا برای این چت ارسال نشده باشد
        if not chat_room.sms_sent:
            try:
                # ارسال پیامک با متن اولین پیام کاربر
                sms_ir = SmsIr('he4QV5RJiXYsfgjHBpgjpJ2GMFtemy28GSEcDlCpEweK9q0ahroGcmgT5kexuJUR')
                
                result = sms_ir.send_verify_code(
                    number='09309087909',  # شماره مقصد
                    template_id=977780,
                    parameters=[
                        {
                            "name": "TEXT",
                             "value": f"{instance.text[:25]}" 
                        },
                    ],
                )
                
                # علامت گذاری که پیامک ارسال شده
                chat_room.sms_sent = True
                chat_room.save()
                
            except Exception as e:
                # در صورت خطا می‌توانید لاگ کنید
                print(f"Error sending SMS: {e}")