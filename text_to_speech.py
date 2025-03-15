import gtts
import playsound
import os
from gtts.lang import tts_langs
from translate_file import translate_from_file

supported_langs = tts_langs()

file_path = "Speech.txt"
lang_code, translated_text = translate_from_file(file_path)


if lang_code and translated_text:
    if lang_code not in supported_langs:
        error = gtts.gTTS("Language accent is not supported by gTTS. Defaulting to English.", lang ="en")
        error.save("accenterror.mp3")
        playsound.playsound("accenterror.mp3")
        os.remove("accenterror.mp3")
        lang_code = 'en'

    print(f"Final language code for speech: {lang_code}")
    print(f"Translated text: {translated_text}")

    sound = gtts.gTTS(translated_text, lang=lang_code)
    sound.save("welcome.mp3")

    playsound.playsound("welcome.mp3")

    os.remove("welcome.mp3")
else:
    print("Translation failed or no valid language was selected.")
