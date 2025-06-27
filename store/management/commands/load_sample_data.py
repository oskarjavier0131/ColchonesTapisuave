from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category, MattressTechnology, Mattress, CompanyInfo
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load sample data for the mattress store'

    def handle(self, *args, **options):
        # Create Company Info
        company_info, created = CompanyInfo.objects.get_or_create(
            name="Tapi Suave",
            defaults={
                'slogan': 'Tu descanso perfecto nos importa',
                'description': 'Somos especialistas en colchones de la más alta calidad. Con más de 20 años de experiencia, ofrecemos productos con tecnología de punta para garantizar el mejor descanso.',
                'phone': '+57 300 123 4567',
                'whatsapp': '+57 300 123 4567',
                'email': 'info@tapisuave.com',
                'address': 'Carrera 7 #32-16, Bogotá, Colombia'
            }
        )

        # Create Technologies
        technologies_data = [
            {
                'name': 'Memory Foam',
                'description': 'Espuma viscoelástica que se adapta perfectamente al contorno del cuerpo.',
                'benefits': 'Reduce puntos de presión, mejora la circulación, alivio del dolor de espalda.'
            },
            {
                'name': 'Resortes Independientes',
                'description': 'Sistema de resortes encapsulados individualmente para mayor soporte.',
                'benefits': 'Soporte diferenciado, reduce transferencia de movimiento, mayor durabilidad.'
            },
            {
                'name': 'Látex Natural',
                'description': 'Material natural extraído del árbol de caucho, hipoalergénico.',
                'benefits': 'Antibacterial, transpirable, ecológico, resistente a ácaros.'
            },
            {
                'name': 'Gel Cooling',
                'description': 'Tecnología de gel que regula la temperatura corporal.',
                'benefits': 'Mantiene frescura, reduce calor corporal, ideal para climas cálidos.'
            },
            {
                'name': 'Híbrido',
                'description': 'Combinación de diferentes tecnologías para máximo confort.',
                'benefits': 'Versatilidad, adaptabilidad, combina beneficios múltiples.'
            }
        ]

        technologies = {}
        for tech_data in technologies_data:
            tech, created = MattressTechnology.objects.get_or_create(
                name=tech_data['name'],
                defaults={
                    'description': tech_data['description'],
                    'benefits': tech_data['benefits']
                }
            )
            technologies[tech_data['name']] = tech

        # Create Categories
        categories_data = [
            {
                'name': 'Ortopédicos',
                'description': 'colchones especialmente diseñados para el cuidado de la columna vertebral y articulaciones.'
            },
            {
                'name': 'Memory Foam',
                'description': 'Colchones con espuma viscoelástica que se adapta a tu cuerpo.'
            },
            {
                'name': 'Resortes',
                'description': 'Colchones tradicionales con sistema de resortes para mayor soporte.'
            },
            {
                'name': 'Ecológicos',
                'description': 'Colchones fabricados con materiales naturales y sostenibles.'
            },
            {
                'name': 'Premium',
                'description': 'Nuestra línea de colchones de lujo con tecnología avanzada.'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'slug': slugify(cat_data['name']),
                    'description': cat_data['description']
                }
            )
            categories[cat_data['name']] = cat

        # Create Sample Mattresses
        mattresses_data = [
            {
                'name': 'Ortopédico Classic',
                'category': 'Ortopédicos',
                'technology': 'Resortes Independientes',
                'description': 'Colchón ortopédico tradicional con excelente soporte para la columna vertebral.',
                'short_description': 'Soporte firme y duradero para el cuidado de tu espalda.',
                'price': Decimal('450000'),
                'size': 'doble',
                'firmness': 'firme',
                'thickness': 20,
                'warranty_years': 5,
                'is_featured': True
            },
            {
                'name': 'Memory Dream',
                'category': 'Memory Foam',
                'technology': 'Memory Foam',
                'description': 'Colchón de espuma viscoelástica que se adapta perfectamente a las curvas de tu cuerpo.',
                'short_description': 'Máximo confort con tecnología de espuma de memoria.',
                'price': Decimal('680000'),
                'size': 'queen',
                'firmness': 'medio',
                'thickness': 25,
                'warranty_years': 8,
                'is_featured': True
            },
            {
                'name': 'Eco Natural',
                'category': 'Ecológicos',
                'technology': 'Látex Natural',
                'description': 'Colchón 100% natural fabricado con látex extraído de árboles de caucho.',
                'short_description': 'Colchón ecológico y saludable para toda la familia.',
                'price': Decimal('890000'),
                'size': 'king',
                'firmness': 'medio',
                'thickness': 22,
                'warranty_years': 10,
                'is_featured': True
            },
            {
                'name': 'Cool Gel Pro',
                'category': 'Premium',
                'technology': 'Gel Cooling',
                'description': 'Colchón premium con tecnología de gel para mantener la temperatura ideal.',
                'short_description': 'Frescura y confort durante toda la noche.',
                'price': Decimal('1200000'),
                'size': 'king',
                'firmness': 'medio',
                'thickness': 30,
                'warranty_years': 10,
                'is_featured': True
            },
            {
                'name': 'Hybrid Comfort',
                'category': 'Premium',
                'technology': 'Híbrido',
                'description': 'Colchón híbrido que combina lo mejor de diferentes tecnologías.',
                'short_description': 'La perfecta combinación de soporte y confort.',
                'price': Decimal('950000'),
                'size': 'queen',
                'firmness': 'medio',
                'thickness': 28,
                'warranty_years': 8,
                'is_featured': True
            },
            {
                'name': 'Resorte Tradicional',
                'category': 'Resortes',
                'technology': 'Resortes Independientes',
                'description': 'Colchón tradicional de resortes con excelente ventilación.',
                'short_description': 'Calidad tradicional con tecnología moderna.',
                'price': Decimal('380000'),
                'size': 'semidoble',
                'firmness': 'firme',
                'thickness': 18,
                'warranty_years': 5,
                'is_featured': False
            }
        ]

        for mattress_data in mattresses_data:
            mattress, created = Mattress.objects.get_or_create(
                name=mattress_data['name'],
                defaults={
                    'slug': slugify(mattress_data['name']),
                    'category': categories[mattress_data['category']],
                    'technology': technologies[mattress_data['technology']],
                    'description': mattress_data['description'],
                    'short_description': mattress_data['short_description'],
                    'price': mattress_data['price'],
                    'size': mattress_data['size'],
                    'firmness': mattress_data['firmness'],
                    'thickness': mattress_data['thickness'],
                    'warranty_years': mattress_data['warranty_years'],
                    'is_featured': mattress_data['is_featured']
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data for the mattress store!')
        )