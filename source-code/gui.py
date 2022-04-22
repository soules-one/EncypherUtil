from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import fileinput
import Encypher_Crypto_module as ECM





def update_label(l, text, var):
    for i in l:
        i.config(text=text.format(var))


def update_state():
    global state_var
    global RSA_mode
    if RSA_mode.get() == "2":
        for i in f2_btn:
            i.config(state=DISABLED)
        for i in f3_btn:
            i.config(state=DISABLED)
    else:
        for i in f2_btn:
            i.config(state=NORMAL)
        for i in f3_btn:
            i.config(state=NORMAL)


def set_frame0(event):
    replace_frame(frame0)


def set_frame1(event):
    replace_frame(frame1)


def set_frame2(event):
    replace_frame(frame2)


def set_frame3(event):
    replace_frame(frame3)


def set_frame_keys(event):
    replace_frame(frame_keys)
    

def set_frame_info(event):
    replace_frame(frame_info)


def replace_frame(func_frame):
    global active_frame
    if active_frame == func_frame:
        pass
    else:
        func_frame.pack(side="right", fill=BOTH, expand=TRUE)
        active_frame.pack_forget()
        active_frame = func_frame
    

def _open(event):
    global read_file
    global read_btn
    read_file = askopenfilename()
    update_label(read_btn, "Файл для шифрования - {0}", read_file)


def _open_par(event):
    global par_file
    global par_btn
    par_file = askopenfilename()
    update_label(par_btn, "Файл параметров - {0}", par_file)


def _open_RSA_private(event):
    global RSA_private
    global RSA_private_btn
    RSA_private = askopenfilename()
    update_label(RSA_private_btn, "Файл приватного ключа - {0}" , RSA_private)
    

def _open_RSA_public(event):
    global RSA_public
    global RSA_public_btn
    RSA_public = askopenfilename()
    update_label(RSA_public_btn, "Файл публичного ключа - {0}", RSA_public)


def _save(event):
    global save_file
    global save_btn
    files = [("Все файлы", "*.*"), ("Текст", "*.txt")]
    save_file = asksaveasfilename()
    update_label(save_btn, "Конечный файл - {0}", save_file)


def _save_par(event):
    global par_file
    global par_btn
    par_file = asksaveasfilename()
    update_label(par_btn, "Файл параметров - {0}", par_file)
    
    
def _save_RSA_private(event):
    global RSA_private
    global RSA_private_btn
    RSA_private = asksaveasfilename()
    update_label(RSA_private_btn, "Файл приватного ключа - {0}", RSA_private)
    
    
def _save_RSA_public(event):
    global RSA_public
    global RSA_public_btn
    RSA_public = asksaveasfilename()
    update_label(RSA_public_btn, "Файл публичного ключа - {0}", RSA_public)


def open_button(window, com):
    btn = Button(window, text="Выбрать файл", padx=20)
    btn["font"] = "Arial 11"
    btn.bind("<Button-1>", com)
    return btn


def save_button(window, com):
    btn = Button(window, text="Сохранить как", padx=20)
    btn["font"] = "Arial 11"
    btn.bind("<Button-1>", com)
    return btn


def read_clear(event):
    global read_file
    read_file = "Не выбрано"
    update_label(read_btn, "Файл для шифрования - {0}", read_file)


def par_clear(event):
    global par_file
    par_file = "Не выбрано"
    update_label(par_btn, "Файл параметров - {0}", par_file)


def save_clear(event):
    global save_file
    save_file = "Не выбрано"
    update_label(save_btn, "Конечный файл - {0}", save_file)


def RSA_private_clear(event):
    global RSA_private
    RSA_private = "Не выбрано"
    update_label(RSA_private_btn, "Файл приватного ключа - {0}", RSA_private)


def RSA_public_clear(event):
    global RSA_public
    RSA_public = "Не выбрано"
    update_label(RSA_public_btn, "Файл публичного ключа - {0}", RSA_public)


def clear_button(window, com):
    btn = Button(window, text="Убрать значение")
    btn["font"] = "Arial 11"
    btn.bind("<Button-1>", com)
    return btn


