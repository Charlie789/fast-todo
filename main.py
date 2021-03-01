from task import Task


task_list = []


def main_menu():
    print()
    print("** MENU **")
    print("1. Lista zadań nieukończonych")
    print("2. Lista zadań ukończonych")
    print("3. Nowe zadanie")
    print("0. Koniec")

    choice = input("Wybierz: ")
    if choice == "1":
        incomplete_list()
    elif choice == "2":
        complete_list()
    elif choice == "3":
        add_task()
    elif choice == "0":
        exit(0)
    else:
        print("Błędny wybór")


def incomplete_list():
    print()
    print("** LISTA ZADAŃ UKOŃCZONYCH **")
    print("Wybierz nr zadania, aby oznaczyć jako ukończone")

    print("0. powrót")

    for index, incomplete_task in enumerate(task_list):
        if not incomplete_task.isComplited:
            print(f"{index + 1}. {incomplete_task.title}")

    choice = input("Wybierz: ")
    try:
        int(choice)
    except ValueError:
        print("Wybrana wartość nie jest liczbą całkowitą")
        incomplete_list()
        return

    if choice == "0":
        return
    elif int(choice) <= len(task_list):
        task_list[int(choice) - 1].complete_task()
    else:
        print("Błędny wybór")
        incomplete_list()


def complete_list():
    print()
    print("** LISTA ZADAŃ NIEUKOŃCZONYCH **")
    print("Wybierz nr zadania, aby oznaczyć jako nieukończone")

    print("0. powrót")

    for index, incomplete_task in enumerate(task_list):
        if incomplete_task.isComplited:
            print(f"{index + 1}. {incomplete_task.title}")

    choice = input("Wybierz: ")
    try:
        int(choice)
    except ValueError:
        print("Wybrana wartość nie jest liczbą całkowitą")
        complete_list()
        return

    if choice == "0":
        return
    elif int(choice) <= len(task_list):
        task_list[int(choice) - 1].incomplete_task()
    else:
        print("Błędny wybór")
        complete_list()


def add_task():
    print()
    print("** NOWE ZADANIE **")
    print("Podaj nazwe zadania:")

    new_task = Task(input())
    task_list.append(new_task)


if __name__ == "__main__":
    while True:
        main_menu()
