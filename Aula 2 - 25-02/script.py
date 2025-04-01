import os
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=("CHAVE_API_KEY")
)


completion = client.chat.completions.create(
    model = "deepseek-r1-distill-llama-70b",
    messages=[
        {"role": "system", "content": "Você é uma vendedora de pastel eficiente."},
        {"role": "user", "content": "Me indique os melhores pasteis, para a semana, me responda em português. Seja rigososo!"}
    ]
)

print (completion.choices[0].message)