def panel_simple(window, var):
    global state_var
    mode_sel_lbl = Label(window, pady=5, text="Выберите режим шифрования:", font="Calibri 14")
    mode_sel = Frame(window, pady=5, borderwidth=1, relief=SUNKEN)
    EAX_btn = Radiobutton(mode_sel, text="EAX", variable=var, value="EAX")
    EAX_btn["font"] = "Arial 11"
    GCM_btn = Radiobutton(mode_sel, text="GCM", variable=var, value="GCM")
    GCM_btn["font"] = "Arial 11"
    OCB_btn = Radiobutton(mode_sel, text="OCB", variable=var, value="OCB")
    OCB_btn["font"] = "Arial 11"
    CBC_btn = Radiobutton(mode_sel, text="CBC", variable=var, value="CBC")
    CBC_btn["font"] = "Arial 11"
    mode_sel_lbl.pack(fill=X, expand=TRUE)
    for i in range(4):
        mode_sel.columnconfigure(i, weight=1, minsize=30)
    EAX_btn.grid(row=0, column=0, padx=3, pady=3)
    GCM_btn.grid(row=0, column=1, padx=3, pady=3)
    OCB_btn.grid(row=0, column=2, padx=3, pady=3)
    CBC_btn.grid(row=0, column=3, padx=3, pady=3)
    mode_sel.pack(fill=X, expand=TRUE)
    return EAX_btn, GCM_btn, OCB_btn, CBC_btn


def add_panel_simple(window, var):
    panel_simple(window, var)
    return None


def add_panel_fk(window, var):
    mode_sel_lbl = Label(window, pady=5, text="Выберите операцию:", font="Calibri 14")
    mode_sel = Frame(window, pady=5, borderwidth=1, relief=SUNKEN)
    fst_btn = Radiobutton(mode_sel, text="Создание пары\nпубличный/приватный ключ", variable=var, value="1")
    fst_btn["font"] = "Arial 11"
    snd_btn = Radiobutton(mode_sel, text="Получение публичного ключа", variable=var, value="2")
    snd_btn["font"] = "Arial 11"
    mode_sel_lbl.pack(fill=X, expand=TRUE)
    for i in range(2):
        mode_sel.columnconfigure(i, weight=1, minsize=30)
    fst_btn.grid(row=0, column=0, padx=3, pady=3)
    snd_btn.grid(row=0, column=1, padx=3, pady=3)
    mode_sel.pack(fill=X, expand=TRUE)


def add_panel_f2(window, var):
    mode_sel_lbl = Label(window, pady=5, text="Выберите операцию:", font="Calibri 14")
    mode_sel = Frame(window, pady=5, borderwidth=1, relief=SUNKEN)
    fst_btn = Radiobutton(mode_sel, text="Шифрование RSA + AES", variable=var, value="1", command=update_state)
   # fst_btn.bind("<Button-1>", update_state)
    fst_btn["font"] = "Arial 11"
    snd_btn = Radiobutton(mode_sel, text="Шифрование RSA", variable=var, value="2", command=update_state)
    #snd_btn.bind("<Button-1>", update_state)
    snd_btn["font"] = "Arial 11"

    mode_sel_lbl.pack(fill=X, expand=TRUE)
    for i in range(2):
        mode_sel.columnconfigure(i, weight=1, minsize=30)
    fst_btn.grid(row=0, column=0, padx=3, pady=3)
    snd_btn.grid(row=0, column=1, padx=3, pady=3)
    mode_sel.pack(fill=X, expand=TRUE)


def two_button_frame(main_frame, first_button, com0, com1):
    frame = Frame(main_frame, pady=5, borderwidth=1, relief=SUNKEN)
    btn0 = first_button(frame, com0)
    space0 = Label(frame, text=" "*30, padx=10)
    space1 = Label(frame, text=" "*5, padx=10)
    space2 = Label(frame, text=" "*5, padx=10)
    btn1 = clear_button(frame, com1)
    space1.pack(side="left")
    btn0.pack(side="left", fill=X, expand=TRUE)
    space0.pack(side="left")
    btn1.pack(side="left", fill=X, expand=TRUE)
    space2.pack(side="left")
    return frame


