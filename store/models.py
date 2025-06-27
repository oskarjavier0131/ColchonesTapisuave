from django.db import models
from django.urls import reverse
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Descripción")
    image = models.ImageField(upload_to='categories/', blank=True, verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class MattressTechnology(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    benefits = models.TextField(verbose_name="Beneficios")
    
    class Meta:
        verbose_name = "Tecnología de Colchón"
        verbose_name_plural = "Tecnologías de Colchones"
    
    def __str__(self):
        return self.name

class Mattress(models.Model):
    FIRMNESS_CHOICES = [
        ('suave', 'Suave'),
        ('medio', 'Medio'),
        ('firme', 'Firme'),
        ('extra_firme', 'Extra Firme'),
    ]
    
    SIZE_CHOICES = [
        ('individual', 'Individual (90x190)'),
        ('semidoble', 'Semidoble (120x190)'),
        ('doble', 'Doble (140x190)'),
        ('queen', 'Queen (150x190)'),
        ('king', 'King (180x190)'),
        ('super_king', 'Super King (200x200)'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Nombre")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    technology = models.ForeignKey(MattressTechnology, on_delete=models.CASCADE, verbose_name="Tecnología")
    description = models.TextField(verbose_name="Descripción")
    short_description = models.CharField(max_length=300, verbose_name="Descripción corta")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, verbose_name="Tamaño")
    firmness = models.CharField(max_length=20, choices=FIRMNESS_CHOICES, verbose_name="Firmeza")
    thickness = models.PositiveIntegerField(verbose_name="Grosor (cm)")
    warranty_years = models.PositiveIntegerField(verbose_name="Años de garantía")
    main_image = models.ImageField(upload_to='mattresses/', verbose_name="Imagen principal")
    is_featured = models.BooleanField(default=False, verbose_name="Destacado")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Colchón"
        verbose_name_plural = "Colchones"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_size_display()}"
    
    def get_absolute_url(self):
        return reverse('mattress_detail', kwargs={'slug': self.slug})

class MattressImage(models.Model):
    mattress = models.ForeignKey(Mattress, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mattresses/gallery/', verbose_name="Imagen")
    alt_text = models.CharField(max_length=200, blank=True, verbose_name="Texto alternativo")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Imagen de Colchón"
        verbose_name_plural = "Imágenes de Colchones"
        ordering = ['order']
    
    def __str__(self):
        return f"Imagen {self.order} - {self.mattress.name}"

class HomeVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    video_file = models.FileField(upload_to='videos/', verbose_name="Archivo de video")
    thumbnail = models.ImageField(upload_to='video_thumbnails/', verbose_name="Miniatura")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Video del Inicio"
        verbose_name_plural = "Videos del Inicio"
        ordering = ['order']
    
    def __str__(self):
        return self.title

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de la empresa")
    slogan = models.CharField(max_length=300, verbose_name="Eslogan")
    description = models.TextField(verbose_name="Descripción")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Dirección")
    logo = models.ImageField(upload_to='company/', verbose_name="Logo")
    
    class Meta:
        verbose_name = "Información de la Empresa"
        verbose_name_plural = "Información de la Empresa"
    
    def __str__(self):
        return self.name
