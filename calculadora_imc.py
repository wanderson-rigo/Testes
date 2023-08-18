import tkinter as tk

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
window.geometry("300x200")

# Widgets
altura_label = tk.Label(window, text="Altura (m):")
altura_label.pack(pady=5)
altura_entry = tk.Entry(window)
altura_entry.pack(pady=5)
altura_entry.insert(0, '1.74')

peso_label = tk.Label(window, text="Peso (kg):")
peso_label.pack(pady=5)
peso_entry = tk.Entry(window)
peso_entry.pack(pady=5)

calcular_button = tk.Button(window, text="Calcular IMC", command=calcular_imc)
calcular_button.pack(pady=10)

resultado_label = tk.Label(window, text="IMC: ", font=("Arial", 14))
resultado_label.pack(pady=5)

# Loop principal da aplicação
window.mainloop()