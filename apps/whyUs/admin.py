from django.contrib import admin
from .models import ServiceList,Collaboration,Resum_company, Member_Company, SocialMedia,Plan,PlanItem
# Register your models here.


@admin.register(Collaboration)
class CollbrationAdmin(admin.ModelAdmin):

    list_display = ('name_c',)


@admin.register(Resum_company)
class ResumCompanyAdmin(admin.ModelAdmin):

    list_display = ('title',)



# SocialMedia Inline for Member_Company
class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1  # Number of empty forms for adding new records
    fields = ('icon', 'link')  # Fields to display in the inline
    verbose_name = 'شبکه اجتماعی'
    verbose_name_plural = 'شبکه‌های اجتماعی'





# Member Company Admin
@admin.register(Member_Company)
class MemberCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'who', 'is_active', 'created_at', 'update_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'who')
    ordering = ('-created_at',)
    inlines = [SocialMediaInline]  # Add the TabularInline here


@admin.register(ServiceList)
class AdminServiceList(admin.ModelAdmin):

    list_display = ('title',)



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
    inlines = [PlanItemInline]  # TabularInline for PlanItem
    verbose_name = 'پلن'
    verbose_name_plural = 'پلن‌ها'