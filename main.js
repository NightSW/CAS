// Central de Agentes Secretos - JavaScript Principal

document.addEventListener('DOMContentLoaded', function() {
    // Efeitos visuais gerais
    initializeEffects();
    
    // Inicializar funcionalidades específicas da página
    if (document.getElementById('chat-messages')) {
        initializeChat();
    }
    
    if (document.getElementById('notice-board')) {
        initializeNoticeBoard();
    }
});

function initializeEffects() {
    // Efeito de hover nos cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Efeito de clique nos botões
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Efeito de ripple
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
}

function initializeChat() {
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-button');
    
    // Mensagens de exemplo
    const exampleMessages = [
        { author: 'Agente Falcão', message: 'Missão Alpha concluída com sucesso. Aguardando próximas instruções.', time: '14:30' },
        { author: 'Agente Sombra', message: 'Detectada atividade suspeita no setor 7. Investigando.', time: '14:45' },
        { author: 'Central', message: 'Todos os agentes: reunião de briefing às 16:00.', time: '15:00' }
    ];
    
    // Carregar mensagens de exemplo
    exampleMessages.forEach(msg => {
        addMessage(msg.author, msg.message, msg.time);
    });
    
    // Enviar mensagem
    function sendMessage() {
        const message = chatInput.value.trim();
        if (message) {
            const currentTime = new Date().toLocaleTimeString('pt-BR', { 
                hour: '2-digit', 
                minute: '2-digit' 
            });
            const username = document.querySelector('.welcome-message h1').textContent.split(' ')[2] || 'Agente';
            
            addMessage(username, message, currentTime);
            chatInput.value = '';
            
            // Simular resposta automática (opcional)
            setTimeout(() => {
                addMessage('Central', 'Mensagem recebida e registrada. ✓', currentTime);
            }, 1000);
        }
    }
    
    function addMessage(author, message, time) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message';
        messageDiv.innerHTML = `
            <div class="message-author">${author} - ${time}</div>
            <div class="message-content">${message}</div>
        `;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Event listeners
    if (sendButton) {
        sendButton.addEventListener('click', sendMessage);
    }
    
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
}

function initializeNoticeBoard() {
    // Adicionar efeito de fade-in para avisos
    const notices = document.querySelectorAll('.notice-item');
    notices.forEach((notice, index) => {
        notice.style.opacity = '0';
        notice.style.transform = 'translateX(-20px)';
        
        setTimeout(() => {
            notice.style.transition = 'all 0.5s ease';
            notice.style.opacity = '1';
            notice.style.transform = 'translateX(0)';
        }, index * 200);
    });
}

// Função para atualizar status em tempo real
function updateSystemStatus() {
    const statusElements = document.querySelectorAll('.status-indicator');
    statusElements.forEach(element => {
        element.style.animation = 'pulse 2s infinite';
    });
}

// Função para simular atividade de rede
function simulateNetworkActivity() {
    const networkStatus = document.getElementById('network-status');
    if (networkStatus) {
        setInterval(() => {
            networkStatus.style.color = '#27ae60';
            setTimeout(() => {
                networkStatus.style.color = '#3498db';
            }, 500);
        }, 3000);
    }
}

// CSS para efeito ripple (adicionado dinamicamente)
const style = document.createElement('style');
style.textContent = `
    .btn {
        position: relative;
        overflow: hidden;
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
`;
document.head.appendChild(style);

// Inicializar funcionalidades adicionais
updateSystemStatus();
simulateNetworkActivity();

