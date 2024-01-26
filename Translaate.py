import random
from googletrans import LANGUAGES, Translator
from gtts import gTTS

def translate_to_random_language(text):
    supported_languages = list(LANGUAGES.keys())
    random_language = random.choice(supported_languages)

    translator = Translator()
    translated_text = translator.translate(text, dest=random_language)

    return translated_text.text, translated_text.src, translated_text.dest

def translate_alot(text, times=10):
    for i in range(times):
        text, source_lang, target_lang = translate_to_random_language(text)
        print(text, source_lang, target_lang)
    return text

text_to_translate = input("Enter text to translate: ")
translated_text, source_lang, target_lang = translate_to_random_language(text_to_translate)

print(f"Original text ({source_lang}): {text_to_translate}")
text=translate_alot(text_to_translate)
print(text)
output = Translator().translate(text, dest="en")
print(output)
output_text = output.text
tts = gTTS(output_text)
tts.save('text.mp3')
#print(f"Translated text ({target_lang}): {translated_text}")