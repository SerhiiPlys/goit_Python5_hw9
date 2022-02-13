""" ДЗ8
    можно сохранить словарь в файл рядом со скриптом, открывать его на чтение при зауске программы
    и считывать в ОЗУ а перед акрытием - открывать на запись и сохранять  - это элементарно
    но пока сделаем словарь с контаками в ОЗУ
    точно также логику проверки на ошибки можно коректировать по ходу бета тестов
    . - заканчиваем работу если встречаем в вводе
    hello - ответ Can I help you
    add ффф ввв - сохраняем контакт ффф с телефоном ввв
    change  ффф ввв - если существует ффф поменять номер на ввв, если не существует
                      выдать предупреждение
    phone ффф - показать номер для контакта ффф, в случае ошибки сообщение
    show_all - показать все контакты
    good bye, close, get out, exit, end - команды выхода
"""
import os

dict_numbers  = {"John Dou":"111111111111"} # тестовый словарь - тел книга

def dec_pars(func):
    def inner(a):
        result = func(a)  # результат это лист, но непроверенный, далее в декораторе проверим его на безошибочность
        if len(result) > 3:
            print("Используйте формат команды определнный выше")
            result = ["error"] # модифицируем результат чтобы сработала команда ееррор
        elif result[0] not in (".", "add", "hello", "change", "phone", "show_all"):
            print("Неизвестная команда")
            result = ["error"] # модифицируем результат чтобы сработала команда ееррор
        try:
            if result[0] == "add":
                a = result[1]
                b = result[2]                # пробуем на исключение IndexError
            if result[0] == "phone":
                a = result[1]
            if result[0] == "change":
                a = dict_numbers[result[1]]  # пробуем на исключение KeyError
        except KeyError:
                print("Неизвестный контакт для замены номера")
                result = ["error"] # модифицируем результат чтобы сработала команда ееррорhello
        except IndexError:
                print("Неверный формат для добавления или показа номера")
                result = ["error"] # модифицируем результат чтобы сработала команда ееррорhello
        return result
    return inner

@dec_pars
def parsing_in(a):   # нормализуем строку ввода, ошибки команд будут ловится в декораторе
    l1 = a.split(' ')
    l2 = []
    for i in l1:
        if i != '':   # убираем лишние элементы в списке получившемся
            l2.append(i)
    l3 = []
    for i in l2:
        j = i.strip()    #  триммируем каждый элемент списка
        z = j.casefold() #  и приводим его к нижнему регистру
        l3.append(z)     # получаем готовый нормализованый список
    return l3  # столько возни и новых переменных потому
               #  что строки неизменяемы и конструкция a = а.strip() невозможна 

def error_input(a):
    return "Ошибочный ввод, причина в строке выше, попробуйте снова"

def greating(a):
    return "Can I help you"

def exit_bot(a):
    os._exit(1)    # выход из бота с кодом ошибки 1

def add_numb(a):
    a.update({l_in[1]:l_in[2]})
    return "Контакт добавлен"

def change_numb(a):
    a[l_in[1]] = l_in[2]
    return "Контакт изменен"

def show_phone(a):
    s1 = a[l_in[1]]
    return s1
        
def show_all_phone(a):
    s1 = ''
    for k,v in a.items():
        s1 += k+ ' '+ v + '\n'
    return s1
        
dict_commands = ({"error":error_input,
                  "hello":greating,
                  '.':exit_bot,
                  "add":add_numb,
                  "change":change_numb,
                  "phone":show_phone,
                  "show_all":show_all_phone})
def get_handler(a):
    
    command = a[0]  # первый элемент в списке - команда
    return dict_commands[command] # возврат сигнатуры нужной функции



l_in  = []
s_out = ''  # строка вывод ответа на любую введенную команду - глобальная переменная
def main():
    global l_in
    print("""
          Допустимые команды
          . - для выхода
          hello - для приветсвия
          add ... 111 - для добавления контакта
          change ... 111 - для изменения контакта
          phone ... - для просмотра номера
          show_all - для просмотра всей телефонной книги
          """)
    while True:
        s_in = input("$ - ")
        if s_in in ("good_bye", "close", "exit", "end"):
            print("Good Bye")
            os._exit(0)  # нормальное завершение программы - код 0
        else:
            l_in = parsing_in(s_in)  # парсим строку ввода
#            print(l_in)
            s_out = get_handler(l_in)(dict_numbers)
            print(s_out)



if __name__ == "__main__":
    main()
