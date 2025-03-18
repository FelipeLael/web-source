import os
from dotenv import load_dotenv

def load_environment():
    """
    Carrega variáveis de ambiente do arquivo .env
    e retorna valores configurados
    """
    # Carregar variáveis do arquivo .env
    load_dotenv()
    
    # Obter API key para o serviço Groq
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("GROQ_API_KEY não encontrada no arquivo .env")
    
    return {
        "api_key": api_key
    }

def get_app_settings():
    """
    Retorna configurações padrão da aplicação
    """
    return {
        "window_title": "Transcritor de Áudio com Groq",
        "window_size": "800x600",
        "min_window_size": (800, 600),
        "theme_mode": "dark",
        "color_theme": "blue",
        "default_font": "Helvetica"
    } 