import customtkinter as ctk
from services.transcription import TranscriptionService
from ui.widgets import create_ui_elements
from utils.config import get_app_settings

class AudioTranscriptionApp:
    def __init__(self, root):
        self.root = root
        
        # Obter configurações da aplicação
        settings = get_app_settings()
        self.root.title(settings["window_title"])
        self.root.geometry(settings["window_size"])
        self.root.minsize(*settings["min_window_size"])
        
        # Inicializar serviço de transcrição
        self.transcription_service = TranscriptionService()
        
        # Estado da aplicação
        self.is_processing = False
        self.audio_file = None
        self.selected_model = self.transcription_service.default_model
        
        # Criar interface
        self.create_widgets()

    def create_widgets(self):
        # Criar o frame principal
        self.main_frame = ctk.CTkFrame(master=self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Criar elementos da UI usando função do módulo widgets
        elements = create_ui_elements(
            self.main_frame, 
            self.transcription_service.models, 
            self.update_model,
            self.select_audio_file,
            self.start_transcription
        )
        
        # Armazenar referências aos elementos da UI
        self.title_label = elements["title_label"]
        self.model_frame = elements["model_frame"]
        self.model_container = elements["model_container"]
        self.model_label = elements["model_label"]
        self.model_dropdown = elements["model_dropdown"]
        self.model_var = elements["model_var"]
        self.upload_frame = elements["upload_frame"]
        self.select_button = elements["select_button"]
        self.file_label = elements["file_label"]
        self.transcription_frame = elements["transcription_frame"]
        self.transcription_label = elements["transcription_label"]
        self.transcription_text = elements["transcription_text"]
        self.button_frame = elements["button_frame"]
        self.transcribe_button = elements["transcribe_button"]
        self.progress_bar = elements["progress_bar"]
        self.status_label = elements["status_label"]

    def update_model(self, selection):
        """Atualiza o modelo selecionado quando o usuário escolhe uma opção no dropdown"""
        self.selected_model = self.transcription_service.models[selection]

    def select_audio_file(self):
        """Seleciona um arquivo de áudio para transcrição"""
        file_path = self.transcription_service.select_file()
        
        if file_path:
            self.audio_file = file_path
            self.file_label.configure(text=f"Arquivo: {self.transcription_service.get_filename(file_path)}")
            self.transcribe_button.configure(state="normal")
            self.transcription_text.delete("0.0", "end")
            self.progress_bar.pack_forget()
            self.status_label.pack_forget()

    def start_transcription(self):
        """Inicia o processo de transcrição em uma thread separada"""
        if self.is_processing or not self.audio_file:
            return

        self.is_processing = True
        self.transcribe_button.configure(state="disabled")
        self.select_button.configure(state="disabled")
        self.model_dropdown.configure(state="disabled")
        self.progress_bar.pack(fill="x", padx=10, pady=(10, 0))
        self.status_label.pack(pady=(5, 0))
        self.status_label.configure(text="Processando transcrição...")
        
        # Iniciar threads para transcrição e progresso visual
        self.transcription_service.start_transcription(
            self.audio_file,
            self.selected_model,
            self.update_ui_after_transcription,
            self.root,
            self.progress_bar
        )

    def update_ui_after_transcription(self, result):
        """Atualiza a UI após a transcrição ser concluída"""
        self.is_processing = False
        self.transcription_text.delete("0.0", "end")
        self.transcription_text.insert("0.0", result)
        
        self.transcribe_button.configure(state="normal")
        self.select_button.configure(state="normal")
        self.model_dropdown.configure(state="normal")
        self.progress_bar.pack_forget()
        self.status_label.configure(text="Transcrição concluída!")
        
        # Esconder a mensagem de status após 3 segundos
        self.root.after(3000, lambda: self.status_label.pack_forget()) 