def password_frame(main_frame):
    global pass_string
    frame = Frame(main_frame, pady=5, borderwidth=1, relief=SUNKEN)
    lbl = Label(frame, text="Пароль (до 16 символов):", font="Colibri 12")
    ent = Entry(frame, textvariable=pass_string, show="*", font="Arial 11")
    lbl.pack()
    ent.pack()
    return frame


def create_top_info():
    # frame_info

    global root
    ti= Toplevel()
    ti.minsize(500, 300)
    ti.maxsize(500, 300)
    ti.attributes("-topmost", "true")
    x = root.winfo_x()
    y = root.winfo_y()
    ti.geometry("+%d+%d" % (x + 100, y + 100))




    fi_header = Label(ti, pady=5, text="О программе\n", font="Colibri 16")
    fi_name = Label(ti, pady=5, text="EncypherUtil ©Egor Yakubovich\nLicensed under GNU GPL V3 license", font="Arial 12")
    fi_lbl = Label(ti, pady=5, anchor=N ,text="EncypherUtil - криптографическая\
 программа,\nнаписанная на языке Python 3 с использованием Pycryptodome и Tkinter\nhttps://codeberg.org/soules-one", font="Arial 11")
    fi_header.pack()
    fi_name.pack()
    fi_lbl.pack()
    return ti


def get_top_info(event):
    global top_info
    try:
        a = top_info.state()
        if a != "normal":
            top_info.deiconify()
    except:
        top_info = create_top_info()


def create_top_help():

    global root
    th = Toplevel()
    x = root.winfo_x()
    y = root.winfo_y()
    th.geometry("+%d+%d" % (x + 50, y + 50))
    th.minsize(750, 300)
    th.title("Основы работы с программой")

    global help_text
    # frame_help
    fh_frm = Text(th, relief=SUNKEN, borderwidth=1, exportselection=0,
                  font = "Arial 12", wrap=WORD, spacing3=3)
    fh_frm.insert(INSERT, help_text)
    fh_frm.tag_add("h1", "1.0", "1.32")
    fh_frm.tag_add("h2", "3.0", "3.28")
    fh_frm.tag_add("h3", "7.0", "7.28")
    fh_frm.tag_add("h4", "11.0", "11.21")
    fh_frm.tag_config("h1", justify=CENTER, font="Colibri 16")
    fh_frm.tag_config("h2", justify=CENTER, font="Colibri 14")
    fh_frm.tag_config("h3", justify=CENTER, font="Colibri 14")
    fh_frm.tag_config("h4", justify=CENTER, font="Colibri 14")
    fh_frm.pack(side = LEFT, fill = BOTH, expand=TRUE)
    fh_scrl = Scrollbar(th, orient=VERTICAL,  command = fh_frm.yview)
    fh_scrl.pack(side = RIGHT, fill = Y)
    fh_frm["yscrollcommand"] = fh_scrl.set
    fh_frm.config(state=DISABLED)
    
    

    return th


def get_top_help(event):
    global top_help
    try:
        a = top_help.state()
        if a != "normal":
            top_help.deiconify()
    except:
        top_help = create_top_help()


def start_func_AES(func):
    if "Не выбрано" in (read_file, save_file) or "" in (read_file, save_file):
        return messagebox.showwarning("ВНИМАНИЕ!", "Не были выбраны все необходимые параметры!")
    try:
        global var
        mode = ECM.mode_selector(var.get())
        if par_file in ("Не выбрано", ""):
            func(read_file, save_file, par_name="", mode=mode, password=pass_string.get())
        else:
            func(read_file, save_file, par_name=par_file, mode=mode, password=pass_string.get())
        return messagebox.showinfo("Успешно", "Операция успешно выполнена!")
    except:
        return messagebox.showerror("Ошибка", "При выполнении программы произошла ошибка!")


def f0_start(event):
    start_func_AES(ECM.p_encrypt_start)


