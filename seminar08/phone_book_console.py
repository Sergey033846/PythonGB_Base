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


PHONE_BOOK_FILENAME = 'seminar08/phone_book.txt'
PHONE_BOOK_FILENAME_DEST = 'seminar08/phone_book_copy.txt'
CELL_DATA_MAX_LENGTH = 15
CELL_IDSTR_MAX_LENGTH = 3
COLOR_TAGS_LENGTH = len('\033[33m' * 2)
FIELD_CAPTIONS = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']


# вывод телефонной книги (список) или результатов поиска (словарь) на экран
def phone_book_print(phone_book):

    def phone_book_record_print(numstr_: int, phone_book_record_):
        print(f'{numstr_:>{CELL_IDSTR_MAX_LENGTH}}  ', end='')
        for data in phone_book_record_.values():
            cell_length = CELL_DATA_MAX_LENGTH + COLOR_TAGS_LENGTH if '[' in data else CELL_DATA_MAX_LENGTH            
            print(f'{data:<{cell_length}}', end='')
        print()
       
    print(f'\033[34m{'№':>{CELL_IDSTR_MAX_LENGTH}}  {''.join(map(lambda x: x.ljust(15), FIELD_CAPTIONS))}\033[00m')        
    if isinstance(phone_book, list):
        for i, phone_book_record in enumerate(phone_book, 1):                    
            phone_book_record_print(i, phone_book_record)                
    elif isinstance(phone_book, dict):
        for numstr, phone_book_record in phone_book.items():
            phone_book_record_print(numstr + 1, phone_book_record)                
    

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
    

# удаление всех записей в файле справочника (убрал команду)
# def phone_book_clear(filename):
#     if input('Подтвердите удаление данных (+/-): ') == '+':
#         open(filename, 'w').close()
#         print('Все записи в справочнике удалены.')
        

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
# с расчетом индексов для "подсветки" искомого значения
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
                    phone_book_record_with_mask[field_caption] = f'{data[:index_start]}\033[47m{data[index_start: index_end]}\033[00m{data[index_end:]}'                    
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
                

# вывод на экран главного меню
def ui_print_main_menu_and_status_bar(command_list_, is_data_changed_):
    if is_data_changed_:
        print(f'\033[35m{'ВНИМАНИЕ! Данные изменены.'}\033[00m')        
    print(f'\033[32m{'Доступные команды:'}\033[00m')
    columns_count = 5
    rows_count = len(command_list_) // columns_count + (len(command_list_) % columns_count != 0)
    max_command_name_len = len(max(command_list_, key=len))
    for row in range(rows_count):     
        print(f'{' ' * 3}'.join(map(lambda x: x.ljust(max_command_name_len), command_list_[row * columns_count: (row + 1) * columns_count])))
    print()


def phone_book_editor():
    print(f'\033[32m{'Программа "Телефонный справочник"'}\033[00m')
    command_list = ['1. Печать данных', '2. Добавить запись', '3. Поиск записи', '4. Изменить запись', '5. Удалить запись', 
                    '6. Открыть корзину', '7. Копировать в файл', '8. Сохранить справочник', '9. Завершение работы']

    phone_book_main = phone_book_read_txt(PHONE_BOOK_FILENAME, FIELD_CAPTIONS)
    recycle_bin = []
    is_data_changed = False
    
    while(True):
        ui_print_main_menu_and_status_bar(command_list, is_data_changed)            

        command = int(input(f'\033[32m{'Введите команду: '}\033[00m'))
        print(f'Выбрана команда "{command_list[command - 1]}"')

        match command:        
            # 1. Печать данных
            case 1:                 
                phone_book_print(phone_book_main)
            
            # 2. Добавить запись
            case 2: 
                new_record_data = input('Введите через пробел фамилию, имя, отчество, номер телефона, описание:\n')
                if phone_book_add_record(phone_book_main, new_record_data, FIELD_CAPTIONS, 'Телефон') != -1:
                    print('Запись успешно добавлена.')
                    is_data_changed = True
                else:
                    print('Ошибка добавления. Такая запись уже существует.')
            
            # 3. Поиск записи
            case 3:                 
                mask_search_info = input('Введите данные для поиска по маске вида *значение*: ').lower()
                search_result = phone_book_search(phone_book_main, mask_search_info)
                print(f'\033[32m{'Результаты поиска:'}\033[00m')
                phone_book_print(search_result) if len(search_result) else print('Записи не найдены.') 
            
            # 4. Изменить запись
            case 4:
                numrec2edit = int(input('Введите номер записи для редактирования: '))
                if phone_book_record_exists(phone_book_main, numrec2edit): 
                    old_record_data = dict(phone_book_main[numrec2edit - 1]).values()                                        
                    print(f'Текущие значения записи: \n{' '.join(old_record_data)}')
                    new_record_data = input('Введите через пробел новые фамилию, имя, отчество, номер телефона, описание:\n')                    
                    phone_book_change_record(phone_book_main, numrec2edit, new_record_data, FIELD_CAPTIONS)
                    print('Запись изменена.')
                    is_data_changed = True
                else:
                    print('Такая запись не существует!')

            # 5. Удалить запись
            case 5:
                numrec2del = int(input('Введите номер записи для удаления: '))
                if phone_book_record_exists(phone_book_main, numrec2del):
                    if input('Подтвердите удаление данных (+/-): ') == '+':
                        deleted_record = phone_book_delete_record(phone_book_main, numrec2del)
                        if deleted_record:
                            recycle_bin.append(deleted_record)
                            print(f'Запись {deleted_record} перемещена в корзину.')
                            is_data_changed = True                  
                    else:
                        print('Удаление записи отменено.')
                else:
                    print('Такая запись не существует!')
            
            # 6. Открыть корзину
            case 6:
                phone_book_print(recycle_bin)
                if len(recycle_bin) and input('Восстановить записи из корзины? (+/-): ') == '+':
                    phone_book_main += recycle_bin
                    phone_book_sort(phone_book_main)
                    recycle_bin.clear()
                    print('Записи восстановлены.')
                    is_data_changed = True
            
            # 7. Копировать в файл
            case 7: 
                numrec2copy = int(input('Введите номер записи для копирования в другой файл: '))
                if phone_book_record_exists(phone_book_main, numrec2copy): 
                    phone_book_record_copy2file(phone_book_main, numrec2copy, PHONE_BOOK_FILENAME_DEST)
                    print('Копирование записи произведено.')
                else:
                    print('Такая запись не существует!')
            
            # 8. Сохранить справочник
            case 8: 
                phone_book_save_txt(phone_book_main, PHONE_BOOK_FILENAME)
                print('Телефонный справочник успешно сохранен.')
                is_data_changed = False
            
            # 9. Завершение работы
            case 9:
                if not is_data_changed or is_data_changed and input('Данные не сохранены, выйти без сохранения? (+/-): ') == '+':                    
                    break        
            
            case _: 
                print('Неизвестная команда, повторите ввод.')

        print()        
    print('Сеанс завершен.')


phone_book_editor()
