from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    score = models.DecimalField(default=0, decimal_places=1, max_digits=2,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0),
                                ]
                                )
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})


class Rating(models.Model):
    user = models.ForeignKey('accounts.User', verbose_name='Usuário', related_name='user')
    date = models.DateTimeField('Criado em', auto_now_add=True)
    comment = models.TextField('Comentário', blank=True)
    score = models.DecimalField(default=0, decimal_places=1, max_digits=2, validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ]
                                )
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', related_name='product')
