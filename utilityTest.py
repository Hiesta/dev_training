import json

programType = input('A - Add new surname or name\nG - Get information\n')


if programType.lower() == 'a':
    with open('surnames.json', 'r') as file:
        curr_surnames = json.load(file)

        surname = input('Surname = ')
        names = input('Enter names, separated by ", "\n').split(', ')

        if surname in curr_surnames.keys():
            curr_surnames[surname] = list(set(curr_surnames[surname] + names))
        else:
            curr_surnames[surname] = names

    with open('surnames.json', 'w') as file:
        json.dump(curr_surnames, file, indent=4)
if programType.lower() == 'g':
    with open('surnames.json', 'r') as file:
        current_file = json.load(file)
        for surname, names in current_file.items():
            print(surname, ':', end=' ')
            for name in names:
                print(name, end=' ')
            print('')