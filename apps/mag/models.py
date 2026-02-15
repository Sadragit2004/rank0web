from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import funcs
from ckeditor_uploader.fields import RichTextUploadingField
import jdatetime
from django.contrib.postgres.search import SearchVectorField

# Create your models here.

class GroupMagModel(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    title = models.CharField(max_length=50,verbose_name='عنوان')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(verbose_name='تاریخ ثبت',default=timezone.now)
    update_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50,verbose_name='نامک')
    parent_group = models.ForeignKey('GroupMagModel',on_delete=models.CASCADE,verbose_name='والد گروه',related_name='parent_of_group',null=True,blank=True)
    file_upload = funcs.FileUpload('Mag','group')
    image_name = models.ImageField(upload_to=file_upload.upload_to,verbose_name='تصویر',default='')

    def __str__(self):
        return f'{self.title}'


    class Meta:
        verbose_name = 'گروه مگ'
        verbose_name_plural = 'گروه های مگ'




class MetaTagModelGroup(models.Model):
    """
    Model for meta tags for the blog.
    """
    group = models.ForeignKey(GroupMagModel, on_delete=models.CASCADE, verbose_name='متا تگ', blank=True, null=True,related_name='meta_tag_blog')
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
        return f'{self.page_title}'



    class Meta:
        verbose_name = 'متا تگ'
        verbose_name_plural = 'متا تگ های گروه ها'




class AuthorMagModel(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    full_name = models.CharField(max_length=50,verbose_name='نام کامل')
    file_upload = funcs.FileUpload('Mag','Author')
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True,null=True)
    image_name = models.ImageField(upload_to=file_upload.upload_to,verbose_name='تصویر')
    gmail = models.EmailField(verbose_name='ایمیل',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(verbose_name='تاریخ ثبت',default=timezone.now)
    update_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50,verbose_name='نامک')


    def __str__(self):
        return f'{self.full_name}'






class SocialMediaAuthor(models.Model):
    """ Model to store social media links. """
    Author = models.ForeignKey(AuthorMagModel,on_delete=models.CASCADE,verbose_name='نویسنده',related_name='socialmediaauthor')
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





# Add a SearchVectorField to your models


class MagManager(models.Manager):
    def search_mag(self, query):
        return self.extra(
            where=["MATCH(title, summery_text) AGAINST (%s IN NATURAL LANGUAGE MODE)"],
            params=[query]
        )

class Mag(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')
    subject = models.CharField(max_length=100,verbose_name='عنوان فرعی',blank=True,null=True)
    summery_text = models.TextField(verbose_name='متن خلاصه')
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    create_at = models.DateTimeField(default=timezone.now,verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(verbose_name='اپدیت شده',auto_now_add=True)
    group = models.ForeignKey(GroupMagModel,on_delete=models.CASCADE,verbose_name='گروه', related_name='magazines',blank=True,null=True)
    author = models.ForeignKey(AuthorMagModel,on_delete=models.CASCADE,verbose_name='نویسنده',blank=True,null=True)
    time_read = models.CharField(max_length=100,verbose_name='تایم مطالعه')
    view = models.PositiveIntegerField()
    slug = models.CharField(max_length=50,verbose_name='نامک')
    file_upload = funcs.FileUpload('Mag','Author')
    image_name = models.ImageField(upload_to=file_upload.upload_to,verbose_name='تصویر')
    file_upload_audio = funcs.FileUpload("audio",'sound_blog')
    audio = models.FileField(upload_to = file_upload_audio.upload_to,verbose_name = 'صوتی',blank = True,null = True)
    description_audio = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True,null = True)
    objects = MagManager()
    
    
    
    def __str__(self):
        return f'{self.title}'




# Meta tag model for blog
class MetaTagModel(models.Model):
    """
    Model for meta tags for the blog.
    """
    blog = models.ForeignKey(Mag, on_delete=models.CASCADE, verbose_name='متا تگ', blank=True, null=True)
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
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)





# FAQ
class FAQ(models.Model):
    """
    Model for frequently asked questions related to a blog post.
    """
    mag = models.ForeignKey(Mag, on_delete=models.CASCADE, verbose_name='وبلاگ', related_name='mag_faqs', null=True, blank=True)
    question = models.CharField(max_length=300, verbose_name='سوال', null=True, blank=True)
    answer = models.TextField(verbose_name='جواب', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='وضعیت', default=True)
    register_date = models.DateTimeField(default=timezone.now(), verbose_name='تاریخ ثبت', null=True, blank=True)

    def __str__(self):
        return f'{self.question}'

    class Meta:
        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات'





class LableBlog(models.Model):
    """
    Model for blog labels.
    """
    title = models.CharField(max_length=30, verbose_name='برچسب')
    mag = models.ForeignKey(Mag, on_delete=models.CASCADE, verbose_name='مقالات', related_name='mag_lable', null=True, blank=True)
    link = models.TextField(verbose_name='لینک')

    def __str__(self):
        return f'{self.title}'




    def time_since_posted(self):
        """
        Returns the time elapsed since the blog post was created.
        """
        now = timezone.now()
        diff = now - self.create_at
        if diff.days == 0 and diff.seconds < 60:
            return 'چند لحظه پیش'
        if diff.days == 0 and diff.seconds < 3600:
            minutes = diff.seconds // 60
            return f'{minutes} دقیقه پیش'
        if diff.days == 0 and diff.seconds < 86400:
            hours = diff.seconds // 3600
            return f'{hours} ساعت پیش'
        if diff.days < 30:
            return f'{diff.days} روز پیش'
        if diff.days < 365:
            months = diff.days // 30
            return f'{months} ماه پیش'
        years = diff.days // 365
        return f'{years} سال پیش'

    def get_jalali_register_date(self):
        """
        Returns the Jalali (Persian) date of the blog post.
        """
        return jdatetime.datetime.fromgregorian(datetime=self.create_at).strftime('%Y/%m/%d')



    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'مگ'
        verbose_name_plural = 'مگ ها'


class MagMainSlider(models.Model):

    title = models.CharField(max_length=100,verbose_name='عنوان')
    description = RichTextUploadingField(verbose_name='توضیحات', config_name='special', blank=True)
    file_upload = funcs.FileUpload('Mag','slider')
    image_name = models.ImageField(upload_to=file_upload.upload_to,verbose_name='تصویر')
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    create_at = models.DateTimeField(default=timezone.now,verbose_name='تاریخ ثبت')
    update_at = models.DateTimeField(verbose_name='اپدیت شده',default=timezone.now)


    def __str__(self):
        return f'{self.title}'


    class Meta:
        verbose_name = 'صفحه بنر'
        verbose_name_plural = 'بنر ها'


class Comment(models.Model):
    mag = models.ForeignKey(Mag, on_delete=models.CASCADE, related_name="comments", verbose_name="مجله")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies", verbose_name="پاسخ به")
    author = models.CharField(max_length=100, verbose_name="نام نویسنده", null=True, blank=True,)
    email = models.EmailField(verbose_name="ایمیل", null=True, blank=True,)
    text = models.TextField(verbose_name="متن نظر", null=True, blank=True,)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ثبت")
    is_active = models.BooleanField(default=False,verbose_name='فعال')

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author} - {self.text[:30]}"






class main_tag_mag(models.Model):
    """
    Model for meta tags for the blog.
    """
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
