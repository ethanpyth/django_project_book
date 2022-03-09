from django.contrib import admin
from django.db import models


# Create your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'apercu_contenu')
    list_filter = ('author', 'category')
    prepopulated_fields = {'slug': ('title', ), }
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('title', 'content')

    fieldsets = (
        ('Général', {
            'classes': ['collapse'],
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('contenu de l\'article', {
            'description': 'le formulaire accepte les balises HTML. utilisez les à bon escient',
            'fields': ('content', )
        })
    )

    def apercu_contenu(self, article):
        text = article.content[:40]
        if len(article.content) > 40:
            return '{}...'.format(text)
        else:
            return text

    apercu_contenu.short_description = 'Apercu du contenu'


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default=None)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Date de parution")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class Moteur(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Voiture(models.Model):
    name = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Products, through='Offre')

    def __str__(self):
        return self.name


class Offre(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "{0} vendu par {1}".format(self.product, self.seller)
