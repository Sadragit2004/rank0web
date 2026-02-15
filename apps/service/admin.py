from django.contrib import admin
from .models import ServiceGallery, VideoService, Meta_tag_model_group, faq, Service, Item, Plan, PlanItem, Groups, Meta_tag_model

# Inline configuration for Item (TabularInline)
class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
    verbose_name = 'آیتم'
    verbose_name_plural = 'آیتم‌ها'

class PlanInlineTabular(admin.TabularInline):
    model = Plan
    extra = 1
    verbose_name = 'پلن'
    verbose_name_plural = 'پلن‌ها'

class FaqTabularInline(admin.TabularInline):
    model = faq
    extra = 1
    verbose_name = 'سوال متداول'
    verbose_name_plural = 'سوالات متداول'

class ServiceGalleryInline(admin.TabularInline):
    model = ServiceGallery
    extra = 1
    verbose_name = 'گالری سرویس'
    verbose_name_plural = 'گالری سرویس‌ها'

class VideoServiceInline(admin.TabularInline):
    model = VideoService
    extra = 1
    verbose_name = 'ویدیو سرویس'
    verbose_name_plural = 'ویدیوهای سرویس'

class MetaTagModelGroupAdminTabular(admin.TabularInline):
    model = Meta_tag_model_group
    extra = 1
    verbose_name = 'متا تگ گروه'
    verbose_name_plural = 'متا تگ‌های گروه'

# Admin configuration for Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    inlines = [ItemInline, PlanInlineTabular, FaqTabularInline, VideoServiceInline, ServiceGalleryInline]
    verbose_name = 'سرویس'
    verbose_name_plural = 'سرویس‌ها'

# Inline configuration for PlanItem (TabularInline)
class PlanItemInline(admin.TabularInline):
    model = PlanItem
    extra = 1
    verbose_name = 'آیتم پلن'
    verbose_name_plural = 'آیتم‌های پلن'

# Admin configuration for Plan
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'price')
    inlines = [PlanItemInline]
    verbose_name = 'پلن'
    verbose_name_plural = 'پلن‌ها'

# Admin configuration for Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    verbose_name = 'آیتم'
    verbose_name_plural = 'آیتم‌ها'

# Admin configuration for PlanItem
@admin.register(PlanItem)
class PlanItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'plan', 'is_checked', 'created_at', 'update_at')
    list_filter = ('is_checked', 'created_at')
    search_fields = ('title',)
    verbose_name = 'آیتم پلن'
    verbose_name_plural = 'آیتم‌های پلن'

@admin.register(Groups)
class GroupsServiceAdmin(admin.ModelAdmin):
    list_display = ('title_group',)
    inlines = [MetaTagModelGroupAdminTabular]
    verbose_name = 'گروه'
    verbose_name_plural = 'گروه‌ها'

@admin.register(Meta_tag_model)
class MetaAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'service',)
    verbose_name = 'متا تگ'
    verbose_name_plural = 'متا تگ‌ها'