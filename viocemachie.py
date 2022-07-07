import pyttsx3
import docx

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


# родитель - умеет говорить
class voice_machine:

    @property
    def str_readed(self):
        return ''

    @str_readed.setter
    def str_readed(self, s):
        if len(s) > 0:
            self.phrase_for_saying = "Первое слово: " + s.split(' ')[0].upper()

    def __init__(self):
        self.phrase_for_saying = 'Ничего не найдено!'
        self.__tts = pyttsx3.init()

    def say_1st_word(self):
        print(self.phrase_for_saying)
        self.__tts.say(self.phrase_for_saying)
        self.__tts.runAndWait()
        print('Нажмите ENTER')
        input()


class voice_stdin(voice_machine):
    def say_1st_world(self):
        print('*'*20 + ' STDIN')
        self.str_readed = input('Введите слово или фразу: ')
        super().say_1st_word()


class voice_txt(voice_machine):
    def say_1st_world(self, fn):
        print('*'*20 + ' TXT')
        try:
            with open(fn, encoding='utf-8') as file:
                self.str_readed = file.read()
        except:
            self.phrase_for_saying = 'Не могу прочитать файл ' + fn + '!'
        super().say_1st_word()


class voice_docx(voice_machine):
    def say_1st_world(self, fn):
        print('*'*20 + ' DOCX')
        try:
            self.str_readed = docx.Document(fn).paragraphs[0].text
        except:
            self.phrase_for_saying = 'Не могу прочитать файл ' + fn + '!'
        super().say_1st_word()


class voice_pdf(voice_machine):
    def say_1st_world(self, fn):
        print('*'*20 + ' PDF')
        try:
            with open(fn, 'rb') as fh:
                resource_manager = PDFResourceManager()
                file_handle = io.StringIO()
                converter = TextConverter(resource_manager, file_handle)
                page_interpreter = \
                    PDFPageInterpreter(resource_manager, converter)
                page_interpreter.process_page(next(
                    PDFPage.get_pages(fh, caching=True, check_extractable=True)
                    ))
                self.str_readed = file_handle.getvalue()
                converter.close()
                file_handle.close()
        except:
            self.phrase_for_saying = 'Не могу прочитать файл ' + fn + '!'
        super().say_1st_word()
