# Задача №49. 
# Создать  телефонный  справочник  с возможностью  импорта  и  экспорта  данных  в формате  .txt.  
# Фамилия,  имя,  отчество,  номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа  должна  сохранять  данные  в текстовом файле
# 3. Пользователь  может  ввести  одну  из характеристик  для  поиска  определенной записи
# (Например  имя  или  фамилию человека)
# 4. Использование  функций. Ваша программа не должна быть линейной

# 5. Дополнить телефонный справочник возможностью изменения и удаления данных.
# 6. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# 7. Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

import tkinter as tk
from tkinter import *
from tkinter import Tk, Menu, Button, PhotoImage, filedialog
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo


FIELD_CAPTIONS = ('Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание')


# вывод телефонной книги (список) или результатов поиска (словарь) на экран
def phone_book_print(phone_book, treeview):             
    if isinstance(phone_book, list):
        for i, phone_book_record in enumerate(phone_book, 1):                    
            treeview.insert("", END, i, values=tuple(phone_book_record.values()))  
    elif isinstance(phone_book, dict):
        for i, phone_book_record in phone_book.items():
            treeview.insert("", END, i + 1, values=tuple(phone_book_record.values()))              
    

# чтение файла и возврат телефонной книги в виде списка словарей
def phone_book_read_txt(filename, field_captions) -> list:        
    phone_book = []    
    with open(filename, 'r', encoding='utf-8') as file:     
        for line in file.readlines():            
            phone_book.append(dict(zip(field_captions, line[:-1].split(','))))            
    return phone_book


# запись отсортированной по возрастанию телефонной книги в файл
def phone_book_save_txt(phone_book, filename):            
    with open(filename, 'w', encoding='utf-8') as file:       
        file.writelines([f'{','.join(item.values())}\n' for item in sorted(phone_book, key=lambda x: tuple(x.values()))])
    

# добавление записи в телефонный справочник, 
# если запись со значением поля check_field существует, то возвращает -1
def phone_book_add_record(phone_book: list, new_record_data_str, field_captions, check_field):        
    new_record = dict(zip(field_captions, new_record_data_str.title().split()))
    is_record_exists = False
    for phone_book_record in phone_book:
        is_record_exists = new_record[check_field] == phone_book_record[check_field]
        if is_record_exists:
            break
    if not is_record_exists:
        phone_book.append(new_record)
        phone_book_sort(phone_book)
    else:
        return -1
           

# поиск записи в справочнике одновременно по всем полям по маске вида *значение* 
# с расчетом индексов для "подсветки" искомого значения,
# для версии с использованием tkinter - "подсветка" является преобразованием в прописные буквы,
# возвращаемое значение - словарь {сквозной номер строки (начиная с 0): запись справочника}
def phone_book_search(phone_book, mask_search_info_) -> dict:    
    search_info = mask_search_info_.replace('*', '')
        
    # назначаем функцию проверки элемента записи телефонного справочника на соответствие введенной маске,
    # возвращаем индекс начала искомой подстроки или -1 в случае отсутствия        
    if mask_search_info_.count('*') == 0:        
        check_mask_start_index = lambda x: 0 if str(x).lower() == search_info else -1
    elif mask_search_info_.startswith('*') and mask_search_info_.endswith('*'):                        
        check_mask_start_index = lambda x: x.lower().find(search_info)
    elif mask_search_info_.startswith('*'):                
        check_mask_start_index = lambda x: len(x) - len(search_info) if str(x).lower().endswith(search_info) else -1
    elif mask_search_info_.endswith('*'):            
        check_mask_start_index = lambda x: 0 if str(x).lower().startswith(search_info) else -1
        
    search_result = dict()
    for i_str, phone_book_record in enumerate(phone_book):                
        mask_start_indexes = dict(map(lambda item: (item[0], check_mask_start_index(item[1])), phone_book_record.items()))       
        if list(set(mask_start_indexes.values()))[0] != -1:
            phone_book_record_with_mask = dict()
            for field_caption, data in phone_book_record.items():                      
                if mask_start_indexes[field_caption] != -1:
                    index_start = mask_start_indexes[field_caption]
                    index_end = mask_start_indexes[field_caption] + len(search_info)                                    
                    phone_book_record_with_mask[field_caption] = f'{data[:index_start]}{data[index_start: index_end].upper()}{data[index_end:]}'                    
                else:
                    phone_book_record_with_mask[field_caption] = data            
            search_result[i_str] = phone_book_record_with_mask
    
    return search_result


