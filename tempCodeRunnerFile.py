import tkinter as tk
import random
import time
import winsound

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação de Sorteio e Cronômetro")
        self.name_counter = 1
        self.theme_counter = 1
        self.button_font_size = 20
        self.custom_font = ("Helvetica", 40)
        self.frame_borderwidth = 0  # Largura da borda dos frames

        self.names = ['Davi', 'Josy', 'Manassés']
        self.themes = ['Ensino', 'Pesquisa e Pós-Graduação e Inovação', 'Editora IFC', 'Extensão', 'Esporte e Lazer', 'Servidores', 'Infraestrutura e Planejamento', 'Assistência ao Educando']
        self.available_themes = self.themes.copy()
        self.selected_names = []

        self.center_frame = tk.Frame(root, borderwidth=self.frame_borderwidth, relief=tk.GROOVE)
        self.center_frame.pack(fill=tk.BOTH, expand=True)

        # Frame esquerdo (Sorteio de Nomes e Temas)
        self.left_frame = tk.Frame(self.center_frame, borderwidth=self.frame_borderwidth, relief=tk.GROOVE)
        self.left_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor='e')

        self.name_button = tk.Button(self.left_frame, text="Sortear Nome", command=self.pick_name, font=self.button_font_size, height=2)
        self.name_button.grid(row=0, column=0, padx=5)

        self.restart_button = tk.Button(self.left_frame, text="Reiniciar Sorteio", command=self.restart_sorting, font=self.button_font_size, height=2)
        self.restart_button.grid(row=0, column=1, padx=5)

        self.names_selected_listbox = tk.Listbox(self.left_frame, font=("Helvetica", 30), height=4, width=25)
        self.names_selected_listbox.grid(row=1, columnspan=2, pady=10)

        self.theme_button = tk.Button(self.left_frame, text="Sortear Tema", command=self.pick_theme, font=self.button_font_size, height=2)
        self.theme_button.grid(row=3, columnspan=2, pady=10)

        self.theme_listbox = tk.Listbox(self.left_frame, font=("Helvetica", 30), height=6, width=25)
        self.theme_listbox.grid(row=4, columnspan=2, pady=10)

        # Frame central (Rótulos de Tempo)
        self.timer_frame = tk.Frame(self.center_frame, borderwidth=self.frame_borderwidth, relief=tk.GROOVE)
        self.timer_frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.timer_label = tk.Label(self.timer_frame, text="Tempo restante:", font=self.custom_font)
        self.timer_label.pack()

        self.time_left = tk.StringVar()
        self.time_left.set("0:00")  # Defina o tempo inicial como "0:00"
        self.timer_display = tk.Label(self.timer_frame, textvariable=self.time_left, font=("Helvetica", 230))
        self.timer_display.pack()

        # Frame direito (Botões de Tempo)
        self.right_frame = tk.Frame(self.center_frame, borderwidth=self.frame_borderwidth, relief=tk.GROOVE)
        self.right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

        self.timer_button_5 = tk.Button(self.right_frame, text="5 Minutos", command=lambda: self.set_timer(5 * 60), font=self.button_font_size, height=2)
        self.timer_button_5.pack(fill=tk.Y, pady=(50, 0))

        self.timer_button_2 = tk.Button(self.right_frame, text="2 Minutos", command=lambda: self.set_timer(2 * 60), font=self.button_font_size, height=2)
        self.timer_button_2.pack(fill=tk.Y, pady=0)

        self.timer_button_1 = tk.Button(self.right_frame, text="1 Minuto", command=lambda: self.set_timer(1 * 60), font=self.button_font_size, height=2)
        self.timer_button_1.pack(fill=tk.Y, pady=0)

        self.timer_add_10_button = tk.Button(self.right_frame, text="+10 Segundos", command=self.add_10_seconds, font=self.button_font_size, height=2)
        self.timer_add_10_button.pack(fill=tk.Y, pady=0)

        self.timer_pause_button = tk.Button(self.right_frame, text="Pause", command=self.pause_timer, font=self.button_font_size, height=2, state=tk.DISABLED)
        self.timer_pause_button.pack(fill=tk.Y, pady=0)

        self.timer_resume_button = tk.Button(self.right_frame, text="Play", command=self.resume_timer, font=self.button_font_size, height=2, state=tk.DISABLED)
        self.timer_resume_button.pack(fill=tk.Y, pady=0)

        self.timer_stop_button = tk.Button(self.right_frame, text="Stop", command=self.stop_timer, font=self.button_font_size, height=2, state=tk.DISABLED)
        self.timer_stop_button.pack(fill=tk.Y, pady=(0, 50))

        self.timer_warning_sound_played = False
        self.timer_end_sound_played = False
        self.update_timer_id = None

        self.timer_running = False
        self.timer_paused = False
        self.paused_time = 0
        self.end_time = 0

    def pick_name(self):
        if self.names:
            random_name = random.choice(self.names)
            self.names_selected_listbox.insert(tk.END, f"  {self.name_counter}: {random_name}")
            self.selected_names.append(random_name)
            self.names.remove(random_name)
            self.name_counter += 1
        else:
            self.names_selected_listbox.insert(tk.END, "Todos os nomes sorteados!")

    def restart_sorting(self):
        self.names.extend(self.selected_names)
        self.selected_names = []
        self.names_selected_listbox.delete(0, tk.END)
        self.name_counter = 1

    def pick_theme(self):
        if self.available_themes:
            random_theme = random.choice(self.available_themes)
            self.available_themes.remove(random_theme)
            self.theme_listbox.insert(tk.END, f"  {self.theme_counter}: {random_theme}")
            self.theme_counter += 1
        else:
            self.theme_listbox.insert(tk.END, "Todos os temas sorteados!")

    def set_timer(self, seconds):
        self.timer_label.config(text="Tempo restante:")
        if not self.timer_running:
            self.end_time = time.time() + seconds
            self.timer_running = True
            self.timer_paused = False
            self.update_timer()
            self.timer_pause_button.config(state=tk.NORMAL)
            self.timer_resume_button.config(state=tk.DISABLED)
            self.timer_add_10_button.config(state=tk.NORMAL)
            self.timer_stop_button.config(state=tk.NORMAL)
        else:
            self.end_time = time.time() + seconds
            self.timer_running = True
            self.timer_paused = False
            self.update_timer()

    def add_10_seconds(self):
        if self.timer_paused or self.timer_running:
            self.end_time += 10
            self.update_timer()

    def pause_timer(self):
        if self.timer_running and not self.timer_paused:
            self.timer_paused = True
            self.paused_time = self.end_time - time.time()
            self.timer_pause_button.config(state=tk.DISABLED)
            self.timer_resume_button.config(state=tk.NORMAL)
            self.timer_stop_button.config(state=tk.NORMAL)
            if self.update_timer_id:
                self.root.after_cancel(self.update_timer_id)

    def resume_timer(self):
        if self.timer_paused:
            self.timer_paused = False
            self.end_time = time.time() + self.paused_time
            self.timer_pause_button.config(state=tk.NORMAL)
            self.timer_resume_button.config(state=tk.DISABLED)
            self.timer_stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.timer_paused = False
            self.timer_pause_button.config(state=tk.DISABLED)
            self.timer_resume_button.config(state=tk.DISABLED)
            self.timer_stop_button.config(state=tk.DISABLED)
            self.timer_add_10_button.config(state=tk.DISABLED)
            self.timer_label.config(text="Tempo parado")
            self.time_left.set("0:00")
            if self.update_timer_id:
                self.root.after_cancel(self.update_timer_id)

    def update_timer(self):
        if self.timer_running:
            if self.timer_paused:
                remaining_time = self.paused_time
            else:
                remaining_time = self.end_time - time.time()

            if remaining_time <= 0:
                self.timer_label.config(text="Tempo acabou!")
                if not self.timer_end_sound_played:
                    self.play_end_sound()
                    self.timer_end_sound_played = True
                self.timer_running = False
                self.timer_pause_button.config(state=tk.DISABLED)
                self.timer_resume_button.config(state=tk.DISABLED)
                self.timer_stop_button.config(state=tk.DISABLED)
                self.timer_add_10_button.config(state=tk.DISABLED)
            else:
                mins, secs = divmod(int(remaining_time), 60)
                self.time_left.set(f"{mins:01d}:{secs:02d}")
                if remaining_time <= 10 and not self.timer_warning_sound_played:
                    self.play_warning_sound()
                    self.timer_warning_sound_played = True
                self.update_timer_id = self.root.after(1000, self.update_timer)
        else:
            self.time_left.set("0:00")

    def play_warning_sound(self):
        winsound.Beep(600, 1000)

    def play_end_sound(self):
        winsound.Beep(440, 500)
        winsound.Beep(440, 500)

root = tk.Tk()
app = Application(root)
root.mainloop()
