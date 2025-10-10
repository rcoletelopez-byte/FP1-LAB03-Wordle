'''
Interfaz gráfica para el juego Wordle.
'''

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

from wordle_utils import es_palabra_valida, obtener_pistas, calcula_minutos_y_segundos

MAX_TRIES = 6
WORD_LEN = 5

COLOR_BG = "#1e1e1e"
COLOR_EMPTY = "#3a3a3c"   # gris
COLOR_A = "#b59f3b"       # amarillo
COLOR_V = "#538d4e"       # verde
COLOR_TEXT = "#eaeaea"

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)

class WordleWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("WORDLE-FP1")
        self.root.configure(bg=COLOR_BG)

        self.cells = []  
        self.setup_widgets()
        self.reset_game()

    def setup_widgets(self):
        # Título
        self.title_lbl = tk.Label(self.root, text="WORDLE-FP1", font=("Arial", 18, "bold"),
                                  bg=COLOR_BG, fg=COLOR_TEXT)
        self.title_lbl.pack(pady=8)

        # Tablero 6x5
        self.grid_frame = tk.Frame(self.root, bg=COLOR_BG)
        self.grid_frame.pack(pady=10)

        for r in range(MAX_TRIES):
            row = []
            for c in range(WORD_LEN):
                cell = tk.Label(self.grid_frame, text=" ", width=4, height=2,
                                font=("Consolas", 18, "bold"),
                                bg=COLOR_EMPTY, fg=COLOR_TEXT, bd=2, relief="ridge")
                cell.grid(row=r, column=c, padx=4, pady=4)
                row.append(cell)
            self.cells.append(row)

        # Entrada y botón
        self.entry = tk.Entry(self.root, font=("Consolas", 16), width=10, justify="center")
        self.entry.pack(pady=6)
        self.entry.focus_set()
        # Vincula el evento Enter a la función on_try
        self.entry.bind("<Return>", self.on_try)

        self.btn = tk.Button(self.root, text="Probar", font=("Arial", 12, "bold"),
                             command=self.on_try)
        self.btn.pack(pady=4)

        # Info
        self.info = tk.Label(self.root, text="Introduce una palabra de 5 letras.",
                             bg=COLOR_BG, fg=COLOR_TEXT, font=("Arial", 10))
        self.info.pack(pady=6)

    def reset_game(self):
        """Reinicia el estado del juego."""
        self.secret = elige_palabra()
        self.try_index = 0
        self.start_time = datetime.now()
        self.btn["state"] = "normal"
        self.entry.delete(0, tk.END)
        self.entry.focus_set()

        # Resetea el tablero
        for r in range(MAX_TRIES):
            for c in range(WORD_LEN):
                self.cells[r][c]["text"] = " "
                self.cells[r][c]["bg"] = COLOR_EMPTY

    def paint_row(self, r, attempt, fb):
        for c in range(WORD_LEN):
            ch = attempt[c] if c < len(attempt) else " "
            self.cells[r][c]["text"] = ch.upper()
            code = fb[c] if c < len(fb) else "_"
            if code == "V":
                self.cells[r][c]["bg"] = COLOR_V
            elif code == "A":
                self.cells[r][c]["bg"] = COLOR_A
            else:
                self.cells[r][c]["bg"] = COLOR_EMPTY

    def on_try(self, event=None):
        if self.try_index >= MAX_TRIES:
            return
        attempt = self.entry.get().strip().lower()
        if not es_palabra_valida(attempt):
            messagebox.showwarning("Aviso", "Palabra inválida. Debe tener 5 letras a-z.")
            return
        fb = obtener_pistas(self.secret, attempt)
        self.paint_row(self.try_index, attempt, fb)
        self.entry.delete(0, tk.END)
        self.try_index += 1

        if fb == "VVVVV":
            finish_time = datetime.now()
            minutos, segundos = calcula_minutos_y_segundos(self.start_time, finish_time)
            messagebox.showinfo("¡Bien!", "¡Has acertado la palabra!\nTiempo: " +
                                str(minutos) + " minutos y " + str(segundos) + " segundos.")
            self.reset_game()
        elif self.try_index == MAX_TRIES:
            messagebox.showinfo("Fin", "Agotaste intentos. La palabra era: " + self.secret)
            self.reset_game()

def main():
    root = tk.Tk()
    app = WordleWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
