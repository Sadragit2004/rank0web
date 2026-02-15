"""Models for About Us page, including gallery, meta tags, and schema code."""

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import jdatetime
from django.utils import timezone
import funcs


class AboutUs(models.Model):
    """Model representing the About Us page."""
    subject = models.CharField(max_length=100, verbose_name='نوع موضوع')
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ اپدیت')
    city = models.TextField(verbose_name='شهر', blank=True, null=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'درباره شرکت'
        verbose_name_plural = 'درباره شرکت'

class GalleryAbout(models.Model):
    """Model for storing images related to the About Us page."""
    page = models.ForeignKey(AboutUs, on_delete=models.CASCADE, verbose_name='صفحه', related_name='about_image')
    image_upload = funcs.FileUpload('images', 'main_info')
    image_name = models.ImageField(upload_to=image_upload.upload_to, verbose_name='ادرس عکس صفحه اصلی', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ اپدیت')
    alt = models.CharField(max_length=100, verbose_name='متن جایگزین', blank=True, null=True)

    def __str__(self):
        return self.page.subject

    def get_jalali_register_date(self):
        """Return the Jalali date for created_at."""
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y/%m/%d')

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'گالری درباره ما'

class ItemGallery(models.Model):
    """Model for storing gallery items for About Us."""
    page = models.ForeignKey(AboutUs, on_delete=models.CASCADE, verbose_name='صفحه', related_name='item_about')
    subject = models.CharField(max_length=100, verbose_name='گزینه')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ اپدیت')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس گالری'

class MetaTagModel(models.Model):
    """Model for storing meta tags for SEO purposes."""
    site_name = models.CharField(max_length=255, null=True, blank=True)
    page_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    alt = models.CharField(null=True, blank=True, max_length=100)
    og_image = models.URLField(null=True, blank=True)
    og_url = models.URLField(null=True, blank=True)
    og_type = models.CharField(max_length=50, null=True, blank=True)
    index = models.BooleanField(verbose_name='ایندکس', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_title or 'Meta Tag'

    class Meta:
        verbose_name = 'متا تگ درباره من'
        verbose_name_plural = 'متا تگ‌های درباره من'

    def save(self, *args, **kwargs):
        """Ensure description length does not exceed 128 characters."""
        if self.description and len(self.description) > 128:
            self.description = self.description[:128]
        super().save(*args, **kwargs)

class SchemaCode(models.Model):
    """Model for storing structured schema code for the About Us page."""
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE, verbose_name='درباره من')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    text_field = RichTextUploadingField(verbose_name='2توضیحات', config_name='special', blank=True)

    def __str__(self):
        return f"Schema for {self.about.subject}"

    class Meta:
        verbose_name = 'Schema Code'
        verbose_name_plural = 'Schema Codes'
