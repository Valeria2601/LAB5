from tkinter import *

# Функция шифрования текста
def encrypt_text():
  shift = int(shift_entry.get()) % 33
  text = text_entry.get()
  encrypted_text = ""
  
  for letter in text:
    # Шифруем только буквы
    if letter.isalpha():
      if letter.isupper():
        # Заглавные буквы
        encrypted_text += chr((ord(letter) - ord('А') + shift) % 33 + ord('А'))
      else:
        # Строчные буквы
        encrypted_text += chr((ord(letter) - ord('а') + shift) % 33 + ord('а'))
    else:
      # Остальные символы оставляем без изменения
      encrypted_text += letter
  
  result_label["text"] = "Зашифрованный текст: " + encrypted_text

# Функция расшифровки текста
def decrypt_text():
  shift = int(shift_entry.get()) % 33
  text = text_entry.get()
  decrypted_text = ""
  
  for letter in text:
    # Расшифровываем только буквы
    if letter.isalpha():
      if letter.isupper():
        # Заглавные буквы
        decrypted_text += chr((ord(letter) - ord('А') - shift) % 33 + ord('А'))
      else:
        # Строчные буквы
        decrypted_text += chr((ord(letter) - ord('а') - shift) % 33 + ord('а'))
    else:
      # Остальные символы оставляем без изменения
      decrypted_text += letter
  
  result_label["text"] = "Расшифрованный текст: " + decrypted_text

def check_language():
    text = text_entry.get()
    if any(char.isalpha() for char in text):
        if not any(char.isalpha() and ord(char) > 127 for char in text):
            result_label["text"] = "Ошибка: Введенный текст на английском языке"
        else:
            encrypt_text()
    else:
        encrypt_text()

# Создаем графический интерфейс
root = Tk()
root.title("Шифр Цезаря")

# Метка и поле ввода для текста
text_label = Label(root, text="Текст:")
text_label.pack()
text_entry = Entry(root)
text_entry.pack()

# Метка и поле ввода для шага сдвига
shift_label = Label(root, text="Шаг сдвига:")
shift_label.pack()
shift_entry = Entry(root)
shift_entry.pack()

# Кнопка для шифрования текста
encrypt_button = Button(root, text="Зашифровать", command=check_language)
encrypt_button.pack()

# Кнопка для расшифровки текста
decrypt_button = Button(root, text="Расшифровать", command=decrypt_text)
decrypt_button.pack()

# Метка для вывода результата
result_label = Label(root, text="")
result_label.pack()

# Запускаем главный цикл отрисовки окна
root.mainloop()