from googletrans import Translator

try:
    with open('test.txt') as myFile:
        test = myFile
        translator = Translator()
        translations = translator.translate(test.readlines(), dest='ja')
        with open('text-translate.txt', mode='w', encoding='utf8') as newFile:
            trans = []
            for item in translations:
                newFile.write(f'{item.origin} -> {item.text}\n')
except FileNotFoundError:
    print('sorry, file not found')
