
#
# Importar la librerias
#
import openai
import settings

openai.api_key = settings.api_key

# Rol system= para darle un contexto a nuestro sistema
# Contexto del asistente asistente universal "Eres un asistente muy util"
context = {"role": "system",
           "content": "Eres un asistente de creación de codigo de software, 
           "especialemnete los siguientes lenguajes (java Script,c#, php)"}
messages = [context]

# Para ejecutar este codigo siempre, hasta que escriba salir o exit se rompe el bucle.
while True:
    # Si no pones un input el asistente, ChatGPT se conecta automaticamente e interactua contigo.
    content = input("Pregunta lo que quieras? ")
    # Con la palabra exit o salir se rompe el ciclo
    if content == "salir" or content == "exit":
        break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    response_content = response.choices[0].message.content

    # Se agrega la respuesta al contexto para que siga acorde con la conversacion,
    # Si no se guarda el content de respuesta seria muy dificil entablar conversacion, 
    # ya que no sabria de que se esta hablando
    messages.append({"role": "assistant", "content": response_content})

    print(response_content)
