mport tkinter as tk
from tkinter import messagebox, ttk
import random
import math

class SimonDice:
    def __init__(self, master):
        self.master = master
        self.master.title("Simon Says")
        self.master.geometry("700x800")
        
        self.colors = ["blue", "green", "red", "yellow", "purple"]
        self.light_colors = ["light blue", "light green", "pink", "khaki", "plum"]
        self.buttons = []
        self.sequence = []
        self.player_sequence = []
        self.is_player_turn = False
        self.high_score = 0
        self.difficulty = tk.StringVar(value="Medium")
        self.difficulties = {
            "Easy": 1.5,
            "Medium": 1.0,
            "Hard": 0.5
        }

        self.create_difficulty_selector()
        self.create_buttons()
        self.create_control_buttons()
        self.create_score_labels()

    def create_difficulty_selector(self):
        difficulty_frame = tk.Frame(self.master)
        difficulty_frame.pack(pady=10)

        tk.Label(difficulty_frame, text="Difficulty:", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
        difficulty_combo = ttk.Combobox(difficulty_frame, textvariable=self.difficulty, 
                                        values=list(self.difficulties.keys()), state="readonly", font=("Arial", 12))
        difficulty_combo.pack(side=tk.LEFT, padx=5)
        difficulty_combo.set("Medium")

    def create_buttons(self):
        button_frame = tk.Frame(self.master)
        button_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        canvas_size = 600
        self.canvas = tk.Canvas(button_frame, width=canvas_size, height=canvas_size)
        self.canvas.pack()

        center_x, center_y = canvas_size // 2, canvas_size // 2
        radius = 200
        angle = -math.pi / 2  # Start from the top

        for i, color in enumerate(self.colors):
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            pentagon = self.create_pentagon(self.canvas, x, y, 80, color, self.light_colors[i])
            self.canvas.tag_bind(pentagon, '<Button-1>', lambda event, c=color, idx=i: self.button_click(c, idx))
            
            self.buttons.append(pentagon)
            angle += 2 * math.pi / 5

    def create_pentagon(self, canvas, x, y, size, color, light_color):
        points = []
        for i in range(5):
            angle = i * 2 * math.pi / 5 - math.pi / 2
            points.extend([x + size * math.cos(angle), y + size * math.sin(angle)])
        
        pentagon = canvas.create_polygon(points, fill=color, outline='black', tags='pentagon')
        canvas.tag_bind(pentagon, '<Enter>', lambda e: canvas.itemconfig(pentagon, fill=light_color))
        canvas.tag_bind(pentagon, '<Leave>', lambda e: canvas.itemconfig(pentagon, fill=color))
        return pentagon

    def create_control_buttons(self):
        control_frame = tk.Frame(self.master)
        control_frame.pack(pady=10)

        self.start_button = tk.Button(control_frame, text="Start Game", command=self.start_game, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.continue_button = tk.Button(control_frame, text="Continue", command=self.continue_game, font=("Arial", 14), state=tk.DISABLED)
        self.continue_button.pack(side=tk.LEFT, padx=10)

    def create_score_labels(self):
        score_frame = tk.Frame(self.master)
        score_frame.pack(pady=10)

        self.score_label = tk.Label(score_frame, text="Current Score: 0", font=("Arial", 18))
        self.score_label.pack(side=tk.LEFT, padx=10)

        self.high_score_label = tk.Label(score_frame, text="High Score: 0", font=("Arial", 18))
        self.high_score_label.pack(side=tk.LEFT, padx=10)

    def start_game(self):
        self.sequence = []
        self.player_sequence = []
        self.continue_game()
        self.start_button.config(state=tk.DISABLED)

    def continue_game(self):
        self.continue_button.config(state=tk.DISABLED)
        self.add_to_sequence()

    def add_to_sequence(self):
        self.sequence.append(random.choice(self.colors))
        self.display_sequence()

    def display_sequence(self):
        self.is_player_turn = False
        
        def flash_button(index=0):
            if index < len(self.sequence):
                color = self.sequence[index]
                button = self.buttons[self.colors.index(color)]
                self.canvas.itemconfig(button, fill=self.light_colors[self.colors.index(color)])
                self.master.after(int(500 * self.difficulties[self.difficulty.get()]), 
                                  lambda: self.canvas.itemconfig(button, fill=color))
                self.master.after(int(750 * self.difficulties[self.difficulty.get()]), 
                                  lambda: flash_button(index + 1))
            else:
                self.is_player_turn = True

        self.master.after(1000, flash_button)

    def button_click(self, color, index):
        if not self.is_player_turn:
            return

        # Flash effect when button is clicked
        button = self.buttons[index]
        self.canvas.itemconfig(button, fill=self.light_colors[index])
        self.master.after(200, lambda: self.canvas.itemconfig(button, fill=self.colors[index]))

        self.player_sequence.append(color)
        if self.player_sequence[-1] != self.sequence[len(self.player_sequence) - 1]:
            self.game_over()
        elif len(self.player_sequence) == len(self.sequence):
            current_score = len(self.sequence)
            self.score_label.config(text=f"Current Score: {current_score}")
            if current_score > self.high_score:
                self.high_score = current_score
                self.high_score_label.config(text=f"High Score: {self.high_score}")
            self.player_sequence = []
            self.continue_button.config(state=tk.NORMAL)

    def game_over(self):
        messagebox.showinfo("Game Over", f"Game Over! Your final score is: {len(self.sequence) - 1}")
        self.start_button.config(state=tk.NORMAL)
        self.continue_button.config(state=tk.DISABLED)
        self.score_label.config(text="Current Score: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = SimonDice(root)
    root.mainloop()
