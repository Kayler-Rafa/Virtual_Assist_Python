import speech_recognition as sr
import pyautogui
import datetime
import webbrowser
import pyttsx3

# Inicializa o motor de fala com voz feminina em português
engine = pyttsx3.init()
voices = engine.getProperty("voices")

# Tenta selecionar uma voz em português
for voice in voices:
    if "portuguese" in voice.languages or "brazil" in voice.id.lower():
        engine.setProperty("voice", voice.id)
        break

engine.setProperty("rate", 180)  # Velocidade da fala

def speak(text):
    """Faz o Alfa falar diretamente em português"""
    engine.say(text)
    engine.runAndWait()

def get_time():
    """Retorna a hora atual"""
    now = datetime.datetime.now().strftime("%H:%M")
    return f"Agora são {now}"

def open_app(app_name):
    """Abre aplicativos"""
    speak(f"Abrindo {app_name}")
    pyautogui.press("win")
    pyautogui.write(app_name)
    pyautogui.press("enter")

def open_youtube():
    """Abre o YouTube"""
    speak("Abrindo YouTube")
    webbrowser.open("https://www.youtube.com")
    

def get_commands():
    """Lista os comandos disponíveis"""
    commands = (
        "Olá! Eu sou a Alfa. Aqui estão alguns comandos que você pode usar: "
        "'Alfa, que horas são?' para saber a hora atual. "
        "'Alfa, abra o Opera' para abrir o navegador. "
        "'Alfa, abra o Spotify' para abrir o Spotify. "
        "'Alfa, abra o YouTube' para acessar o YouTube. "
        "'Alfa, me dê seus comandos' para ver esta lista de comandos." 
    )
    speak(commands)

def get_hello():
    """Retorna mensagem"""
    return f"Olá"

def process_command(command):
    """Executa comandos"""
    if "horas" in command:
        speak(get_time())
    elif "abra o navegador" in command:
        open_app("Opera")
    elif "quero ouvir música" in command:
        open_app("Spotify")
    elif "abra o youtube" in command:
        open_youtube()
    elif "comando" in command:
        get_commands()
    elif "olá" in command:
        speak("Olá")
    else:
        speak("Desculpe, não entendi o comando.")

def listen():
    """Escuta comandos de voz"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Alfa -")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="pt-BR").lower()
        print(f"Você disse: {command}")

        if "alfa" in command:
            command = command.replace("alfa", "").strip()
            process_command(command)
        else:
            print("Nenhum comando reconhecido.")

    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de voz.")

# Mensagem de boas-vindas ao iniciar o script
speak("Iniciada!")

# Loop infinito para o Alfa sempre escutar
while True:
    listen()
