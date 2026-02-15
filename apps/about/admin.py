from django.contrib import admin
from .models import MetaTagModel,AboutUs, GalleryAbout, ItemGallery,SchemaCode


class SchemaCodeTabular(admin.TabularInline):

    model = SchemaCode
    extra = 1



@admin.register(GalleryAbout)
class GalleryAboutAdmin(admin.ModelAdmin):
    list_display = ('page', 'image_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('page__subject',)
    ordering = ('page',)
    list_editable = ('is_active',)


@admin.register(ItemGallery)
class ItemGalleryAdmin(admin.ModelAdmin):
    list_display = ('page', 'subject', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('subject', 'page__subject')
    ordering = ('page', 'subject')
    list_editable = ('is_active',)


class TabularAdminInlineAbout(admin.TabularInline):

    model = GalleryAbout
    extra  = 1


class TabularAdminInlineGallry(admin.TabularInline):

    model = ItemGallery
    extra = 1




@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('subject', 'description')
    ordering = ('subject',)
    list_editable = ('is_active',)
    inlines = [TabularAdminInlineGallry,TabularAdminInlineAbout,SchemaCodeTabular]




@admin.register(MetaTagModel)
class MetaTagModel(admin.ModelAdmin):

    list_display = ('page_title',)


