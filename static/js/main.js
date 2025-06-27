// Main JavaScript for Colchones TapiSuave
document.addEventListener('DOMContentLoaded', function() {
    // WhatsApp Widget Functionality
    const whatsappBtn = document.getElementById('whatsapp-btn');
    const whatsappWidget = document.getElementById('whatsapp-widget');
    const closeChat = document.getElementById('close-chat');
    const chatInput = document.getElementById('chat-input');
    const sendMessage = document.getElementById('send-message');
    const chatMessages = document.getElementById('chat-messages');

    // AI Agent responses
    const botResponses = {
        'hola': '¡Hola! Bienvenido a Colchones TapiSuave. ¿En qué puedo ayudarte hoy? Puedo ayudarte con información sobre nuestros colchones, precios, garantías y más.',
        'colchones': 'Tenemos una amplia variedad de colchones: Ortopédicos, Memory Foam, Resortes Independientes, Látex Natural, y más. ¿Qué tipo te interesa?',
        'precios': 'Nuestros precios varían según el tamaño y tecnología. Van desde $300.000 para individuales hasta $2.500.000 para Super King con tecnología avanzada. ¿Qué tamaño necesitas?',
        'garantia': 'Todos nuestros colchones tienen garantía extendida de hasta 10 años. También ofrecemos 30 días de prueba en casa.',
        'envio': 'Ofrecemos envío GRATIS a toda Colombia en compras superiores a $500.000. El tiempo de entrega es de 2-5 días hábiles.',
        'tamaños': 'Manejamos todos los tamaños estándar: Individual (90x190), Semidoble (120x190), Doble (140x190), Queen (150x190), King (180x190), y Super King (200x200).',
        'tecnologia': 'Contamos con tecnologías avanzadas como Memory Foam, Gel Cooling, Resortes Independientes, Látex Natural, y sistemas de ventilación. ¿Cuál te interesa más?',
        'firmeza': 'Tenemos colchones en diferentes niveles de firmeza: Suave, Medio, Firme, y Extra Firme. Te ayudo a elegir según tu posición de dormir.',
        'catalogo': 'Puedes descargar nuestro catálogo completo desde la página principal o ver todos los productos en nuestra sección de catálogo.',
        'contacto': 'Puedes contactarnos por WhatsApp al +57 311 2474802, por email a info@tapisuave.com, o visitarnos en Bogotá.',
        'default': 'Gracias por tu consulta. Nuestro equipo especializado puede ayudarte mejor. ¿Te gustaría que te conecte con un asesor humano?'
    };

    // Show WhatsApp widget
    whatsappBtn.addEventListener('click', function(e) {
        e.preventDefault();
        whatsappWidget.style.display = 'block';
    });

    // Close WhatsApp widget
    closeChat.addEventListener('click', function() {
        whatsappWidget.style.display = 'none';
    });

    // Send message functionality
    function sendChatMessage() {
        const message = chatInput.value.trim();
        if (message === '') return;

        // Add user message
        addMessage(message, 'user');
        chatInput.value = '';

        // Simulate typing indicator
        addTypingIndicator();

        // Generate bot response
        setTimeout(() => {
            removeTypingIndicator();
            const response = generateBotResponse(message);
            addMessage(response, 'bot');
        }, 1500);
    }

    sendMessage.addEventListener('click', sendChatMessage);
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendChatMessage();
        }
    });

    // Add message to chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${sender === 'user' ? 'user-message' : 'bot-message'}`;
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Add typing indicator
    function addTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'chat-message bot-message typing-indicator';
        typingDiv.innerHTML = 'Escribiendo... <div class="loading-spinner"></div>';
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = chatMessages.querySelector('.typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    // Generate bot response
    function generateBotResponse(userMessage) {
        const message = userMessage.toLowerCase();
        
        // Check for keywords in user message
        for (const [keyword, response] of Object.entries(botResponses)) {
            if (keyword !== 'default' && message.includes(keyword)) {
                return response;
            }
        }
        
        // Special cases
        if (message.includes('ayuda') || message.includes('help')) {
            return 'Estoy aquí para ayudarte. Puedo responder sobre: colchones, precios, garantía, envío, tamaños, tecnología, firmeza, catálogo, y contacto. ¿Qué te interesa saber?';
        }
        
        if (message.includes('gracias')) {
            return '¡De nada! Estoy aquí para ayudarte las 24 horas. ¿Hay algo más en lo que pueda asistirte?';
        }
        
        if (message.includes('adiós') || message.includes('bye')) {
            return '¡Hasta pronto! No dudes en contactarnos cuando necesites. ¡Que tengas un excelente descanso!';
        }
        
        return botResponses.default;
    }

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add scroll effect to navbar
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.elegant-nav');
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(44, 62, 80, 0.98)';
        } else {
            navbar.style.background = 'rgba(44, 62, 80, 0.95)';
        }
    });

    // Lazy loading for images
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // Add animation to elements when they come into view
    const animatedElements = document.querySelectorAll('.category-card, .product-card, .feature-icon');
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, {
        threshold: 0.1
    });

    animatedElements.forEach(el => animationObserver.observe(el));

    // Product filtering (for catalog page)
    const filterButtons = document.querySelectorAll('.btn-filter');
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Filter logic would go here
            const filterValue = this.dataset.filter;
            filterProducts(filterValue);
        });
    });

    function filterProducts(filterValue) {
        const products = document.querySelectorAll('.product-card');
        products.forEach(product => {
            if (filterValue === 'all' || product.dataset.category === filterValue) {
                product.style.display = 'block';
                product.classList.add('fade-in');
            } else {
                product.style.display = 'none';
            }
        });
    }

    // Auto-hide WhatsApp widget after inactivity
    let chatTimeout;
    function resetChatTimeout() {
        clearTimeout(chatTimeout);
        chatTimeout = setTimeout(() => {
            if (whatsappWidget.style.display === 'block') {
                addMessage('¿Sigues ahí? Si necesitas más ayuda, no dudes en escribir. Estaré aquí cuando me necesites.', 'bot');
            }
        }, 300000); // 5 minutes
    }

    // Reset timeout on any chat activity
    chatInput.addEventListener('input', resetChatTimeout);
    sendMessage.addEventListener('click', resetChatTimeout);

    // Initialize chat timeout
    resetChatTimeout();
});