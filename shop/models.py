from django.db import models


class Category(models.Model):
    name        = models.CharField(max_length=200, verbose_name="Назва")
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Опис")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at  = models.DateTimeField(auto_now=True,     verbose_name="Оновлено о")

    class Meta:
        verbose_name        = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Product(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    related_name='products', verbose_name="Категорія")
    name        = models.CharField(max_length=300,  verbose_name="Назва")
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True,      verbose_name="Опис")
    price       = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image       = models.ImageField(upload_to='products/', blank=True, verbose_name="Фото")
    in_stock    = models.BooleanField(default=True,  verbose_name="В наявності")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at  = models.DateTimeField(auto_now=True,     verbose_name="Оновлено о")

    class Meta:
        verbose_name        = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Очікує'),
        ('confirmed', 'Підтверджено'),
        ('shipped',   'Відправлено'),
        ('delivered', 'Доставлено'),
    ]
    customer_name  = models.CharField(max_length=200, verbose_name="Ім'я клієнта")
    customer_email = models.EmailField(verbose_name="Email")
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES,
                                      default='pending', verbose_name="Статус")
    created_at     = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at     = models.DateTimeField(auto_now=True,     verbose_name="Оновлено о")

    class Meta:
        verbose_name        = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення #{self.pk} — {self.customer_name}"