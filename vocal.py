import nltk
import streamlit as st
import speech_recognition as sr
from nltk.chat.util import Chat, reflections

# Assurez-vous de télécharger les ressources nécessaires de NLTK
nltk.download('punkt')

# Charger et prétraiter le fichier texte
# Ici, nous utilisons des paires de correspondances simples pour le chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by you. You can call me Bot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, how can I help you?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"je suis riche",
        ["C'est super ! Que faites-vous dans la vie ?", "Félicitations !"]
    ],
    [
        r"je suis pauvre",
        ["Je suis désolé d'entendre cela. Comment puis-je vous aider ?", "Ça ira mieux, ne vous inquiétez pas."]
    ],
    # Ajouter des paires par défaut pour les entrées non reconnues
    [
        r"(.*)",
        ["Je suis désolé, je ne comprends pas ce que vous dites.", "Pouvez-vous reformuler votre question ?", "Je ne suis pas sûr de comprendre, pouvez-vous être plus précis ?"]
    ],
]

chatbot = Chat(pairs, reflections)

# Fonction pour transcrire la parole en texte
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Parlez maintenant...")
        audio = recognizer.listen(source)
        st.info("Transcription en cours...")
        try:
            text = recognizer.recognize_google(audio, language="fr-FR")
            st.success(f"Vous avez dit : {text}")
            return text
        except sr.UnknownValueError:
            st.error("Désolé, je n'ai pas compris. Veuillez réessayer.")
        except sr.RequestError:
            st.error("Erreur de service de reconnaissance vocale. Veuillez vérifier votre connexion.")
        return ""

# Interface utilisateur Streamlit
st.title("Chatbot à Commande Vocale")
st.write("""
Cette application permet de discuter avec un chatbot en utilisant des entrées textuelles ou vocales.
""")

# Entrée de texte
text_input = st.text_input("Tapez votre message ici :")

# Entrée vocale
if st.button("Parlez"):
    text_input = speech_to_text()

# Afficher la réponse du chatbot
if text_input:
    response = chatbot.respond(text_input)
    st.write(f"Chatbot : {response}")

