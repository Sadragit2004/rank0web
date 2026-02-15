from django.contrib import admin
from .models import MetaTagModelGroup,Sample, Item, Feature, GallerySiteSample,GroupSample



class MetaTagModeGroupAdminTabular(admin.TabularInline):

    model = MetaTagModelGroup
    extra = 1


@admin.register(GroupSample)
class GroupSampleAdmin(admin.ModelAdmin):

    list_display = ('title_group',)
    inlines = [MetaTagModeGroupAdminTabular]

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1  # تعداد خطوط اضافی برای اضافه کردن رکورد جدید


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1


class GallerySiteSampleInline(admin.TabularInline):
    model = GallerySiteSample
    extra = 1


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    inlines = [ItemInline, FeatureInline, GallerySiteSampleInline]

    class Media:
        css = {
            'all': ('custom_admin.css',)  # می‌توانید فایل CSS برای استایل شخصی اضافه کنید
        }
        js = ('custom_admin.js',)  # فایل جاوااسکریپت دلخواه


# ثبت سایر مدل‌ها در پنل ادمین
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'sample', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'sample', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)


@admin.register(GallerySiteSample)
class GallerySiteSampleAdmin(admin.ModelAdmin):
    list_display = ('sample', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
