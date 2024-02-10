peoples = [
    {"Name": "Иван", "Age": 25, "Surname": "Иванов"},
    {"Name": "Алексей", "Age": 22, "Surname": "Петров"},
    {"Name": "Екатерина", "Age": 28, "Surname": "Сидорова"},
    {"Name": "Андрей", "Age": 35, "Surname": "Козлов"},
    {"Name": "Ольга", "Age": 29, "Surname": "Новикова"},
    {"Name": "Алексей", "Age": 22, "Surname": "Петров"},
    {"Name": "Иван", "Age": 25, "Surname": "Козлов"}
]

keys = ["Name", "Surname"]

def sort_peoples(peoples: list, keys: list)-> list:
    unique_people = set()
    unique_list = []
    for people in peoples:
        people_sort_by_keys = tuple([people[key] for key in keys])
        if people_sort_by_keys not in unique_people:
            unique_list.append(people)
            unique_people.add(people_sort_by_keys)
    return unique_list

print(sort_peoples(peoples,keys))

dictionary = {1:2, 3:4}

def swap_key_on_value(dictionary: dict) -> dict:
   return {value: key for key,value in dictionary.items()}

print(swap_key_on_value(dictionary))

students = {'Vlad': [5,7,3,8,2],'Serg': [1,4,5,6,2],'Vital': [6,4,9,1,3]}

def best_student(students: dict)->tuple:
    max_average_mark = 0
    min_average_mark = float('inf')
    for name, marks in students.items():
        average_mark = sum(marks) / len(marks)
        if average_mark > max_average_mark:
            max_average_mark = average_mark
            best_student = {name: average_mark}
        if average_mark < min_average_mark:
            min_average_mark = average_mark
            lagging_student = {name: average_mark}
    return best_student, lagging_student

print(best_student(students))