from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for data in contacts_list[1:]:
    name = data[0]
    if name != '':
        name_list = name.split()
        if len(name_list) == 3:
            data[0] = name_list[0]
            data[1] = name_list[1]
            data[2] = name_list[2]
        elif len(name_list) == 2:
            data[0] = name_list[0]
            data[1] = name_list[1]
        elif len(name_list) == 1:
            data[0] = name_list[0]

    name1 = data[1]
    if name1 != '':
        name_list1 = name1.split()
        if len(name_list1) == 3:
            data[0] = name_list1[0]
            data[1] = name_list1[1]
            data[2] = name_list1[2]
        elif len(name_list1) == 2:
            data[1] = name_list1[0]
            data[2] = name_list1[1]
        elif len(name_list1) == 1:
            data[1] = name_list1[0]

    name2 = data[2]
    if name2 != '':
        name_list2 = name2.split()
        if len(name_list2) == 3:
            data[0] = name_list2[0]
            data[1] = name_list2[1]
            data[2] = name_list2[2]
        elif len(name_list2) == 2:
            data[1] = name_list2[0]
            data[2] = name_list2[1]
        elif len(name_list2) == 1:
            data[2] = name_list2[0]

    del data[7:]

pattern = re.compile(r'(\+7|8)*\s*\(?(\d{3})\)?\s*\D*(\d{3})[-\s+]*(\d{2})-?(\d{2})((\s)*\(?(доб\.)?\s*(\d+)\)?)?')
number_sub = r'+7(\2)\3-\4-\5\7\8\9'
for phone in contacts_list[1:]:
    phone[5] = pattern.sub(number_sub, phone[5])

new_contact_list = []
for info in contacts_list[1:]:
    name1 = info[0]
    name2 = info[1]
    for employee in contacts_list:
        new_name1 = employee[0]
        new_name2 = employee[1]
        if name1 == new_name1 and name2 == new_name2:
            if info[2] == '':
                info[2] = employee[2]
            if info[3] == '':
                info[3] = employee[3]
            if info[4] == '':
                info[4] = employee[4]
            if info[5] == '':
                info[5] = employee[5]
            if info[6] == '':
                info[6] = employee[6]

for employee in contacts_list:
    if employee not in new_contact_list:
        new_contact_list.append(employee)

pprint(contacts_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contact_list)