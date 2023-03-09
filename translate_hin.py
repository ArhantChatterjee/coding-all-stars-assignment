from googletrans import Translator

def conversion(word):
    # Create a translator object
    translator = Translator()
    # Detect the source language (optional)
    detected_lang = translator.detect(word)

    # Translate the word to Hindi
    translation = translator.translate(word, dest='hi')
    if detected_lang.lang == "en":
        # Print the translated text
        print(f"{word} ({detected_lang.lang}) in Hindi is {translation.text}")
        return translation.text

word = input("enter the word to convert: ")
conversion(word)