def f1_start(event):
    start_func_AES(ECM.p_decrypt_start)


def start_func_keys(func):
    if "Не выбрано" in (RSA_public, RSA_private) or "" in (RSA_public, RSA_private):
        return messagebox.showwarning("ВНИМАНИЕ!", "Не были выбраны все необходимые параметры!")
    try:
        func(RSA_private, RSA_public, pass_string.get())
        return messagebox.showinfo("Успешно", "Операция успешно выполнена!")
    except:
        return messagebox.showerror("Ошибка", "При выполнении программы произошла ошибка!")


def fk_start(event):
    if keys_op_mode.get() == "1":
        start_func_keys(ECM.keys_creation)
    elif keys_op_mode.get() == "2":
        start_func_keys(ECM.keys_get_public)


def f2_start(event):
    if "Не выбрано" in (RSA_public, save_file, read_file) or "" in (RSA_public, save_file, read_file):
        return messagebox.showwarning("ВНИМАНИЕ!", "Не были выбраны все необходимые параметры!")
    try:
        if RSA_mode.get() == "1":
            global var
            mode = ECM.mode_selector(var.get())
            ECM.keys_encryption_aes(read_file, save_file, RSA_public, mode)
        elif RSA_mode.get() == "2":
            ECM.keys_encryption_rsa(read_file, save_file, RSA_public)
        return messagebox.showinfo("Успешно", "Операция успешно выполнена!")
    except:
        return messagebox.showerror("Ошибка", "При выполнении программы произошла ошибка!")


def f3_start(event):
    if "Ну выбрано" in (RSA_private, save_file, read_file) or "" in (RSA_private, save_file, read_file):
        return messagebox.showwarning("ВНИМАНИЕ!", "Не были выбраны все необходимые параметры!")
    try:
        if RSA_mode.get() == "1":
            global var
            ECM.keys_decryption_aes(read_file, save_file, RSA_private, pass_string.get(), var.get())
        elif RSA_mode.get() == "2":
            ECM.keys_encryption_rsa(read_file, save_file, RSA_private, pass_string.get())
        return messagebox.showinfo("Успешно", "Операция успешно выполнена!")
    except:
        return messagebox.showerror("Ошибка", "При выполнении программы произошла ошибка!")
    


help_text = """О принципах работы с программой
В левой части экрана находится панель с кнопками переключаения режимов работы программы, в правой - рабочее пространство. Нажимая на кнопку, вы меняете рабоочее пространство. Все операции, необходимые для выполнения операции, расположены последовательно. Вам лишь необходимо выполнить их сверху вниз, дойдя до кнопки "Выполнить".
Шифрование/дешифрование AES
При шифровании AES вам необходимо выбрать режим подачи данных. Все, кроме CBC используют систему аунтефикации данных, что позволяет удостоверится в неизменности данных, но усложняет расшифровку.
В файл параметров записываются данные,необходимые для дешифроврования. Если вы зашифруете данные без файлов параметров, то параметры шифрования будут записанны в конечный файл, и данные можно будет дешифровать, введя лишь пароль.
Пароль должен быть не длинее 16 символов(в противном случае, лишние символы будут отброшены).Если не указать пароль при шифровании, то будет сгенерирован случайный ключ шифрования. Если вы не укажете пароль и не создадите файл параметров. Пароль будет сохранён в папке с зашифрованным файлом в виде файла "название_конечного_файла_key.txt"
Шифрование/дешифрование RSA
При шифровании RSA используется уникальная пара приватный/публичный ключ. Создать их можно в пространстве "Работа с ключами RSA" (подробнее о них в разделе "Работа с ключами RSA").
При шифровании RSA можно использовать систему RSA+AES или только RSA. В случае шифрования системой RSA+AES, ключ шифрования файла случайный, а сам он зашифрован с помощью публичного ключа.
В случае шифрования RSA для шифрования потребуется только пара публичный/приватный ключ. Такой способ шифрования наиболее простой, но не очень эффективный так как ключи шифрования могут весить больше зашифрованного файла, и шифрование может занять много времени.
Работа с ключами RSA
Вы можете совершить две операции с ключами: создать пару приватный/публичный ключ и получить публичный ключ из приватного.
Публичный ключ используется при шифровании и может быть в свободном доступе. Приватный ключ используется для дешифрования и используется получателем. Доступ к нему требует пароля. Ключи хранятся в файле формата ".pem". Каждая пара ключей является уникальной (две пары с одинаковым паролем не являются идентичными). В случае утраты публичного ключа, его можно восстановить из приватного. В случае утраты приватного ключа, доступ к зашифрованным файлам будет потерян."""
root = Tk()
root.title("EncypherUtil")
root.minsize(width=750, height=600)
root.grid()
var = StringVar()
var.set("EAX")
# Создание виджетов
read_file = "Не выбрано"
par_file = "Не выбрано"
save_file = "Не выбрано"
RSA_public = "Не выбрано"
RSA_private = "Не выбрано"
state_var = NORMAL
RSA_mode = StringVar()
RSA_mode.set("1")
pass_string = StringVar()
keys_op_mode = StringVar()
keys_op_mode.set("1")