# удаление записи из справочника по номеру строки
def phone_book_delete_record(phone_book, numrec2del_):
    return phone_book.pop(numrec2del_ - 1)


# проверка номера записи (нумерация начинается с 1) на наличие в справочнике
def phone_book_record_exists(phone_book, num_record):
    return 0 < num_record <= len(phone_book)


# сортировка телефонного справочника
def phone_book_sort(phone_book):
    phone_book.sort(key=lambda x: tuple(x.values()))


# изменение записи в телефонном справочнике
def phone_book_change_record(phone_book: list, numrec2edit_, new_record_data_str, field_captions):    
    phone_book[numrec2edit_ - 1] = dict(zip(field_captions, new_record_data_str.title().split()))
    phone_book_sort(phone_book)


# копирование записи в другой файл
def phone_book_record_copy2file(phone_book_src, numrec2copy_, filename_dest):            
    with open(filename_dest, 'a', encoding='utf-8') as file:             
        file.write(f'{','.join(phone_book_src[numrec2copy_ - 1].values())}\n')        
                

# "основная" функция
def phone_book_editor_tkinter():  

    # -------- вложенные функции оконного интерфейса -----------

    # формирование строки геометрии для создания окна по центру экрана
    def create_geometry_2_center_windows(window_width, window_height):           
        screen_width = main_window.winfo_screenwidth()
        screen_height = main_window.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height -window_height) // 2    
        return f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}'


    # команда главного меню и панели инструментов "Создать файл"
    def new_file(phone_book):               
        phone_book.clear()
        tree.delete(*tree.get_children())
        main_window.title(f'Телефонный справочник - Новый')


    # команда главного меню и панели инструментов "Открыть файл"
    def open_file(phone_book):            
        filename = filedialog.askopenfilename()
        if filename:                        
            phone_book.clear()
            phone_book += phone_book_read_txt(filename, FIELD_CAPTIONS)
            tree.delete(*tree.get_children())
            phone_book_print(phone_book, tree)
            main_window.title(f'Телефонный справочник - {filename}')


    # команда главного меню и панели инструментов "Сохранить файл"
    def save_file(phone_book):
        filename = filedialog.asksaveasfilename()
        if filename:
            phone_book_save_txt(phone_book, filename)


    # команда главного меню и панели инструментов "Удалить"
    def delete_record(phone_book):
        selected_row = int(tree.selection()[0])        
        deleted_record = phone_book_delete_record(phone_book_main, selected_row)
        tree.delete(*tree.get_children())
        phone_book_print(phone_book, tree)
        showinfo(title="Информация", message=f'Запись {deleted_record} удалена.')


    # команда главного меню и панели инструментов "Добавить"
    def add_record(phone_book):
        treeview_phone_record_card_add_edit(phone_book, 'add')


    # отображение карточки изменения данных при двойном клике на строке Treeview
    def treeview_OnDoubleClick(event):
        treeview_phone_record_card_add_edit(phone_book_main, 'edit')


    # функция работы с карточкой записи в зависимости от переданной команды (add/edit)
    def treeview_phone_record_card_add_edit(phone_book, command):
                
        # закрытие карточки изменения данных (Принять)
        def treeview_cardedit_ok(window_):         
            if command == 'edit':
                selected_row = int(tree.selection()[0])
                phone_book[selected_row - 1]['Фамилия'] = ent_lastname.get()
                phone_book[selected_row - 1]['Имя'] = ent_firstname.get()
                phone_book[selected_row - 1]['Отчество'] = ent_middlename.get()
                phone_book[selected_row - 1]['Телефон'] = ent_phonenumber.get()
                phone_book[selected_row - 1]['Описание'] = ent_description.get()            
                tree.item(selected_row, values=tuple(phone_book[selected_row - 1].values()))
            elif command == 'add':                
                new_record_data = f'{ent_lastname.get()} {ent_firstname.get()} {ent_middlename.get()} {ent_phonenumber.get()} {ent_description.get()}'
                if phone_book_add_record(phone_book, new_record_data, FIELD_CAPTIONS, 'Телефон') != -1:
                    tree.delete(*tree.get_children())
                    phone_book_print(phone_book, tree)
                    showinfo(title="Информация", message=f'Запись успешно добавлена.')                    
                else:
                    showerror(title="Информация", message=f'Такая запись уже существует!')                                                
            treeview_cardedit_close(window_)

        # закрытие карточки изменения данных (Отменить)
        def treeview_cardedit_close(window_):
            window_.grab_release() 
            window_.destroy()

        window = Toplevel() 
        if command == 'edit':
            window.title("Изменить запись")
        elif command == 'add':
            window.title("Добавить запись")
        window.geometry(create_geometry_2_center_windows(376, 143))
        window.update_idletasks()        
        
        lbl_lastname = tk.Label(master=window, text="Фамилия:")
        ent_lastname = tk.Entry(master=window, width=50)        
        lbl_lastname.grid(row=0, column=0, sticky="e")
        ent_lastname.grid(row=0, column=1)
        lbl_firstname = tk.Label(master=window, text="Имя:")
        ent_firstname = tk.Entry(master=window, width=50)        
        lbl_firstname.grid(row=1, column=0, sticky="e")
        ent_firstname.grid(row=1, column=1)
        lbl_middlename = tk.Label(master=window, text="Отчество:")
        ent_middlename = tk.Entry(master=window, width=50)        
        lbl_middlename.grid(row=2, column=0, sticky="e")
        ent_middlename.grid(row=2, column=1)
        lbl_phonenumber = tk.Label(master=window, text="Телефон:")
        ent_phonenumber = tk.Entry(master=window, width=50)        
        lbl_phonenumber.grid(row=3, column=0, sticky="e")
        ent_phonenumber.grid(row=3, column=1)
        lbl_description = tk.Label(master=window, text="Описание:")
        ent_description = tk.Entry(master=window, width=50)        
        lbl_description.grid(row=4, column=0, sticky="e")
        ent_description.grid(row=4, column=1)
        
        if command == 'edit' and len(tree.selection()):
            selected_row = int(tree.selection()[0])            
            ent_lastname.insert(0, f'{phone_book[selected_row - 1]['Фамилия']}')
            ent_firstname.insert(0, f'{phone_book[selected_row - 1]['Имя']}')
            ent_middlename.insert(0, f'{phone_book[selected_row - 1]['Отчество']}')
            ent_phonenumber.insert(0, f'{phone_book[selected_row - 1]['Телефон']}')
            ent_description.insert(0, f'{phone_book[selected_row - 1].get('Описание', '')}')
        
        panel_buttons = tk.Frame(master=window)        
        panel_buttons.grid(row=15, column=1, ipadx=5, ipady=5)        
        btn_cancel = tk.Button(master=panel_buttons, text="Отменить", command=lambda: treeview_cardedit_close(window))
        btn_cancel.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_ok = tk.Button(master=panel_buttons, text="Принять", command=lambda: treeview_cardedit_ok(window))
        btn_ok.pack(side=tk.RIGHT, ipadx=10)
                
        window.protocol("WM_DELETE_WINDOW", lambda: treeview_cardedit_close(window))        
        window.grab_set()


    # поиск записи в справочнике
    def search_record(phone_book):
                
        # закрытие карточки ввода маски поиска (Найти)
        def treeview_cardsearch_ok(window_): 
            mask_search_info = ent_mask2search.get()            
            search_result = phone_book_search(phone_book, mask_search_info)                        
            if len(search_result):
                tree.delete(*tree.get_children())
                phone_book_print(search_result, tree)
                main_window.title(f'Телефонный справочник - Результаты поиска')
            else:
                showerror(title="Информация", message=f'Записи не найдены.')            
            treeview_cardsearch_close(window_)

        # закрытие карточки ввода маски поиска (Отменить)
        def treeview_cardsearch_close(window_):
            window_.grab_release() 
            window_.destroy()

        window = Toplevel() 
        window.title("Найти запись")        
        window.geometry(create_geometry_2_center_windows(370, 60))
        window.update_idletasks()        
        
        lbl_mask2search = tk.Label(master=window, text="Маска для поиска:")
        ent_mask2search = tk.Entry(master=window, width=50)        
        lbl_mask2search.grid(row=0, column=0, sticky="e")
        ent_mask2search.grid(row=0, column=1)   
        ent_mask2search.insert(0, '*значение*')     
                        
        panel_buttons = tk.Frame(master=window)        
        panel_buttons.grid(row=15, column=1, ipadx=5, ipady=5)        
        btn_cancel = tk.Button(master=panel_buttons, text="Отменить", command=lambda: treeview_cardsearch_close(window))
        btn_cancel.pack(side=tk.RIGHT, padx=10, ipadx=10)
        btn_ok = tk.Button(master=panel_buttons, text="Найти", command=lambda: treeview_cardsearch_ok(window))
        btn_ok.pack(side=tk.RIGHT, ipadx=10)
                
        window.protocol("WM_DELETE_WINDOW", lambda: treeview_cardsearch_close(window))        
        window.grab_set()

    # --------------------------------------------------------------------------

    # основной список телефонного справочника
    phone_book_main = []

    # создаем главное окно
    main_window = Tk()
    main_window.title("Телефонный справочник")          
    main_window.geometry(create_geometry_2_center_windows(700, 400))     
    main_window.update_idletasks()

    # добавляем главное меню
    main_window.option_add("*tearOff", False)
    main_menu = Menu()
    file_menu = Menu()
    file_menu.add_command(label="Создать", command=lambda: new_file(phone_book_main))
    file_menu.add_command(label="Открыть", command=lambda: open_file(phone_book_main))
    file_menu.add_command(label="Сохранить", command=lambda: save_file(phone_book_main))
    file_menu.add_separator()
    file_menu.add_command(label="Выход", command=quit) 
    main_menu.add_cascade(label="Файл", menu=file_menu) 
    main_window.config(menu=main_menu)

    # создаем панель инструментов    
    toolbar = ttk.Frame(main_window, padding=0)    
    toolbar.pack(fill=X, side=TOP)            
    new_icon =  PhotoImage(file="./seminar08/icons/new_icon.png")
    open_icon = PhotoImage(file="./seminar08/icons/open_icon.png")
    save_icon = PhotoImage(file="./seminar08/icons/save_icon.png")
    add_icon = PhotoImage(file="./seminar08/icons/add_icon.png")
    delete_icon = PhotoImage(file="./seminar08/icons/delete_icon.png")
    search_icon = PhotoImage(file="./seminar08/icons/search_icon.png")
    btn_new = Button(toolbar, image=new_icon, text="Новый", command=lambda: new_file(phone_book_main))
    btn_open = Button(toolbar, image=open_icon, text="Открыть", command=lambda: open_file(phone_book_main))
    btn_save = Button(toolbar, image=save_icon, text="Сохранить", command=lambda: save_file(phone_book_main))
    btn_add = Button(toolbar, image=add_icon, text="Добавить", command=lambda: add_record(phone_book_main))
    btn_delete = Button(toolbar, image=delete_icon, text="Удалить", command=lambda: delete_record(phone_book_main))
    btn_search = Button(toolbar, image=search_icon, text="Найти", command=lambda: search_record(phone_book_main))
    btn_new.pack(side=tk.LEFT, padx=2, pady=2)
    btn_open.pack(side=tk.LEFT, padx=2, pady=2)
    btn_save.pack(side=tk.LEFT, padx=2, pady=2)
    btn_add.pack(side=tk.LEFT, padx=2, pady=2)
    btn_delete.pack(side=tk.LEFT, padx=2, pady=2)
    btn_search.pack(side=tk.LEFT, padx=2, pady=2)

    # добавляем виджет TreeView
    tree = ttk.Treeview(columns=FIELD_CAPTIONS, show="headings")
    tree.pack(expand=True, fill=BOTH)        
    for i, caption in enumerate(FIELD_CAPTIONS, 1):
        tree.heading(f'#{i}', text=caption, anchor=W)
        tree.column(f'#{i}', stretch=NO, width=130)         
    tree.bind("<Double-1>", treeview_OnDoubleClick)   
            
    main_window.mainloop()

# запуск приложения
phone_book_editor_tkinter()
