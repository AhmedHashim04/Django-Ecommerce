from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.db.models import Avg


class Product(models.Model):
    name = models.CharField(max_length=40, verbose_name=_("Name"))
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name=_("Category"), blank=True, null=True)
    brand = models.ForeignKey('settings.Brand', on_delete=models.PROTECT, verbose_name=_("Brand"), blank=True, null=True)
    description = models.TextField(max_length=1000, verbose_name=_("Description"))
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Price"))
    cost = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=_("Cost"))
    created_at = models.DateTimeField(auto_now=True, verbose_name=_("Created At"))
    image = models.ImageField(upload_to='products/', verbose_name=_("Product Image"), blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    viewed_by = models.ManyToManyField("account.Profile", verbose_name=_("Viewed By"), related_name="viewed_products", blank=True)
    tags = TaggableManager(verbose_name=_("Tags"))
    stock = models.PositiveIntegerField(default=0, verbose_name=_("Stock"))
    overall_rating = models.FloatField(default=0.0, verbose_name=_("Overall Rating"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})

    def update_overall_rating(self):
        reviews = self.product_review.all()
        if reviews.exists():
            self.overall_rating = round(reviews.aggregate(Avg('rating'))['rating__avg'], 2)
        else:
            self.overall_rating = 0
        self.save()

    def is_in_stock(self):
        return self.stock > 0

    @staticmethod
    def calculate_overall_rating(reviews):
        if not reviews.exists():
            return 0
        total_rating = sum(review.rating for review in reviews)
        return total_rating / reviews.count()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    parent = models.ForeignKey('self', limit_choices_to={'parent__isnull': True}, on_delete=models.CASCADE, verbose_name=_("Parent Category"), blank=True, null=True)
    description = models.TextField(max_length=1000, verbose_name=_("Description"))
    image = models.ImageField(upload_to='category_pictures/', verbose_name=_("Image"), blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'slug': self.slug})


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_review", verbose_name=_("Product"))
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_review", verbose_name=_("User"))
    content = models.TextField(max_length=1000, verbose_name=_("Review"))
    rating = models.IntegerField(choices=RATING_CHOICES, default=3, verbose_name=_("Rating"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f"{self.user.username}'s review of {self.product.name}"
