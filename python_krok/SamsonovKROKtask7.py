from collections import Counter
import re
import datetime

# Функция для проверки на формат времени, построена с помощью модуля datetime
def date_time_is_valid(date_time_str : str, date_time_format : str = '%Y-%m-%dT%H:%M:%S') -> bool :
    try:
        datetime.datetime.strptime(date_time_str, date_time_format)
        return True
    except ValueError:
        return False

#Добавим паттерны для проверки на соответсвие требованиям указанным в условии
pattern_for_employee = re.compile(r'^[a-zA-Z0-9_]+$')
pattern_for_hach = re.compile(r'^[a-z0-9]{7}$')
pattern_for_date_time = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$')

#Подсчет самых активных сотрудников, путем открытия файла, генератора списков и использования метода collections -> Counter().most_common()
with open('commits.txt','r', encoding = 'utf-8') as commits_file:
    cnt_for_employees = Counter(
        [employee for line in commits_file 
         for employee,hach,date_time in [line.split()] 
         if not employee[0].isdigit() 
         and pattern_for_employee.match(employee) 
         and len(hach) == 7 
         and pattern_for_hach.match(hach) 
         and pattern_for_date_time.match(date_time) 
         and date_time_is_valid(date_time)]
         ).most_common(3)

#Создание результирующего файла и последующая построчная запись только сотрудников
with open('result.txt','w', encoding = 'utf-8') as results_file:
    for couple in cnt_for_employees:
        results_file.write(f"{couple[0]}\n")