from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField('Title', max_length=128)
    description = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    auct = models.BooleanField('Auction', help_text='Mark, if auction is available')
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/', null=True, blank=True)

    @admin.display(description='Created at')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue">Today at {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description='Updated at')
    def updated_date(self):
        if self.created_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue">Today at {}</span>', updated_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description='Image')
    def get_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
                )

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
