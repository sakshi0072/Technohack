import os
import pygame
from tkinter import Tk, Button, Label, filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        self.music_files = []
        self.current_file = None

        self.label = Label(root, text="No music file selected")
        self.label.pack(pady=10)

        self.browse_button = Button(root, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        self.play_button = Button(root, text="Play", state="disabled", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = Button(root, text="Pause", state="disabled", command=self.pause_music)
        self.pause_button.pack(pady=5)

        self.stop_button = Button(root, text="Stop", state="disabled", command=self.stop_music)
        self.stop_button.pack(pady=5)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()

        if folder_path:
            self.music_files = [file for file in os.listdir(folder_path) if file.endswith((".mp3", ".wav"))]
            if not self.music_files:
                self.label.config(text="No music files found in the selected folder")
                return

            self.label.config(text="Select a music file to play")
            self.play_button.config(state="normal")

    def play_music(self):
        self.current_file = filedialog.askopenfilename(filetypes=(("Music files", "*.mp3;*.wav"),))
        if self.current_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()

            self.label.config(text="Now playing: " + os.path.basename(self.current_file))
            self.play_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.stop_button.config(state="normal")

    def pause_music(self):
        pygame.mixer.music.pause()
        self.pause_button.config(text="Resume", command=self.resume_music)

    def resume_music(self):
        pygame.mixer.music.unpause()
        self.pause_button.config(text="Pause", command=self.pause_music)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.label.config(text="Music stopped")
        self.play_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.stop_button.config(state="disabled")

if __name__ == "__main__":
    pygame.init()
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
    pygame.quit()
