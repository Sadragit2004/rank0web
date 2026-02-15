from django.contrib import admin
from .models import Customer,text_seo,MetaTag,SocialMedia,Company, MainInfo,FAQ,WhyUs,why_us_2,a_href


# سفارشی‌سازی پنل ادمین برای مدل Company
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_company', 'phone_number', 'mobile_number', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name_company', 'phone_number', 'mobile_number')
    ordering = ('-created_at',)



# سفارشی‌سازی پنل ادمین برای مدل Main_Info
@admin.register(MainInfo)
class MainInfoAdmin(admin.ModelAdmin):
    list_display = ('subject', 'link_button', 'anchor_text')
    search_fields = ('subject', 'link_button', 'anchor_text')
    ordering = ('subject',)



@admin.register(FAQ)
class QustionF(admin.ModelAdmin):

    list_display = ('answer',)

@admin.register(WhyUs)
class WhyUs(admin.ModelAdmin):

    list_display = ('subject',)



class A_hrefInline(admin.TabularInline):

    model =  a_href
    extra = 1


@admin.register(why_us_2)
class Why_2(admin.ModelAdmin):

    list_display = ('subject',)
    inlines = [A_hrefInline]


@admin.register(SocialMedia)
class SocialMediaClass(admin.ModelAdmin):

    list_display = ('name_title',)




@admin.register(MetaTag)
class Meta_admin(admin.ModelAdmin):

    list_display = ('site_name','page_title',)
    
    

@admin.register(text_seo)
class seo_admin(admin.ModelAdmin):

    list_display = ('description',)
    
    
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'mobile_number', 'is_call']
    list_filter = ['is_call']
    search_fields = ['fullname', 'mobile_number']



from .models import Comm

class CommAdmin(admin.ModelAdmin):
    # فیلدهایی که در لیست نمایش داده میشوند
    list_display = ('fullname', 'des', 'display_image', 'display_video')
    
    # امکان جستجو بر اساس فیلدهای متنی
    search_fields = ('fullname', 'des')
    
    # فیلترهای سمت راست
    list_filter = ('fullname',)
    
    # نمایش فیلدها به صورت گروهبندی شده
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('fullname', 'des')
        }),
        ('فایل‌های چندرسانه‌ای', {
            'fields': ('image_name', 'video_name'),
            'classes': ('collapse',)  # امکان جمع شدن این بخش
        }),
    )
    
    # تابع برای نمایش تصویر در لیست
    def display_image(self, obj):
        if obj.image_name:
            return f'<img src="{obj.image_name.url}" width="50" height="50" />'
        return "بدون تصویر"
    display_image.short_description = 'تصویر'
    display_image.allow_tags = True
    
    # تابع برای نمایش ویدیو در لیست
    def display_video(self, obj):
        if obj.video_name:
            return f'<a href="{obj.video_name.url}">دانلود ویدیو</a>'
        return "بدون ویدیو"
    display_video.short_description = 'ویدیو'
    display_video.allow_tags = True

# ثبت مدل در پنل ادمین
admin.site.register(Comm, CommAdmin)
