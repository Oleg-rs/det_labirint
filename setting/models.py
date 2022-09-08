from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Setting(models.Model):
    logo = models.ImageField(upload_to='setting/images/', verbose_name=u"Логотип")
    phone = models.CharField(max_length=200, verbose_name=u"Телефон")
    mail = models.CharField(max_length=200, verbose_name=u"Почта")
    opisanie = models.CharField(max_length=250, verbose_name=u"Слоган")
    zagolovok = models.CharField(max_length=250, verbose_name=u"Дополнительный слоган")

    def __str__(self):
        return self.zagolovok

    class Meta:
        verbose_name = 'Общие настройки'
        verbose_name_plural = 'Общие настройки'



class Katalog(models.Model):
    title = models.CharField(max_length=200, verbose_name=u"Название категории в каталоге")
    description = models.CharField(max_length=250, verbose_name=u"Описание")
    image = models.ImageField(upload_to='setting/images/', verbose_name=u"Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'


class Poryadok(models.Model):
    title = models.CharField(max_length=150, verbose_name=u"Название")
    image = models.ImageField(upload_to='setting/images/', verbose_name=u"Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'

class Banner(models.Model):
    banner = models.ImageField(upload_to='setting/images/', verbose_name=u"Баннер")
    description = models.CharField(max_length=250, verbose_name=u"Описание")
    pod_description = models.CharField(max_length=250, verbose_name=u"Дополнительное описание")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'


class Banner_2(models.Model):
    title = models.CharField(max_length=250,verbose_name=u"Заголовок")
    opisanie_1 = models.CharField(max_length=250,verbose_name=u"Первое описание")
    opisanie_2 = models.CharField(max_length=250,verbose_name=u"Второе описание")
    banner_2 = models.ImageField(upload_to='setting/images/',verbose_name=u"Баннер")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер - полный каталог'
        verbose_name_plural = 'Баннер - полный каталог'


class PreimVa(models.Model):
    image = models.ImageField(upload_to='setting/images/',verbose_name=u"Иконка")
    title = models.CharField(max_length=250, verbose_name=u"Заголовок")
    description = models.CharField(max_length=250, verbose_name=u"Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этапы работы'
        verbose_name_plural = 'Этапы работы'


class Primer(models.Model):
    image = models.ImageField(upload_to='setting/images/', verbose_name=u'Картинка')

    def __str__(self):
        a = 'Картинка'
        return a

    class Meta:
        verbose_name = 'Примеры работ'
        verbose_name_plural = 'Примеры работ'