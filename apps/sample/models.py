from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
import os
from PIL import Image
import jdatetime
import funcs

# Validator for images or SVG

def validate_image_or_svg(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext == '.svg':
        return
    try:
        img = Image.open(file)
        img.verify()
    except Exception as exc:
        raise ValidationError(_('Invalid file. Only images or SVGs are allowed.')) from exc

# Models

class GroupSample(models.Model):
    title_group = models.CharField(max_length=100, verbose_name='عنوان گروه')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپدیت')
    slug = models.CharField(max_length=100, verbose_name='نامک', null=True, blank=True)

    class Meta:
        verbose_name = 'گروه نمونه'
        verbose_name_plural = 'گروه های نمونه کاران'

    def __str__(self):
        return self.title_group


class MetaTagModelGroup(models.Model):
    group_sample = models.ForeignKey(GroupSample, on_delete=models.CASCADE, verbose_name='متا تگ', blank=True, null=True)
    site_name = models.CharField(max_length=255, null=True, blank=True)
    page_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    alt = models.CharField(max_length=100, null=True, blank=True)
    og_image = models.URLField(null=True, blank=True)
    og_url = models.URLField(null=True, blank=True)
    og_type = models.CharField(max_length=50, null=True, blank=True)
    index = models.BooleanField(verbose_name='ایندکس', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sample(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    group_sample = models.ForeignKey(GroupSample, verbose_name='گروه نمونه کارها', on_delete=models.CASCADE, null=True, blank=True, related_name='group_sample')
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    description2 = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True, null=True)
    image_file = funcs.FileUpload('images', 'sample')
    image_name = models.ImageField(upload_to=image_file.upload_to, verbose_name='نام فایل')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپدیت')
    slug = models.CharField(max_length=100, verbose_name='نامک', null=True, blank=True)
    city = models.TextField(verbose_name='شهر', blank=True, null=True)
    domain = models.CharField(max_length=100, verbose_name='دامنه', null=True, blank=True)
    

    def __str__(self):
        return self.title

    def get_jalali_register_date(self):
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y/%m/%d')

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'


class Item(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='نمونه کار', related_name='sample_item')
    title = models.CharField(max_length=100, verbose_name='موضوع')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپدیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'آیتم های نمونه کار'


class Feature(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='نمونه کار', related_name='sample_feature')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    title2 = models.CharField(max_length=100, verbose_name='جواب ویژگی', blank=True, null=True)
    image_file = funcs.FileUpload('images', 'feature_sample')
    image_name = models.ImageField(upload_to=image_file.upload_to, verbose_name='نام فایل', blank=True, null=True, validators=[validate_image_or_svg])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپدیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'


class GallerySiteSample(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, verbose_name='نمونه کار', related_name='sample_Gallery')
    image_file = funcs.FileUpload('images', 'feature_sample')
    image_name = models.ImageField(upload_to=image_file.upload_to, verbose_name='نام فایل')
    alt = models.CharField(max_length=100, verbose_name='متن جایگزین', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپدیت')

    def __str__(self):
        return self.sample.title

    class Meta:
        verbose_name = 'گالری نمونه کار'
        verbose_name_plural = 'تصاویر نمونه کارها'




class Meta_tag_model(models.Model):
    Sample_model = models.ForeignKey(
        Sample, on_delete=models.CASCADE, related_name='Sample_meta', null=True, blank=True
    )
    page_title = models.CharField(max_length=255, null=True, blank=True)  # عنوان صفحه
    description = models.TextField(null=True, blank=True)  # توضیحات، حداکثر 128 کاراکتر
    og_title = models.CharField(max_length=255, null=True, blank=True)  # عنوان OG
    og_description = models.TextField(null=True, blank=True)  # توضیحات OG
    og_image = models.URLField(null=True, blank=True)  # تصویر OG (URL)

    # این فیلد برای مدیریت ساختار og (Open Graph)
    og_url = models.URLField(null=True, blank=True)  # URL برای OG
    og_type = models.CharField(max_length=50, null=True, blank=True)  # نوع محتوای OG (مثلاً article یا website)

    # برای تعیین تاریخ و زمان ایجاد و آپدیت
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_title or 'Meta Tag for {}'.format(self.service)

    def save(self, *args, **kwargs):
        # اگر توضیحات بیش از 128 کاراکتر باشد، آنها را کوتاه می‌کنیم
        if self.description and len(self.description) > 150:
            self.description = self.description[:150]
        super(Meta_tag_model, self).save(*args, **kwargs)
