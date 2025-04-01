import customtkinter as ctk

def create_ui_elements(parent, models, update_model_callback, select_file_callback, transcribe_callback):
    """
    Cria todos os elementos da interface do usuário 
    e retorna um dicionário contendo referências a eles
    """
    elements = {}
    
    # Label de título com estilo melhorado
    elements["title_label"] = ctk.CTkLabel(
        master=parent,
        text="Transcritor de Áudio",
        font=("Helvetica", 24, "bold")
    )
    elements["title_label"].pack(pady=(20, 30))

    # Frame para opções de modelo com estilo melhorado
    elements["model_frame"] = ctk.CTkFrame(master=parent)
    elements["model_frame"].pack(fill="x", pady=(0, 20), padx=5)

    # Container para centralização dos elementos
    elements["model_container"] = ctk.CTkFrame(master=elements["model_frame"], fg_color="transparent")
    elements["model_container"].pack(pady=15)

    # Label para seleção de modelo
    elements["model_label"] = ctk.CTkLabel(
        master=elements["model_container"],
        text="Modelo de Transcrição:",
        font=("Helvetica", 14),
        anchor="e",
        width=180
    )
    elements["model_label"].pack(side="left", padx=(0, 15))

    # Dropdown para seleção de modelo com estilo melhorado
    elements["model_var"] = ctk.StringVar(value="Whisper Large V3")
    elements["model_dropdown"] = ctk.CTkOptionMenu(
        master=elements["model_container"],
        values=list(models.keys()),
        variable=elements["model_var"],
        command=update_model_callback,
        font=("Helvetica", 12),
        width=250,
        height=35,
        dropdown_font=("Helvetica", 12)
    )
    elements["model_dropdown"].pack(side="left")

    # Frame para área de upload
    elements["upload_frame"] = ctk.CTkFrame(master=parent)
    elements["upload_frame"].pack(fill="x", pady=(0, 20))

    # Botão para selecionar arquivo com estilo melhorado
    elements["select_button"] = ctk.CTkButton(
        master=elements["upload_frame"],
        text="Selecionar Arquivo de Áudio",
        command=select_file_callback,
        font=("Helvetica", 12),
        height=40,
        corner_radius=10
    )
    elements["select_button"].pack(side="left", padx=10)

    # Label para mostrar o arquivo selecionado
    elements["file_label"] = ctk.CTkLabel(
        master=elements["upload_frame"],
        text="Nenhum arquivo selecionado",
        font=("Helvetica", 12),
        text_color="gray"
    )
    elements["file_label"].pack(side="left", padx=10)

    # Frame para área de transcrição
    elements["transcription_frame"] = ctk.CTkFrame(master=parent)
    elements["transcription_frame"].pack(fill="both", expand=True, pady=(0, 20))

    # Label para área de transcrição
    elements["transcription_label"] = ctk.CTkLabel(
        master=elements["transcription_frame"],
        text="Transcrição",
        font=("Helvetica", 14, "bold")
    )
    elements["transcription_label"].pack(pady=(10, 5))

    # Área de texto para mostrar a transcrição com scrollbar
    elements["transcription_text"] = ctk.CTkTextbox(
        master=elements["transcription_frame"],
        font=("Helvetica", 12),
        wrap="word"
    )
    elements["transcription_text"].pack(fill="both", expand=True, padx=10, pady=(0, 10))

    # Frame para botões
    elements["button_frame"] = ctk.CTkFrame(master=parent)
    elements["button_frame"].pack(fill="x", pady=(0, 10))

    # Botão para iniciar transcrição
    elements["transcribe_button"] = ctk.CTkButton(
        master=elements["button_frame"],
        text="Iniciar Transcrição",
        command=transcribe_callback,
        font=("Helvetica", 12),
        height=40,
        corner_radius=10,
        state="disabled"
    )
    elements["transcribe_button"].pack(side="right", padx=10)

    # Progress bar (inicialmente oculta)
    elements["progress_bar"] = ctk.CTkProgressBar(master=elements["button_frame"])
    elements["progress_bar"].set(0)
    elements["progress_bar"].pack(fill="x", padx=10, pady=(10, 0))
    elements["progress_bar"].pack_forget()

    # Label de status (inicialmente oculta)
    elements["status_label"] = ctk.CTkLabel(
        master=elements["button_frame"],
        text="",
        font=("Helvetica", 12)
    )
    elements["status_label"].pack(pady=(5, 0))
    elements["status_label"].pack_forget()
    
    return elements 