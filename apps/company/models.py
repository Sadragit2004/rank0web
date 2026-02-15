import os
from PIL import Image
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
import funcs


def validate_image_or_svg(file):
    """
    Validator to check if the uploaded file is an image or an SVG.
    """
    ext = os.path.splitext(file.name)[1].lower()
    if ext == '.svg':
        return
    try:
        img = Image.open(file)
        img.verify()
    except Exception as exc:
        raise ValidationError(_('Invalid file. Only images or SVGs are allowed.')) from exc


class Company(models.Model):
    """ Model to store company information. """
    name_company = models.CharField(max_length=50, verbose_name='نام شرکت', blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name='شماره شرکت', blank=True, null=True)
    mobile_number = models.CharField(max_length=15, verbose_name='شماره موبایل', blank=True, null=True)
    address = models.TextField(verbose_name='آدرس')
    image_upload = funcs.FileUpload('images', 'logo')
    image_name = models.FileField(upload_to=image_upload.upload_to, verbose_name='لوگو تصویر', blank=True, null=True, validators=[validate_image_or_svg])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'اطلاعات شرکت'
        verbose_name_plural = 'اطلاعات شرکت‌ها'

    def __str__(self):
        return f'{self.name_company} - {self.mobile_number}'


class MainInfo(models.Model):
    """ Model to store main page information. """
    subject = models.CharField(max_length=500, verbose_name='عنوان صفحه اصلی', blank=True, null=True)
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    image_upload = funcs.FileUpload('images', 'main_info')
    image_name = models.ImageField(upload_to=image_upload.upload_to, verbose_name='آدرس عکس صفحه اصلی', blank=True, null=True)
    video_upload = funcs.FileUpload('video', 'main_info')
    video_name = models.FileField(upload_to=video_upload.upload_to, verbose_name='آدرس ویدیو صفحه اصلی', blank=True, null=True)
    link_button = models.TextField(verbose_name='آدرس لینک')
    anchor_text = models.CharField(max_length=100, verbose_name='متن لینک', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'اطلاعات صفحه اصلی'
        verbose_name_plural = 'اطلاعات صفحه‌های اصلی'

    def __str__(self):
        return self.subject or 'بدون عنوان'


class MetaTag(models.Model):
    """ Model to store meta tags for SEO. """
    site_name = models.CharField(max_length=255, blank=True, null=True)
    page_title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    og_title = models.CharField(max_length=255, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    alt = models.CharField(max_length=100, blank=True, null=True)
    og_image = models.URLField(blank=True, null=True)
    og_url = models.URLField(blank=True, null=True)
    og_type = models.CharField(max_length=50, blank=True, null=True)
    index = models.BooleanField(default=True, verbose_name='ایندکس')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'تگ متا'
        verbose_name_plural = 'تگ‌های متا'

    def __str__(self):
        return self.site_name or 'متا بدون عنوان'

    def save(self, *args, **kwargs):
        if self.description and len(self.description) > 150:
            self.description = self.description[:150]
        super().save(*args, **kwargs)


class FAQ(models.Model):
    """ Model for frequently asked questions. """
    question = models.CharField(max_length=300, verbose_name='سوال', blank=True, null=True)
    answer = models.TextField(verbose_name='جواب', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='وضعیت')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    video_file = funcs.FileUpload('video', 'faq')
    video = models.FileField(upload_to=video_file.upload_to, verbose_name='ویدیو', blank=True, null=True)

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'

    def __str__(self):
        return self.question or 'سوال بدون عنوان'


class WhyUs(models.Model):
    """ Model to store reasons why choose us. """
    subject = models.CharField(max_length=100, verbose_name='موضوع')
    
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    
    is_active = models.BooleanField(default=True)
    register_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    image_upload = funcs.FileUpload('images', 'why_us')
    image_name = models.FileField(upload_to=image_upload.upload_to, verbose_name='لوگو تصویر', blank=True, null=True, validators=[validate_image_or_svg])

    class Meta:
        verbose_name = 'دلیل انتخاب'
        verbose_name_plural = 'دلایل انتخاب'

    def __str__(self):
        return self.subject




class why_us_2(models.Model):


    subject = models.CharField(max_length=100,verbose_name='موضوع')
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    is_active = models.BooleanField(default=True)
    register_date = models.DateTimeField(default=timezone.now(),verbose_name='تاریخ ثبت ',null=True,blank=True)



    def __str__(self):
        return f'{self.subject}'


    class Meta:

        verbose_name = 'زیر مجموعه چرا ما '





class SocialMedia(models.Model):
    """ Model to store social media links. """
    name_title = models.CharField(max_length=100, verbose_name='نام شبکه اجتماعی')
    link = models.TextField(verbose_name='لینک')
    svg_link = models.TextField(verbose_name='آدرس SVG')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه‌های اجتماعی'

    def __str__(self):
        return self.name_title



class a_href(models.Model):

    why = models.ForeignKey(why_us_2,on_delete=models.CASCADE,verbose_name='چرا ما',related_name='a_why2')
    a_link = models.CharField(max_length=1000,verbose_name='لینک ادرس')
    anker = models.CharField(max_length=100,verbose_name='متن لنگر')
    




class text_seo(models.Model):
    
    
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    
    
    
    
class Customer(models.Model):
    
    mobile_number = models.CharField(max_length=11, verbose_name='شماره موبایل')
    fullname = models.CharField(max_length=100, verbose_name='اسم کامل')
    is_call = models.BooleanField(default=True, verbose_name='تماس گرفته شود؟')

    def __str__(self):
        return self.fullname



    def __str__(self):
        return f'{self.subject}'


    class Meta:

        verbose_name = ' اطلاعات مشتریان '
        
        

class Comm(models.Model):
    
     fullname = models.CharField(max_length=100, verbose_name='اسم کامل')
     image_upload = funcs.FileUpload('images', 'why_us')
     image_name = models.FileField(upload_to=image_upload.upload_to, verbose_name='لوگو تصویر', blank=True, null=True, validators=[validate_image_or_svg])
     des = models.TextField(verbose_name='متن')
     video_upload = funcs.FileUpload('video', 'main_info')
     video_name = models.FileField(upload_to=video_upload.upload_to, verbose_name='آدرس ویدیو صفحه اصلی', blank=True, null=True)
     
     
     verbose_name = ' کامنت صفحه اصلی  '