frame_btn = Frame(root, relief=SUNKEN, borderwidth=1, height=30)
frame0 = Frame(root, relief=SUNKEN, borderwidth=1)
frame1 = Frame(root, relief=SUNKEN, borderwidth=1)
frame2 = Frame(root, relief=SUNKEN, borderwidth=1)
frame3 = Frame(root, relief=SUNKEN, borderwidth=1)
frame_keys = Frame(root, relief=SUNKEN, borderwidth=1)
frame_info = Frame(root, relief=SUNKEN, borderwidth=1)
active_frame = frame0

# frame0
f0_header = Label(frame0, pady=5, text="Шифрование алгоритмом AES\n", font="Colibri 16")
f0_header.pack(fill=X, expand=TRUE)
add_panel_simple(frame0, var)
f0_read_file = Label(frame0, pady=5, text="Файл для шифрования - {0}".format(read_file), font="Arial 12")
f0_read_file.pack(fill=X, expand=TRUE)
f0_read_file_btn = two_button_frame(frame0, open_button, _open, read_clear)
f0_read_file_btn.pack(fill=X, expand=TRUE)
f0_par_file = Label(frame0, pady=5, text="Файл параметров - {0}".format(par_file), font="Arial 12")
f0_par_file_btn = two_button_frame(frame0, save_button, _save_par, par_clear)
f0_save_file = Label(frame0, pady=5, text="Конечный файл - {0}".format(save_file), font="Arial 12")
f0_save_file_btn = two_button_frame(frame0, save_button, _save, save_clear)
f0_par_file.pack(fill=X, expand=TRUE)
f0_par_file_btn.pack(fill=X, expand=TRUE)
f0_save_file.pack(fill=X, expand=TRUE)
f0_save_file_btn.pack(fill=X, expand=TRUE)
f0_start_btn = Button(frame0, text="Выполнить", padx=64)
f0_pass_string = password_frame(frame0)
f0_pass_string.pack(fill=X, expand=TRUE)
f0_space = Label(frame0, text="")
f0_start_btn["font"] = "Arial 14"
f0_start_btn.bind("<Button-1>", f0_start)
f0_start_btn.pack()
f0_space.pack()

# frame1
f1_header = Label(frame1, pady=5, text="Дешифрование алгоритмом AES\n", font="Colibri 16")
f1_header.pack(fill=X, expand=TRUE)
add_panel_simple(frame1, var)
f1_read_file = Label(frame1, pady=5, text="Файл для дешифрования - {0}".format(read_file), font="Arial 12")
f1_read_file.pack(fill=X, expand=TRUE)
f1_read_file_btn = two_button_frame(frame1, open_button, _open, read_clear)
f1_read_file_btn.pack(fill=X, expand=TRUE)
f1_par_file = Label(frame1, pady=5, text="Файл параметров - {0}".format(par_file), font="Arial 12")
f1_par_file_btn = two_button_frame(frame1, open_button, _open_par, par_clear)
f1_save_file = Label(frame1, pady=5, text="Конечный файл - {0}".format(save_file), font="Arial 12")
f1_save_file_btn = two_button_frame(frame1, save_button, _save, save_clear)
f1_par_file.pack(fill=X, expand=TRUE)
f1_par_file_btn.pack(fill=X, expand=TRUE)
f1_save_file.pack(fill=X, expand=TRUE)
f1_save_file_btn.pack(fill=X, expand=TRUE)
f1_start_btn = Button(frame1, text="Выполнить", padx=64)
f1_pass_string = password_frame(frame1)
f1_pass_string.pack(fill=X, expand=TRUE)
f1_space = Label(frame1, text="")
f1_start_btn["font"] = "Arial 14"
f1_start_btn.bind("<Button-1>", f1_start)
f1_start_btn.pack()
f1_space.pack()


