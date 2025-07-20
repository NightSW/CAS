# 🕵️ Central de Operações Secretas

Um site privado e secreto no estilo de uma central de agentes, desenvolvido para você e seus amigos se divertirem como agentes secretos!

## 🎯 Características Principais

- **🔐 Sistema de Login Seguro**: Acesso restrito apenas para agentes autorizados
- **🎨 Design Temático**: Visual escuro/moderno com elementos de espionagem
- **👥 Múltiplos Agentes**: Sistema suporta vários usuários com diferentes níveis de acesso
- **📢 Mural de Avisos**: Central de comunicados secretos
- **💬 Chat em Tempo Real**: Sistema de mensagens entre agentes
- **📊 Painel de Controle**: Interface completa com informações do agente
- **🛡️ Níveis de Segurança**: Sistema de clearance (Alpha, Beta, Gamma)

## 🚀 Tecnologias Utilizadas

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilo**: Design responsivo com tema de espionagem
- **Segurança**: Sistema de sessões Flask

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação Local

1. **Clone ou baixe o projeto**
   ```bash
   # Se usando git
   git clone [URL_DO_REPOSITORIO]
   cd central_agentes_secretos
   
   # Ou extraia o arquivo ZIP baixado
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o servidor**
   ```bash
   python app.py
   ```

4. **Acesse o site**
   - Abra seu navegador
   - Vá para: `http://localhost:5000`

## 👤 Agentes de Demonstração

O sistema vem com 4 agentes pré-configurados para teste:

| Agente | Usuário | Senha | Nível | Especialidade |
|--------|---------|-------|-------|---------------|
| 🦅 Agente Falcão | `agente_falcao` | `falcao123` | Alpha | Operações Especiais |
| 🌙 Agente Sombra | `agente_sombra` | `sombra456` | Beta | Infiltração |
| ⚡ Agente Raio | `agente_raio` | `raio789` | Alpha | Tecnologia |
| 🔥 Agente Fênix | `agente_fenix` | `fenix321` | Gamma | Análise |

## 🎮 Como Usar

### 1. Acesso Inicial
- Acesse a página inicial
- Clique em "ACESSO DE AGENTE"
- Use uma das credenciais de demonstração

### 2. Painel Secreto
Após o login, você terá acesso a:
- **Informações do Agente**: Seu perfil e estatísticas
- **Mural de Avisos**: Comunicados importantes
- **Chat Seguro**: Mensagens entre agentes
- **Ações Rápidas**: Funcionalidades do sistema

### 3. Funcionalidades por Nível
- **Alpha**: Pode adicionar novos avisos
- **Beta/Gamma**: Acesso de leitura e chat

## 🌐 Hospedagem Gratuita

### Opção 1: Render.com (Recomendado)
1. Crie uma conta em [render.com](https://render.com)
2. Conecte seu repositório GitHub
3. Configure o serviço web:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
4. Deploy automático!

### Opção 2: Railway.app
1. Acesse [railway.app](https://railway.app)
2. Conecte com GitHub
3. Selecione o repositório
4. Deploy automático

### Opção 3: Heroku
1. Crie conta no [Heroku](https://heroku.com)
2. Instale Heroku CLI
3. Execute:
   ```bash
   heroku create nome-do-seu-app
   git push heroku main
   ```

### Opção 4: PythonAnywhere
1. Crie conta em [pythonanywhere.com](https://pythonanywhere.com)
2. Faça upload dos arquivos
3. Configure o web app Flask
4. Defina o arquivo principal como `app.py`

## 🔒 Configurações de Segurança

### Alterar Chave Secreta
No arquivo `app.py`, linha 7:
```python
app.secret_key = 'SUA_CHAVE_SECRETA_AQUI'
```

### Adicionar Novos Agentes
No arquivo `app.py`, seção `AGENTES` (linha 11):
```python
'novo_agente': {
    'password': 'senha_secreta',
    'nome_completo': 'Nome do Agente',
    'nivel_acesso': 'Alpha',  # Alpha, Beta ou Gamma
    'especialidade': 'Sua Especialidade',
    'status': 'Ativo'
}
```

### Remover Agentes
Simplesmente delete a entrada correspondente do dicionário `AGENTES`.

## 📁 Estrutura do Projeto

```
central_agentes_secretos/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── README.md             # Esta documentação
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── index.html        # Página inicial
│   ├── login.html        # Página de login
│   └── painel_secreto.html # Painel principal
└── static/               # Arquivos estáticos
    ├── css/
    │   └── style.css     # Estilos principais
    ├── js/
    │   └── main.js       # JavaScript principal
    └── img/              # Imagens (vazio por padrão)
```

## 🎨 Personalização

### Cores do Tema
No arquivo `static/css/style.css`, você pode alterar:
- **Cor principal**: `#e74c3c` (vermelho)
- **Cor secundária**: `#3498db` (azul)
- **Cor de fundo**: Gradiente escuro

### Adicionar Novos Avisos
Agentes com nível Alpha podem adicionar avisos diretamente pelo painel.

### Modificar Mensagens
As mensagens do chat são armazenadas temporariamente. Para persistência, implemente um banco de dados.

## 🛠️ Desenvolvimento Avançado

### Banco de Dados
Para uso em produção, considere implementar:
- SQLite para projetos pequenos
- PostgreSQL para projetos maiores
- MongoDB para dados não-relacionais

### Recursos Adicionais
- Sistema de arquivos para documentos
- Upload de imagens de perfil
- Notificações em tempo real
- Sistema de missões

## 🐛 Solução de Problemas

### Erro de Porta em Uso
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F
```

### Dependências Não Encontradas
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Problemas de Permissão
```bash
# Linux/Mac
chmod +x app.py
```

## 📞 Suporte

Se encontrar problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme que a porta 5000 está livre
3. Verifique os logs do console para erros
4. Teste com diferentes navegadores

## 📄 Licença

Este projeto é de uso livre para fins educacionais e de entretenimento.

## 🎉 Divirta-se!

Agora você e seus amigos podem se sentir como verdadeiros agentes secretos! 

**Lembre-se**: Este é um projeto para diversão. Não use para atividades reais de espionagem! 😄

---

*Desenvolvido com ❤️ para agentes secretos em formação*

