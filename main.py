from datetime import datetime

'''
Додаток, який буде зберігати додатки

This is my note, that I am taking on my laptop
- Created on 19.12.2024 20:15 ❤️

[("This is my note, that I am taking on my laptop", "19.12.2024 20:15")]
[("19.12.2024 20:15", "This is my note, that I am taking on my laptop", )]

{"text": "This is my note, that I am taking on my laptop", "creation_date": "19.12.2024 20:15"}
{"creation_date": "19.12.2024 20:15", "text": "This is my note, that I am taking on my laptop"}

if note_data_one["creation_date"] > note_data_two["creation_date"]:

1) Створити словник нотаток та записати в нього інформацію
2) Написати функцію яка буде виводити нотатку
3) Написати функцію яка буде виводити всі нотатки
4) Написати цикл який буде отримувати інформацію від користувача та реагувати на неї

'''


note_list = [] # {"creation_date": "19.12.2024 20:15", "text": "This is my note, that I am taking on my laptop"}
note_files = "notes.txt"
welcome_banner = '''
 █████   █████          ████                                  ███████████            █████   
░░███   ░░███          ░░███                                 ░░███░░░░░███          ░░███    
 ░███    ░███   ██████  ░███  ████████   ██████  ████████     ░███    ░███  ██████  ███████  
 ░███████████  ███░░███ ░███ ░░███░░███ ███░░███░░███░░███    ░██████████  ███░░███░░░███░   
 ░███░░░░░███ ░███████  ░███  ░███ ░███░███████  ░███ ░░░     ░███░░░░░███░███ ░███  ░███    
 ░███    ░███ ░███░░░   ░███  ░███ ░███░███░░░   ░███         ░███    ░███░███ ░███  ░███ ███
 █████   █████░░██████  █████ ░███████ ░░██████  █████        ███████████ ░░██████   ░░█████ 
░░░░░   ░░░░░  ░░░░░░  ░░░░░  ░███░░░   ░░░░░░  ░░░░░        ░░░░░░░░░░░   ░░░░░░     ░░░░░  
                              ░███                                                           
                              █████                                                          
                             ░░░░░                                                                                                                  
'''

goodbye_banner = '''
   █████████                        █████ █████                        
  ███░░░░░███                      ░░███ ░░███                         
 ███     ░░░   ██████   ██████   ███████  ░███████  █████ ████  ██████ 
░███          ███░░███ ███░░███ ███░░███  ░███░░███░░███ ░███  ███░░███
░███    █████░███ ░███░███ ░███░███ ░███  ░███ ░███ ░███ ░███ ░███████ 
░░███  ░░███ ░███ ░███░███ ░███░███ ░███  ░███ ░███ ░███ ░███ ░███░░░  
 ░░█████████ ░░██████ ░░██████ ░░████████ ████████  ░░███████ ░░██████ 
  ░░░░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░░░░    ░░░░░███  ░░░░░░  
                                                     ███ ░███          
                                                    ░░██████           
                                                     ░░░░░░            
'''
comands = '''
1) exit - exit the app
2) add_note - add new note
3) print_note [index] - print note by index
4) print_all_notes - print all notes
5) help - print this help message
'''


def add_new_note(note_text) ->bool:
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True
    
def print_note(index: int):
    note = note_list[index]
    # 19.12.2024 20:15 dd.mm.yyyy hh:mm
    formated_creaation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f"{note["text"]}\n- Created on {formated_creaation_date}\n")
    
def print_all_notes():
    for note_index in range(len(note_list)):
        print_note(note_index)
        
def save_notes():
    with open(note_files, "w") as file:
        for note in note_list:
            formated_creaation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
            file.write(f"{note['text']}|{formated_creaation_date}\n")
            
def read_notes() -> list[dict ]:
    note_list = [] 
    try:
        with open(note_files, "r") as file:
            for line in file:
                note_text, note_creation_date = line.strip().split("|")
                note_creation_date = datetime.strptime(note_creation_date, "%d.%m.%Y %H:%M")
                note_list.append({"text": note_text, "creation_date": note_creation_date})
        return note_list 
    except FileNotFoundError:
        pass 

note_list = read_notes()  

print(welcome_banner)
print(comands)
print("\nHello and welcome to our app!\n") # Ctrl + C to exit
text = input("Please enter note text: ")
#add_new_note(text)
#add_new_note(text)
#add_new_note(text)
#add_new_note(text)

while True:
    command, *args = input("Please enter command (exit to stop): ").strip().split(' ') # ["print_note", "1"] or ["add_note"]
    if command == "exit":
        print(goodbye_banner)
        save_notes() 
        break
    elif command == "add_note":
        text = input("Please enter note text: ")
        if add_new_note(text):
            print("\nNote added successfully!\n")
        else:
            print("\nError adding note!\n")
    elif command == "help":
        print(comands)
    elif command == "print_note":
        index = int(args[0])
        if index < 0 or index >= len(note_list):
            print("\nError: Note index out of range!\n") 
        print_note(index)
    
    
    # " add_note 1  ".strip()
    # "add_note 1".split(' ')
    # command, *args = ["add_note", "1"]
    # command = "add_note"
    # args = ["1"]