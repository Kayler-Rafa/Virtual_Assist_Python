# 🔊 Alfa - Assistente Virtual com Voz AI

Alfa é um assistente virtual desenvolvido em **Python** que responde a comandos de voz e executa ações como abrir aplicativos, informar a hora e acessar sites. O projeto é inspirado no **Jarvis do Iron Man** e usa bibliotecas como **SpeechRecognition, pyttsx3, pyautogui e webbrowser**.

## 📚 Recursos
- ✅ **Reconhecimento de voz** (ativado por "Alfa")
- ⏰ **Informa a hora atual**
- 🛠 **Abre aplicativos como Opera e Spotify**
- 📺 **Acessa o YouTube**
- 📖 **Lista comandos ao dizer "Alfa, me dê seus comandos"**
- 🎤 **Voz feminina natural em português**

## ⚙️ Instalação
Certifique-se de ter o **Python 3.8+** instalado e execute os comandos abaixo:

```sh
pip install SpeechRecognition pyttsx3 pyautogui pyaudio
```

## 🌐 Como Usar
1. Execute o script:
   ```sh
   python test.py
   ```
2. O Alfa iniciará com a mensagem:
   ```
   Alfa iniciada, seja bem-vindo!
   ```
3. Diga **"Alfa"** seguido de um comando. Exemplos:
   - **"Alfa, que horas são?"**
   - **"Alfa, abra o Opera"**
   - **"Alfa, abra o Spotify"**
   - **"Alfa, abra o YouTube"**
   - **"Alfa, me dê seus comandos"**

## 🛠️ Personalização
- Para alterar a voz ou velocidade da Alfa, modifique estas linhas no código:
  ```python
  engine.setProperty("rate", 180)  # Velocidade da fala
  ```
- Para adicionar mais comandos, edite a função `process_command()`.

## ✨ Contribuição
Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutirmos as melhorias.

## 📚 Licença
Este projeto está sob a licença MIT.

---
Desenvolvido com Rafael Diniz

