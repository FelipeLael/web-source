import customtkinter as ctk
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import AudioTranscriptionApp
from utils.config import get_app_settings

def main():
    # Aplicar configurações de tema
    settings = get_app_settings()
    ctk.set_appearance_mode(settings["theme_mode"])
    ctk.set_default_color_theme(settings["color_theme"])

    # Iniciar aplicação
    root = ctk.CTk()
    app = AudioTranscriptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 