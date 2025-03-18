import os
import threading
import time
from groq import Groq
from tkinter import filedialog
from utils.config import load_environment

class TranscriptionService:
    def __init__(self):
        # Carregar variáveis de ambiente
        env = load_environment()
        
        # Configurar cliente Groq
        self.client = Groq(api_key=env["api_key"])
        
        # Modelos disponíveis
        self.models = {
            "Whisper Large V3 Turbo": "whisper-large-v3-turbo",
            "Distil-Whisper English": "distil-whisper-large-v3-en",
            "Whisper Large V3": "whisper-large-v3"
        }
        
        self.default_model = "whisper-large-v3"
    
    def select_file(self):
        """Abre diálogo para selecionar arquivo de áudio"""
        return filedialog.askopenfilename(
            filetypes=[
                ("Arquivos de áudio", "*.mp3 *.wav *.m4a *.flac *.ogg")
            ]
        )
    
    def get_filename(self, file_path):
        """Retorna apenas o nome do arquivo a partir do caminho completo"""
        return os.path.basename(file_path)
    
    def update_progress(self, progress_bar, is_processing):
        """Atualiza a barra de progresso durante o processamento"""
        for i in range(100):
            if not is_processing[0]:
                break
            progress_bar.set(i / 100)
            time.sleep(0.05)
    
    def perform_transcription(self, file_path, model_id, callback, root):
        """Realiza a transcrição de áudio"""
        try:
            with open(file_path, "rb") as file:
                # Determinar o idioma baseado no modelo
                language = "en" if model_id == "distil-whisper-large-v3-en" else "pt"
                
                transcription = self.client.audio.transcriptions.create(
                    file=(os.path.basename(file_path), file.read()),
                    model=model_id,
                    response_format="text",
                    language=language
                )
                
            root.after(0, lambda: callback(transcription))
            
        except Exception as e:
            root.after(0, lambda e=e: callback(f"Erro na transcrição: {str(e)}"))
    
    def start_transcription(self, file_path, model_id, callback, root, progress_bar):
        """Inicia processo de transcrição em threads paralelas"""
        # Flag compartilhada para controlar o progresso
        is_processing = [True]
        
        # Thread para atualizar a barra de progresso
        progress_thread = threading.Thread(
            target=self.update_progress,
            args=(progress_bar, is_processing)
        )
        
        # Função wrapper para marcar o fim do processamento
        def transcription_done(result):
            is_processing[0] = False
            callback(result)
        
        # Thread para realizar a transcrição
        transcription_thread = threading.Thread(
            target=self.perform_transcription,
            args=(file_path, model_id, transcription_done, root)
        )
        
        # Iniciar as threads
        progress_thread.start()
        transcription_thread.start()
