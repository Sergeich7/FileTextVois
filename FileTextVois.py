"""

Программа получает с клавиатуры или из файлов .TXT .PDF . DOCX первую
фразу и проговаривает первое слово.

Использованы библиотеки:
pyttsx3, docx, PDFMiner

Последние изменение: 20.05.2022

"""

import viocemachie

# Озвучивает 1ое слово введенное с клавиатуры
vm_stdin = viocemachie.voice_stdin()
vm_stdin.say_1st_world()

# Озвучивает 1ое слово из .txt файла
vm_txt = viocemachie.voice_txt()
vm_txt.say_1st_world("smp.txt")

# Озвучивает 1ое слово из .docx файла
vm_docx = viocemachie.voice_docx()
vm_docx.say_1st_world("smp.docx")

# Озвучивает 1ое слово из .txt файла
vm_docx = viocemachie.voice_txt()
vm_docx.say_1st_world("smp.pdf")
