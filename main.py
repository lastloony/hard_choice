import tkinter as tk
from tkinter import messagebox
from random import choice, randint

def animate_random(values, steps=20):
    """Анимация выбора"""
    if steps > 0:
        val = choice(values)
        result_label.config(text=val, font=("Arial", 16, "bold"), fg="blue")
        root.after(50, animate_random, values, steps - 1)
    else:
        final_choice = choice(values)
        result_label.config(text=final_choice, fg="green")
        messagebox.showinfo("Результат", f"Выпало: {final_choice}")

def generate_random_value():
    input_text = input_field.get().strip()

    # Режим для чисел
    if mode_var.get() == "numbers":
        try:
            start, end = map(int, input_text.split("-"))
            if start > end:
                start, end = end, start
            values = [str(i) for i in range(start, end + 1)]
        except ValueError:
            messagebox.showerror("Ошибка", "Введите диапазон чисел в формате: 1-100")
            return
    else:
        # Режим для слов
        if not input_text:
            values = ["Да", "Нет"]
        else:
            values = [v.strip() for v in input_text.split(",") if v.strip()]
            if not values:
                values = ["Да", "Нет"]

    animate_random(values)

root = tk.Tk()
root.title("Hard choice")
root.geometry('500x300')

# Переключатель режима
mode_var = tk.StringVar(value="text")
tk.Label(root, text="Выберите режим:").pack()
tk.Radiobutton(root, text="Список значений", variable=mode_var, value="text").pack()
tk.Radiobutton(root, text="Диапазон чисел", variable=mode_var, value="numbers").pack()

label = tk.Label(root, text="Введите значения через запятую или диапазон чисел:")
label.pack(pady=5)

input_field = tk.Entry(root, width=50)
input_field.pack(pady=5)

generate_button = tk.Button(root, text="Выбрать", command=generate_random_value)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
