'''
Окно входа и регистрации
Никонова Дарья ИСТбд-21
'''
import tkinter as tk

users = {}


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        login_successful()
    else:
        login_failed()

def login_successful():
    success_window = tk.Toplevel(root)
    success_window['bg'] = 'bisque'
    success_window.title("Войти")
    success_label = tk.Label(success_window, text="Вы успешно вошли.", font=("Helvetica", 14), bg = 'bisque')
    success_label.pack(padx=20, pady=10)

    # Центрируем окно успешного входа
    success_window.update_idletasks()
    width = success_window.winfo_width()
    height = success_window.winfo_height()
    x = (success_window.winfo_screenwidth() // 2) - (width // 2)
    y = (success_window.winfo_screenheight() // 2) - (height // 2)
    success_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def login_failed():
    error_window = tk.Toplevel(root)
    error_window['bg'] = 'bisque'
    error_window.title("Войти")
    error_label = tk.Label(error_window, text="Неправильное имя пользователя или пароль. Пожалуйста, попробуйте еще раз.", font=("Helvetica", 14), bg='bisque' )
    error_label.pack(padx=20, pady=10)

     # Центрируем окно ошибки входа
    error_window.update_idletasks()
    width = error_window.winfo_width()
    height = error_window.winfo_height()
    x = (error_window.winfo_screenwidth() // 2) - (width // 2)
    y = (error_window.winfo_screenheight() // 2) - (height // 2)
    error_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  

def register():
    username = username_entry.get()
    password = password_entry.get()

    if len(username) == 0 or len(password) == 0:
        registration_failed("Требуется имя пользователя и пароль.")
    elif username in users:
        registration_failed("Имя пользователя уже занято. Пожалуйста, выберите другое имя пользователя.")
    else:
        users[username] = password
        registration_successful()

def registration_successful():
    success_window = tk.Toplevel(root)
    success_window['bg'] = 'bisque'
    success_window.title("Регистрация")
    success_label = tk.Label(success_window, text="Вы успешно зарегистрировались.", font=("Helvetica", 14), bg='bisque')
    success_label.pack(padx=20, pady=10)

     # Центрируем окно успешной регистрации
    success_window.update_idletasks()
    width = success_window.winfo_width()
    height = success_window.winfo_height()
    x = (success_window.winfo_screenwidth() // 2) - (width // 2)
    y = (success_window.winfo_screenheight() // 2) - (height // 2)
    success_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    

def registration_failed(error_message):
    error_window = tk.Toplevel(root)
    error_window['bg'] = 'bisque'
    error_window.title("Регистрация")
    error_label = tk.Label(error_window, text=error_message, font=("Helvetica", 14), bg='bisque')
    error_label.pack(padx=20, pady=10)


     # Центрируем окно ошибки регистрации
    error_window.update_idletasks()
    width = error_window.winfo_width()
    height = error_window.winfo_height()
    x = (error_window.winfo_screenwidth() // 2) - (width // 2)
    y = (error_window.winfo_screenheight() // 2) - (height // 2)
    error_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root['bg'] = 'bisque'
root.title('Окно авторизации/регистрации')

title_label = tk.Label(root, text="Войдите или зарегистрируйтесь", font=("Helvetica", 24), bg='bisque')
title_label.pack(pady=20)

username_label = tk.Label(root, text="Имя пользователя:",bg='bisque')
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)
username_entry.focus()


password_label = tk.Label(root, text="Пароль:", bg='bisque')
password_label.pack()
password_entry = tk.Entry(root, show = "*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Войти", font=("Helvetica", 14), command=login, bg='peru', activebackground='burlywood')
login_button.pack(pady=10)

register_button = tk.Button(root, text="Зарегистрироваться", font=("Helvetica", 14), command=register, bg='peru', activebackground='burlywood')
register_button.pack(pady=10)


root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.mainloop()
