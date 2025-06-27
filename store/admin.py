from django.contrib import admin
from .models import Category, MattressTechnology, Mattress, MattressImage, HomeVideo, CompanyInfo

class MattressImageInline(admin.TabularInline):
    model = MattressImage
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(MattressTechnology)
class MattressTechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Mattress)
class MattressAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'size', 'price', 'is_featured', 'is_active']
    list_filter = ['category', 'technology', 'size', 'firmness', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MattressImageInline]
    list_editable = ['is_featured', 'is_active']

@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order', 'created_at']
    list_filter = ['is_active']
    list_editable = ['is_active', 'order']

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
