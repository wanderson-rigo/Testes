import tkinter as tk

def aumentar_altura():
    altura = float(altura_entry.get()) + 1
    altura_entry.delete(0, tk.END)
    altura_entry.insert(0, altura)

def diminuir_altura():
    altura = float(altura_entry.get()) - 1
    altura_entry.delete(0, tk.END)
    altura_entry.insert(0, altura)

def aumentar_peso():
    peso = float(peso_entry.get()) + 1
    peso_entry.delete(0, tk.END)
    peso_entry.insert(0, peso)

def diminuir_peso():
    peso = float(peso_entry.get()) - 1
    peso_entry.delete(0, tk.END)
    peso_entry.insert(0, peso)

def calcular_imc():
    try:
        altura = float(altura_entry.get())
        peso = float(peso_entry.get())
        
        imc = peso / (altura ** 2)
        resultado_label.config(text=f"IMC: {imc:.2f}")
    except ValueError:
        resultado_label.config(text="Erro: Insira valores válidos para altura e peso.")

# Configuração da janela principal
window = tk.Tk()
window.title("Calculadora de IMC")
window.geometry("400x300")

# Widgets
altura_label = tk.Label(window, text="Altura (m):")
altura_label.pack(pady=5)
altura_entry = tk.Entry(window)
altura_entry.insert(0, '1.73')
altura_entry.pack(pady=5)

altura_buttons_frame = tk.Frame(window)
aumentar_altura_button = tk.Button(altura_buttons_frame, text="Aumentar", command=aumentar_altura)
diminuir_altura_button = tk.Button(altura_buttons_frame, text="Diminuir", command=diminuir_altura)
aumentar_altura_button.pack(side="left", padx=5)
diminuir_altura_button.pack(side="right", padx=5)
altura_buttons_frame.pack()

peso_label = tk.Label(window, text="Peso (kg):")
peso_label.pack(pady=5)
peso_entry = tk.Entry(window)
peso_entry.insert(0, '60')
peso_entry.pack(pady=5)

peso_buttons_frame = tk.Frame(window)
aumentar_peso_button = tk.Button(peso_buttons_frame, text="Aumentar", command=aumentar_peso)
diminuir_peso_button = tk.Button(peso_buttons_frame, text="Diminuir", command=diminuir_peso)
aumentar_peso_button.pack(side="left", padx=5)
diminuir_peso_button.pack(side="right", padx=5)
peso_buttons_frame.pack()

calcular_button = tk.Button(window, text="Calcular IMC", command=calcular_imc)
calcular_button.pack(pady=10)

resultado_label = tk.Label(window, text="IMC: ", font=("Arial", 14))
resultado_label.pack(pady=5)

# Loop principal da aplicação
window.mainloop()
