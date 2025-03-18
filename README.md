# Transcritor de Áudio com Groq

Bem-vindo ao **Transcritor de Áudio com Groq**! Este é um projeto em Python que permite carregar arquivos de áudio e transcrevê-los automaticamente usando a API do Groq, exibindo o texto resultante em uma interface gráfica moderna criada com Customtkinter.

## Funcionalidades
- **Carregamento de arquivos de áudio**: Suporta formatos como MP3, WAV, M4A, FLAC, OGG, entre outros.
- **Transcrição automática**: Utiliza modelos de transcrição da API Groq, como `whisper-large-v3`, `whisper-large-v3-turbo` e `distil-whisper-large-v3-en`.
- **Seleção de modelo**: Escolha entre diferentes modelos de transcrição para otimizar velocidade ou precisão.
- **Interface gráfica**: Uma UI simples e elegante construída com Customtkinter.
- **Suporte multilíngue**: Configurado para português por padrão, mas pode ser ajustado para outros idiomas (exceto o modelo inglês `distil-whisper-large-v3-en`).

## Pré-requisitos
- Python 3.9 ou superior instalado.
- Uma chave API do Groq (obtenha em [console.groq.com](https://console.groq.com)).
- Dependências Python:
  - `customtkinter`
  - `groq`
  - `python-dotenv`
