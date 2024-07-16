from tkinter import *
import googletrans
from googletrans import Translator, LANGUAGES
from tkinter import ttk, messagebox

root = Tk()
root.geometry("880x300")

try:
    translator = Translator()
except Exception as e:
    messagebox.showerror("Translator Error", f"Failed to initialize translator: {str(e)}")
    translator = None

def translate_it():
    translated_text.delete(1.0, END)
    try:
        if translator:
            from_language = original_combo.get()
            to_language = translate_combo.get()
            original_text_str = original_text.get(1.0, END).strip()
            
            if original_text_str:
                translated_result = translator.translate(original_text_str, src=from_language, dest=to_language)
                translated_text.insert(END, translated_result.text)
            else:
                messagebox.showwarning("Translator", "Please enter text to translate.")
        else:
            messagebox.showerror("Translator", "Translator is not initialized. Please check your network connection.")
    except Exception as e:
        messagebox.showerror("Translator", f"Translation error: {str(e)}")

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

language_list = list(LANGUAGES.values())

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

original_combo = ttk.Combobox(root, width=50, values=language_list)
original_combo.current(21)  # Change this to match the language you want to translate from
original_combo.grid(row=1, column=0)

translate_combo = ttk.Combobox(root, width=50, values=language_list)
translate_combo.current(26)  # Change this to match the language you want to translate to
translate_combo.grid(row=1, column=2)

clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()



