from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'central_agentes_secretos_2024_ultra_secreto')
CORS(app)  # Permitir CORS para interações frontend-backend

# Base de dados simples de agentes (em produção, use um banco de dados real)
AGENTES = {
    'agente_falcao': {
        'password': 'falcao123',
        'nome_completo': 'Agente Falcão',
        'nivel_acesso': 'Alpha',
        'especialidade': 'Operações Especiais',
        'status': 'Ativo'
    },
    'agente_sombra': {
        'password': 'sombra456',
        'nome_completo': 'Agente Sombra',
        'nivel_acesso': 'Beta',
        'especialidade': 'Infiltração',
        'status': 'Ativo'
    },
    'agente_raio': {
        'password': 'raio789',
        'nome_completo': 'Agente Raio',
        'nivel_acesso': 'Alpha',
        'especialidade': 'Tecnologia',
        'status': 'Ativo'
    },
    'agente_fenix': {
        'password': 'fenix321',
        'nome_completo': 'Agente Fênix',
        'nivel_acesso': 'Gamma',
        'especialidade': 'Análise',
        'status': 'Ativo'
    }
}

# Armazenamento temporário de mensagens (em produção, use um banco de dados)
MENSAGENS = []
AVISOS = [
    {
        'titulo': 'Operação Tempestade - Concluída',
        'conteudo': 'A operação foi finalizada com sucesso. Todos os agentes envolvidos retornaram à base.',
        'data': '2024-01-15 14:30',
        'prioridade': 'alta'
    },
    {
        'titulo': 'Novo Protocolo de Segurança',
        'conteudo': 'Implementado novo sistema de autenticação dupla. Todos os agentes devem atualizar suas credenciais.',
        'data': '2024-01-14 09:15',
        'prioridade': 'media'
    },
    {
        'titulo': 'Reunião Semanal',
        'conteudo': 'Briefing semanal agendado para sexta-feira às 16:00 na sala de operações.',
        'data': '2024-01-13 11:00',
        'prioridade': 'baixa'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        
        # Verificar credenciais
        if username in AGENTES and AGENTES[username]['password'] == password:
            session['logged_in'] = True
            session['username'] = username
            session['nome_completo'] = AGENTES[username]['nome_completo']
            session['nivel_acesso'] = AGENTES[username]['nivel_acesso']
            session['especialidade'] = AGENTES[username]['especialidade']
            session['login_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            flash(f'Bem-vindo, {AGENTES[username]["nome_completo"]}!', 'success')
            return redirect(url_for('painel_secreto'))
        else:
            flash('Credenciais inválidas. Acesso negado.', 'error')
            return render_template('login.html', error=True)
    
    return render_template('login.html')

@app.route('/painel_secreto')
def painel_secreto():
    if not session.get('logged_in'):
        flash('Acesso restrito. Faça login primeiro.', 'warning')
        return redirect(url_for('login'))
    
    # Dados do agente atual
    agente_data = {
        'username': session['username'],
        'nome_completo': session['nome_completo'],
        'nivel_acesso': session['nivel_acesso'],
        'especialidade': session['especialidade'],
        'login_time': session['login_time']
    }
    
    return render_template('painel_secreto.html', 
                         agente=agente_data, 
                         avisos=AVISOS, 
                         mensagens=MENSAGENS[-10:])  # Últimas 10 mensagens

@app.route('/api/mensagens', methods=['GET', 'POST'])
def api_mensagens():
    if not session.get('logged_in'):
        return jsonify({'error': 'Não autorizado'}), 401
    
    if request.method == 'POST':
        data = request.get_json()
        mensagem = {
            'autor': session['nome_completo'],
            'conteudo': data['mensagem'],
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'data': datetime.now().strftime('%Y-%m-%d')
        }
        MENSAGENS.append(mensagem)
        return jsonify({'success': True, 'mensagem': mensagem})
    
    return jsonify({'mensagens': MENSAGENS[-20:]})  # Últimas 20 mensagens

@app.route('/api/agentes_online')
def api_agentes_online():
    if not session.get('logged_in'):
        return jsonify({'error': 'Não autorizado'}), 401
    
    # Simular agentes online (em produção, implementar lógica real)
    agentes_online = [
        {'nome': 'Agente Falcão', 'status': 'online'},
        {'nome': 'Agente Sombra', 'status': 'ausente'},
        {'nome': 'Agente Raio', 'status': 'online'},
        {'nome': 'Agente Fênix', 'status': 'ocupado'}
    ]
    
    return jsonify({'agentes': agentes_online})

@app.route('/logout')
def logout():
    nome = session.get('nome_completo', 'Agente')
    session.clear()
    flash(f'Logout realizado com sucesso. Até logo, {nome}!', 'info')
    return redirect(url_for('index'))

# Função para verificar se o usuário está logado
def login_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# Rota para adicionar novos avisos (apenas para demonstração)
@app.route('/admin/adicionar_aviso', methods=['POST'])
@login_required
def adicionar_aviso():
    if session.get('nivel_acesso') != 'Alpha':
        flash('Acesso negado. Apenas agentes Alpha podem adicionar avisos.', 'error')
        return redirect(url_for('painel_secreto'))
    
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']
    prioridade = request.form['prioridade']
    
    novo_aviso = {
        'titulo': titulo,
        'conteudo': conteudo,
        'data': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'prioridade': prioridade
    }
    
    AVISOS.insert(0, novo_aviso)  # Adicionar no início da lista
    flash('Aviso adicionado com sucesso!', 'success')
    return redirect(url_for('painel_secreto'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


