from django.contrib import admin
from .models import main_tag_mag,FAQ,SocialMediaAuthor,GroupMagModel, Mag, MetaTagModel, AuthorMagModel, MagMainSlider,MetaTagModelGroup,LableBlog
import jdatetime

# تبدیل تاریخ میلادی به شمسی
def convert_to_jalali(date):
    return jdatetime.datetime.fromgregorian(datetime=date).strftime('%Y/%m/%d') if date else "-"


class FaqTabularAdmin(admin.TabularInline):

    model = FAQ
    extra = 1
    
class LableBlogTabularAdmin(admin.TabularInline):

    model = LableBlog
    extra = 1

class GroupTanualarAdmin(admin.TabularInline):

    model = GroupMagModel
    extra = 1

class SocialTanualarAdmin(admin.TabularInline):

    model = SocialMediaAuthor
    extra = 1
    
    
class MetaTagModelGroupTanualarAdmin(admin.TabularInline):

    model = MetaTagModelGroup
    extra = 1


@admin.register(GroupMagModel)
class GroupMagAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_group', 'subgroup_count', 'mag_count', 'is_active', 'created_at_jalali')
    list_filter = ('is_active',)
    search_fields = ('title',)
    actions = ['make_active', 'make_inactive']
    inlines = [GroupTanualarAdmin,MetaTagModelGroupTanualarAdmin]

    def subgroup_count(self, obj):
        return obj.parent_of_group.count()
    subgroup_count.short_description = "تعداد زیرگروه‌ها"

    def mag_count(self, obj):
        return obj.magazines.count()
    mag_count.short_description = "تعداد مقالات"

    def created_at_jalali(self, obj):
        return convert_to_jalali(obj.created_at)
    created_at_jalali.short_description = "تاریخ ثبت (شمسی)"

    @admin.action(description="فعال کردن گروه‌های انتخاب‌شده")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="غیرفعال کردن گروه‌های انتخاب‌شده")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)


@admin.register(Mag)
class MagAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_groups', 'is_active', 'view', 'create_at_jalali')
    list_filter = ('is_active', 'group')
    search_fields = ('title', 'author__full_name')
    actions = ['make_active', 'make_inactive']
    inlines = [FaqTabularAdmin,LableBlogTabularAdmin]

    def get_groups(self, obj):
        if obj.group:
            return obj.group.title
        return "-"
    get_groups.short_description = "گروه‌ها"


    def create_at_jalali(self, obj):
        return convert_to_jalali(obj.create_at)
    create_at_jalali.short_description = "تاریخ ثبت (شمسی)"

    @admin.action(description="فعال کردن مقالات انتخاب‌شده")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="غیرفعال کردن مقالات انتخاب‌شده")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)


@admin.register(AuthorMagModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'gmail', 'is_active', 'created_at_jalali')
    list_filter = ('is_active',)
    search_fields = ('full_name', 'user__username')
    inlines = [SocialTanualarAdmin]

    def created_at_jalali(self, obj):
        return convert_to_jalali(obj.created_at)
    created_at_jalali.short_description = "تاریخ ثبت (شمسی)"


@admin.register(MetaTagModel)
class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'site_name', 'index', 'created_at_jalali')
    list_filter = ('index',)
    search_fields = ('page_title', 'site_name')

    def created_at_jalali(self, obj):
        return convert_to_jalali(obj.created_at)
    created_at_jalali.short_description = "تاریخ ثبت (شمسی)"


@admin.register(MagMainSlider)
class MagMainSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_name')
    search_fields = ('title',)




@admin.register(main_tag_mag)
class MainTagAdmin(admin.ModelAdmin):

    list_display = ('site_name',)