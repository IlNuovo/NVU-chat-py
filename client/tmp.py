import tkinter as tk

def crea_scrollable_text():
    # Crea una finestra principale
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(fill="both", expand=True)

    # Crea una scrollbar verticale
    scrollbar = tk.Scrollbar(canvas_frame)
    scrollbar.pack(side="right", fill="y")

    # Crea il widget Text (per contenere il testo scorrevole)
    text_widget = tk.Text(canvas_frame, wrap="word", height=10, width=40)
    text_widget.pack(side="left", fill="both", expand=True)

    # Aggiungi la scrollbar al widget Text
    text_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_widget.yview)

    # Inserisci del testo lungo
    long_text = "Questo è un testo molto lungo che non sta nella finestra e deve essere fatto scorrere verticalmente per vederlo tutto.\n" * 5
    text_widget.insert("1.0", long_text)  # Inserisce il testo nel widget

# Crea la finestra principale
root = tk.Tk()
root.geometry("300x150")  # Imposta una dimensione fissa per la finestra

# Crea il Text scorrevole
crea_scrollable_text()

# Mostra la finestra
root.mainloop()
