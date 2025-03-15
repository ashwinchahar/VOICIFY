from googletrans import Translator, LANGUAGES
import gtts 
import playsound
import os

def translate_from_file(file_path):
    translator = Translator()

    # Read file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().strip()
            if not text:
                error = gtts.gTTS("The file is empty. Please provide some text to translate.", lang ="en")
                error.save("error.mp3")
                playsound.playsound("error.mp3")
                os.remove("error.mp3")
                return None, None
            print(f"\nText to be translated:\n{text}\n")

    except FileNotFoundError:
        missing_file = gtts.gTTS("Error: File '{file_path}' not found.", lang= "en")
        missing_file.save("missingfile.mp3")
        playsound.playsound("missingfile.mp3")
        os.remove("missingfile.mp3")
        return None, None

    # Display available languages
    available = gtts.gTTS("Available languages are as follows:", lang= "en")
    available.save("available.mp3")
    playsound.playsound("available.mp3")
    os.remove("available.mp3")

    print("\nAvailable languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code} - {lang_name}")

    #target input langugae
    voice = gtts.gTTS("Please enter the target language ", lang = "en" )
    voice.save("input.mp3")
    playsound.playsound("input.mp3")
    os.remove("input.mp3")

    target_language = input("Please enter the target language (name or code): ").strip().lower()

    #target language code
    target_language_code = None
    if target_language in LANGUAGES:
        target_language_code = target_language
    else:
        for code, name in LANGUAGES.items():
            if name.lower() == target_language:
                target_language_code = code
                break

    if target_language_code:
        # Translate the text
        translation = translator.translate(text, dest=target_language_code)
        translated_text = translation.text
        print(f"\nTranslated Text in {LANGUAGES[target_language_code]}: {translated_text}")
        return target_language_code, translated_text
    else:
        error = gtts.gTTS("Invalid language input. Please try again.", lang = "en")
        error.save("langerror.mp3")
        playsound.playsound("langerror.mp3")
        os.remove("langerror.mp3")
        return None, None

if __name__ == "__main__":
    file_path = "Speech.txt"
    lang_code, translated_text = translate_from_file(file_path)
    print(f"\nFinal Output: lang_code = {lang_code}, translated_text = {translated_text}")
