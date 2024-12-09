import os 
from tkinter import Tk, Frame,Listbox,Button,filedialog,Label
import pygame as pg

# // Class Musiv_Player
class Music_Player_App :
    # ui interface App
    def __init__(self, root):
        self.root = root
        self.root.title("Music_App")
        self.root.geometry("600x600")
        
    #  pygame mixer สำหรับเล่นเสียง
        pg.mixer.init()
        
    # path สำหรับจัดการไฟล์เพลง
        self.playlist = []
        
    #  Label แสดงเพลงที่กำลังเล่นอยู่
        self.current_song_label = Label(self.root, text="No song playing", bg="gray", fg="white", wraplength=350)
        self.current_song_label.pack(pady=10 , fill="x")
        
    # Frame สำหรับเพลย์ลิสต์และ Button
        self.frame= Frame(self.root)
        self.frame.pack(pady=20)
    
    # ListBoxแสดงเพลย์ลิสต์
        self.song_listbox = Listbox(self.frame, width=50, height=15)
        self.song_listbox.pack(pady=3)
        
    # Buttonsสำหรับควบคุม App และ เล่นเพลง
        Button(self.root, text="Add_song", command=self.add_song).pack(side="top",pady=5, padx=3)
        Button(self.root, text="Play", command=self.play_song).pack(side="top", pady=5, padx=3)
        Button(self.root, text="Stop", command=self.stop_song).pack(side="top", pady=5, padx=3)
        Button(self.root, text="Quit", command=self.root.quit).pack(side="top", pady=5, padx=3)
    
# function เพิ่มเพลง
    def add_song (self) :
        # """เพิ่มเพลงเข้า playlist."""
        song_path = filedialog.askopenfilename(title="เลือกเพลง", filetypes=[("Audio Files", "*.mp3; *.wav")])
        # condition
        if song_path:
            #เพิ่มเพลงเข้า playlist
            self.playlist.append(song_path) # เก็บไว้ที่ song_path
            #แสดงเฉพาะชื่อเพลงในกล่องรายการ
            self.song_listbox.insert("end", os.path.basename(song_path)) 

# function เล่นเพลง
    def play_song (self) :
        #  """เล่นเพลงที่เลือก."""
        try :
            selected_index = self.song_listbox.curselection() #รับพลงที่เลือกจาดindex
            if selected_index :
                selected_song = self.playlist[selected_index[0]] #รับเพลงจาก song_path
                
                pg.mixer.music.load(selected_song) #โหลดเพลงจาก selected_song
                pg.mixer.music.play() #เล่นเพลง
                
                # อัปเดตเพลงที่กำลังเล่นอยู่
                self.current_song_label.config(text=f"Playing: {os.path.basename(selected_song)}")
            else :
                # ถ้าไม่ทีเพลงให้แสดง ไม่มีเพลงที่เลือก
                self.current_song_label.config(text="No song Selected")
                
        except Exception as e :
            #จับError
            self.current_song_label.config(text=f"Error: {str(e)}") 
        
# function หยุดเพลง
    def stop_song (self) :
        #  """หยุดเพลงที่กำลังเล่น"""
         pg.mixer.music.stop() #หยุดเพลง
          #แสดงว่าไม่มีเพลงที่กำลังเล่น
         self.current_song_label.config(text="No song playing")
        
    
# // Main App
if __name__ == '__main__' :
    root = Tk()
    app = Music_Player_App(root)
    root.mainloop()
