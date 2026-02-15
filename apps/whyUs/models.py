from django.db import models
from django.utils import timezone
import funcs

import os  # Standard library imports
from PIL import Image
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Collaboration(models.Model):


    name_c = models.CharField(max_length=100,verbose_name='نام شرکت')
    image_file = funcs.FileUpload('images','c_company')
    image_name = models.ImageField(verbose_name='ادرس عکس',upload_to=image_file.upload_to)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )



    def __str__(self):
        return self.name_c


    class Meta:

        verbose_name = 'شرکا'
        verbose_name_plural = 'شرکا'




class Resum_company(models.Model):

    title = models.CharField(max_length=100,verbose_name='متن')
    answer = models.TextField(verbose_name='جواب متن')
    ress = models.CharField(verbose_name='جواب متن',max_length=10,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )


    def __str__(self):
        return f'{self.title}'



    class Meta:
        verbose_name = 'رزومه شرکت'
        verbose_name_plural = 'رزومه های شرکت'




class Member_Company(models.Model):

    title = models.CharField(max_length=100,verbose_name='عنوان')
    who = models.CharField(max_length=100,verbose_name='سمت در شرکت')
    image_file = funcs.FileUpload('images','members')
    image_name = models.ImageField(verbose_name='ادرس عکس',upload_to=image_file.upload_to)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )


    def __str__(self):
        return  self.title


class SocialMedia(models.Model):

    member = models.ForeignKey(Member_Company,on_delete=models.CASCADE,verbose_name='عضو',related_name='member_social')
    icon = models.TextField(verbose_name='ایکون')
    link = models.TextField(verbose_name='لینک ادرس')



class ServiceList(models.Model):

    title = models.CharField(max_length=50,verbose_name='کلمه')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )


    def __str__(self):
        return f'{self.title}'


    class Meta:

        verbose_name = ' سرویس '
        verbose_name_plural = 'لیست سرویس ها در بنر'



def validate_image_or_svg(file):
    """
    Validator to check if the uploaded file is an image or an SVG.
    """
    ext = os.path.splitext(file.name)[1].lower()
    if ext == '.svg':
        return  # Valid SVG file
    try:
        img = Image.open(file)
        img.verify()
    except Exception as exc:
        raise ValidationError(
            _('Invalid file. Only images or SVGs are allowed.')
        ) from exc




class Plan(models.Model):


    title = models.CharField(max_length=100,verbose_name='موضوع پلن',blank=True,null=True)
    price = models.CharField(max_length=100,verbose_name='قیمت',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_org = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )

    image_file = funcs.FileUpload('images','service')
    image_name = models.FileField(
                upload_to=image_file.upload_to,
                verbose_name='نام فایل',
                blank=True,
                null=True,
                validators=[validate_image_or_svg]\
        )


    def __str__(self):
        return f'{self.title}\t\t{self.price}'


    class Meta:

        verbose_name = 'پلن پایه '
        verbose_name_plural = 'پلن پایه  ها'



class PlanItem(models.Model):

    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,verbose_name='پلن',related_name='plan_item')
    title = models.CharField(verbose_name='عنوان',max_length=100,null=True,blank=True)
    is_checked = models.BooleanField(default=True,verbose_name='check')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='تاریخ ثبت'
    )
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ اپدیت'
    )


    def __str__(self):
        return f'{self.title}'

