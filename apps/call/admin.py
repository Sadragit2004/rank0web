from django.contrib import admin
from .models import TypeCall, Call


@admin.register(TypeCall)
class TypeCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_type', 'created_at')  # نمایش ستون‌ها
    search_fields = ('title_type',)  # امکان جستجو
    list_filter = ('created_at',)  # امکان فیلتر بر اساس تاریخ
    ordering = ('-created_at',)  # مرتب‌سازی پیش‌فرض


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_call', 'phone_number', 'title_time', 'created_at')  # ستون‌های قابل نمایش
    search_fields = ('type_call__title_type', 'phone_number')  # امکان جستجو بر اساس نوع تماس و شماره تلفن
    list_filter = ('type_call', 'created_at')  # امکان فیلتر بر اساس نوع تماس و تاریخ
    ordering = ('-created_at',)  # مرتب‌سازی پیش‌فرض
    list_per_page = 20  # تعداد نمایش رکوردها در هر صفحه

    fieldsets = (  # نمایش بخش‌های مجزا در فرم ادمین
        ('اطلاعات اصلی', {
            'fields': ('type_call', 'phone_number', 'title_time')
        }),
        ('اطلاعات اضافی', {
            'fields': ('link_city', 'created_at'),
            'classes': ('collapse',),  # بخش تاشونده
        }),
    )