# frame2
f2_header = Label(frame2, pady=5, text="Шифрование алгоритмом RSA\n", font="Colibri 16")
f2_header.pack(fill=X, expand=TRUE)
add_panel_f2(frame2, RSA_mode)
EAX2, GCM2, OCB2, CBC2 = panel_simple(frame2, var)
f2_btn = (EAX2, GCM2, OCB2, CBC2)

f2_read_file = Label(frame2, pady=5, text="Файл для шифрования - {0}".format(read_file), font="Arial 12")
f2_read_file.pack(fill=X, expand=TRUE)
f2_read_file_btn = two_button_frame(frame2, open_button, _open, read_clear)
f2_read_file_btn.pack(fill=X, expand=TRUE)
f2_key_file = Label(frame2, pady=5, text="Файл публичного ключа - {0}".format(RSA_public), font="Arial 12")
f2_key_file_btn = two_button_frame(frame2, open_button, _open_RSA_public, RSA_public_clear)
f2_save_file = Label(frame2, pady=5, text="Конечный файл - {0}".format(save_file), font="Arial 12")
f2_save_file_btn = two_button_frame(frame2, save_button, _save, save_clear)
f2_key_file.pack(fill=X, expand=TRUE)
f2_key_file_btn.pack(fill=X, expand=TRUE)
f2_save_file.pack(fill=X, expand=TRUE)
f2_save_file_btn.pack(fill=X, expand=TRUE)
f2_start_btn = Button(frame2, text="Выполнить", padx=64)
f2_space = Label(frame2, text="")
f2_start_btn["font"] = "Arial 14"
f2_start_btn.bind("<Button-1>", f2_start)
f2_start_btn.pack()
f2_space.pack()


# frame3
f3_header = Label(frame3, pady=5, text="Дешифрование алгоритмом RSA\n", font="Colibri 16")
f3_header.pack(fill=X, expand=TRUE)
add_panel_f2(frame3, RSA_mode)
EAX3, GCM3, OCB3, CBC3 = panel_simple(frame3, var)
f3_btn = (EAX3, GCM3, OCB3, CBC3)

f3_read_file = Label(frame3, pady=5, text="Файл для дешифрования - {0}".format(read_file), font="Arial 12")
f3_read_file.pack(fill=X, expand=TRUE)
f3_read_file_btn = two_button_frame(frame3, open_button, _open, read_clear)
f3_read_file_btn.pack(fill=X, expand=TRUE)
f3_key_file = Label(frame3, pady=5, text="Файл приватного ключа - {0}".format(RSA_private), font="Arial 12")
f3_key_file_btn = two_button_frame(frame3, open_button, _open_RSA_private, RSA_private_clear)
f3_save_file = Label(frame3, pady=5, text="Конечный файл - {0}".format(save_file), font="Arial 12")
f3_save_file_btn = two_button_frame(frame3, save_button, _save, save_clear)
f3_key_file.pack(fill=X, expand=TRUE)
f3_key_file_btn.pack(fill=X, expand=TRUE)
f3_save_file.pack(fill=X, expand=TRUE)
f3_save_file_btn.pack(fill=X, expand=TRUE)
f3_start_btn = Button(frame3, text="Выполнить", padx=64)
f3_pass_string = password_frame(frame3)
f3_pass_string.pack(fill=X, expand=TRUE)
f3_space = Label(frame3, text="")
f3_start_btn["font"] = "Arial 14"
f3_start_btn.bind("<Button-1>", f3_start)
f3_start_btn.pack()
f3_space.pack()


