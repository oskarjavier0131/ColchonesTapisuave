from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Category, Mattress, HomeVideo, CompanyInfo
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def home(request):
    featured_mattresses = Mattress.objects.filter(is_featured=True, is_active=True)[:6]
    categories = Category.objects.all()
    videos = HomeVideo.objects.filter(is_active=True)
    try:
        company_info = CompanyInfo.objects.first()
    except CompanyInfo.DoesNotExist:
        company_info = None
    
    context = {
        'featured_mattresses': featured_mattresses,
        'categories': categories,
        'videos': videos,
        'company_info': company_info,
    }
    return render(request, 'store/home.html', context)

def catalog(request):
    mattresses = Mattress.objects.filter(is_active=True)
    categories = Category.objects.all()
    
    category_filter = request.GET.get('category')
    if category_filter:
        mattresses = mattresses.filter(category__slug=category_filter)
    
    size_filter = request.GET.get('size')
    if size_filter:
        mattresses = mattresses.filter(size=size_filter)
    
    firmness_filter = request.GET.get('firmness')
    if firmness_filter:
        mattresses = mattresses.filter(firmness=firmness_filter)
    
    context = {
        'mattresses': mattresses,
        'categories': categories,
        'selected_category': category_filter,
        'selected_size': size_filter,
        'selected_firmness': firmness_filter,
    }
    return render(request, 'store/catalog.html', context)

def mattress_detail(request, slug):
    mattress = get_object_or_404(Mattress, slug=slug, is_active=True)
    related_mattresses = Mattress.objects.filter(
        category=mattress.category, 
        is_active=True
    ).exclude(id=mattress.id)[:4]
    
    context = {
        'mattress': mattress,
        'related_mattresses': related_mattresses,
    }
    return render(request, 'store/mattress_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    mattresses = Mattress.objects.filter(category=category, is_active=True)
    
    context = {
        'category': category,
        'mattresses': mattresses,
    }
    return render(request, 'store/category_detail.html', context)

def download_catalog(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="catalogo_colchones.pdf"'
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    mattresses = Mattress.objects.filter(is_active=True)
    
    y = 750
    p.drawString(50, y, "Catálogo de Colchones")
    y -= 40
    
    for mattress in mattresses:
        if y < 100:
            p.showPage()
            y = 750
        
        p.drawString(50, y, f"Nombre: {mattress.name}")
        y -= 20
        p.drawString(50, y, f"Categoría: {mattress.category.name}")
        y -= 20
        p.drawString(50, y, f"Precio: ${mattress.price}")
        y -= 20
        p.drawString(50, y, f"Tamaño: {mattress.get_size_display()}")
        y -= 30
    
    p.showPage()
    p.save()
    
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response
