import tkinter as tk
from tkinter.filedialog import askopenfile

import pdf2image


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('PDF', '.pdf')])
    print(file_path)
    pass
    pages = pdf2image.convert_from_path(file_path.name)
    print(pages)
    for i in range(len(pages)):
        pages[i].save('page' + str(i) + '.jpg', 'JPEG')

window = tk.Tk()
window.title('Конвертер PDF')
window.geometry('350x150')
window.resizable(False, False)

button_upload = tk.Button(window, text='Загрузить файл', width=20, height=2, command=open_file)
button_upload.place(x=100, y=50)

# number1_entry = tk.Entry(window, width=28)
# number1_entry.place(x=100, y=75)
# number1_label = tk.Label(window, text='Введите первое число:')
# number1_label.place(x=100, y=50)
# number2_entry = tk.Entry(window, width=28)
# number2_entry.place(x=100, y=150)
# number2_label = tk.Label(window, text='Введите второе число:')
# number2_label.place(x=100, y=125)
# answer_entry = tk.Entry(window, width=28)
# answer_entry.place(x=100, y=300)
# answer_label = tk.Label(window, text='Ответ:')
# answer_label.place(x=100, y=275)

window.mainloop()