from logging import exception
from googletrans import Translator

translator = Translator()


def translatethis(text):
    text = str(text)
    try:
        if translator.detect(text).lang == 'ru':
            resLang = 'en'
        else:
            resLang = 'ru'

        textResult = translator.translate(text, dest=resLang)
        return (text + ' → ' + textResult.text)
    except:
        raise Exception('Похоже, что версия переводчика не актуальна, хотя может дело и в чем-то другом, я хз')


