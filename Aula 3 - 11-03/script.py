from groq import Groq

client = Groq()

# Transcrever o áudio 'audio.mp3'
audio_file_path = "audio.mp3"
with open(audio_file_path, "rb") as audio_file:  # Abrir o arquivo em modo binário
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-large-v3-turbo",
        language="pt"  # Define o idioma como português
    )

# Salvar a transcrição no arquivo 'audio_transcrito.txt'
with open("audio_transcrito.txt", "w", encoding="utf-8") as file:
    file.write(transcription.text)  # Corrigir para acessar o atributo 'text'

print("Transcrição concluída e salva em 'audio_transcrito.txt'.")
