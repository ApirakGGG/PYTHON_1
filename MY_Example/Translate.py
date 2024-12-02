import tkinter as tk #for GUI Interface
from tkinter import ttk , messagebox #for style GUI
from deep_translator import GoogleTranslator  # สำหรับแปลภาษา

# create main windows 
root = tk.Tk()
root.title("Translator Program")
root.geometry("800x800")

# function for transtor
def translate_text():
    try :
        src_lang = source_lang.get() # อ่านค่าภาษาต้นทางที่เลือก
        dest_lang = target_lang.get() # อ่านค่าภาษาปลายทางที่เลือก
        text = source_text.get("1.0", tk.END) #อ่านข้อความจาก Text Area ต้นทาง

        #call googletranslate for translation
        translated = GoogleTranslator(source= src_lang , target= dest_lang).translate(text)
        target_text.delete("1.0", tk.END) #ล้าง Text Area ของผลลัพธ์
        target_text.insert(tk.END, translated) #แสดงผลลัพธ์ที่แปล
    except Exception as e :
        messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")
        print(messagebox)

#create label for Message "Choose a Languages"
source_label = tk.Label(root, text="เลือกภาษาต้นทาง:")
source_label.pack(pady=5)

# ดึงข้อมูลภาษาที่รองรับจาก GoogleTranslator
language_options = [
    "english","thai"
]

# create DropDown Menu สำหรับภาษาต้นทาง
source_lang = ttk.Combobox(root, values=language_options , state="readonly")
source_lang.set("english") #ค่าเริ่มต้นภาษา ENG
source_lang.pack()

#สร้างlabel for เลือกข้อความต้นทาง
source_text_label = tk.Label(root, text="ข้อความต้นทาง:")
source_text_label.pack(pady=5)
source_text = tk.Text(root, height = 5 , wrap = tk.WORD)
source_text.pack(pady=5)

#create label "เลือกภาษาปลายทาง"
target_label = tk.Label(root , text="เลือกภาษาปลายทาง:")
target_label.pack(pady=5)

# create DropDown Menu สำหรับภาษาปลายทาง
target_lang = ttk.Combobox(root, values=language_options, state="readonly")
target_lang.set("thai")#ค่าเริ่มต้นภาษา Thai
target_lang.pack()

#create Translate Button
translate_button = tk.Button(root, text="แปลภาษา", command=translate_text, bg="blue", fg="white")
translate_button.pack(pady=10)

#create label and text area for result message
target_text_label = tk.Label(root, text="ผลลัพธ์ที่แปล:")
target_text_label.pack(pady=5)
target_text = tk.Text(root , height=5, wrap=tk.WORD)
target_text.pack(pady=5)

#start program
root.mainloop()

