"""Models for call management system."""

from django.db import models
from django.utils import timezone


class TypeCall(models.Model):
    """مدل مربوط به نوع تماس‌های دریافتی."""

    title_type = models.CharField(max_length=100, verbose_name='نوع درخواست')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')

    def __str__(self):
        """نمایش رشته‌ای نوع تماس."""
        return self.title_type

    class Meta:
        verbose_name = 'نوع تماس'
        verbose_name_plural = 'انواع تماس'


class Call(models.Model):
    """مدل مربوط به اطلاعات تماس‌های ثبت‌شده."""

    type_call = models.ForeignKey(
        TypeCall, on_delete=models.CASCADE, related_name='calls', verbose_name='نوع تماس'
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    title_time = models.CharField(max_length=100, verbose_name='زمان تماس')
    link_city = models.TextField(verbose_name='آدرس شهر', blank=True, null=True)

    def __str__(self):
        """نمایش رشته‌ای اطلاعات تماس."""
        return f'تماس {self.phone_number} - {self.type_call.title_type}'

    class Meta:
        verbose_name = 'تماس'
        verbose_name_plural = 'تماس‌ها'