# frame_keys
fk_header = Label(frame_keys, pady=0, text="Работа с ключами RSA\n", font="Colibri 14")
fk_space1 = Label(frame_keys, text="")
fk_space2 = Label(frame_keys, text="")
fk_password= password_frame(frame_keys)
fk_private_save = Label(frame_keys, pady=0, text="Приватный ключ - {0}".format(RSA_private), font="Arial 12")
fk_private_save_btn = two_button_frame(frame_keys, save_button, _save_RSA_private, RSA_private_clear)
fk_public_save = Label(frame_keys, pady=0, text="Публичный ключ - {0}".format(RSA_public), font="Arial 12")
fk_public_save_btn = two_button_frame(frame_keys, save_button, _save_RSA_public, RSA_public_clear)
fk_start_btn = Button(frame_keys, text="Выполнить", padx=64)
fk_start_btn["font"] = "Arial 14"

fk_header.pack(fill=X, expand=TRUE, side="top")
add_panel_fk(frame_keys, keys_op_mode)
fk_password.pack(fill=X, expand=TRUE, side="top")
fk_private_save.pack(fill=X, expand=TRUE, side="top")
fk_private_save_btn.pack(fill=X, expand=TRUE, side="top")
fk_public_save.pack(fill=X, expand=TRUE, side="top")
fk_public_save_btn.pack(fill=X, expand=TRUE, side="top")
fk_start_btn.bind("<Button-1>", fk_start)
fk_start_btn.pack()
fk_space2.pack()


# frame_info



# frame_help


# Кнопки управления
but0 = Button(frame_btn, text="Шифрование AES", pady=5)
but0.bind("<Button-1>", set_frame0)
but1 = Button(frame_btn, text="Дешифрование AES", pady=5)
but1.bind("<Button-1>", set_frame1)
but2 = Button(frame_btn, text="Шифрование RSA", pady=5)
but2.bind("<Button-1>", set_frame2)
but3 = Button(frame_btn, text="Дешифрование RSA", pady=5)
but3.bind("<Button-1>", set_frame3)
but_keys = Button(frame_btn, text="Работа с\nключами RSA", pady=5)
but_keys.bind("<Button-1>", set_frame_keys)
but_help = Button(frame_btn, text="Помощь", pady=5)
but_help.bind("<Button-1>", get_top_help)
but_info = Button(frame_btn, text="О программе", pady=5)
but_info.bind("<Button-1>", get_top_info)

space1 = Label(frame_btn, pady=5, text="EncypherUtil v.0.0")
space2 = Label(frame_btn, pady=0, text=" ")
l_mode = Label(frame_btn, text="Выберите режим:", font="Calibri 14")

but0["font"] = "Arial 12"
but1["font"] = "Arial 12"
but2["font"] = "Arial 12"
but3["font"] = "Arial 12"
but_keys["font"] = "Arial 12"
but_help["font"] = "Arial 12"
but_info["font"] = "Arial 12"

frame_btn.pack(side="left", fill=Y)
active_frame.pack(side="right", fill=BOTH, expand=TRUE)

l_mode.pack(fill=X)
but0.pack(fill=X)
but1.pack(fill=X)
but2.pack(fill=X)
but3.pack(fill=X)
but_keys.pack(fill=X)

space1.pack(fill=X, side="bottom")
but_info.pack(fill=X, side="bottom")
space2.pack(fill=X, side="bottom")
but_help.pack(fill=X, side="bottom")

save_btn = (f0_save_file, f1_save_file, f2_save_file, f3_save_file)
par_btn = (f0_par_file, f1_par_file)
read_btn = (f0_read_file, f1_read_file, f2_read_file, f3_read_file)
RSA_private_btn = (fk_private_save, f3_key_file)
RSA_public_btn = (fk_public_save, f2_key_file)



root.mainloop()
