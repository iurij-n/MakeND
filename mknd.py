import os

from docxtpl import DocxTemplate

SAVE_FOLDER_NAME = 'Готовые наряды на'
ROWS = {
    '1': 'A - D',
    '2': 'D - F',
    '3': 'F - H',
    '4': 'H - K'
}


def get_templates_list() -> list:
    path = os.getcwd()
    try:
        with os.scandir(path+'/templates') as listofentries:
            templates_list = [entry.name for entry in listofentries
                              if os.path.splitext(entry)[1] in
                              ('.doc', '.docx')]
    except FileNotFoundError:
        raise FileNotFoundError
    print(f'Найдено шаболонов - {len(templates_list)}\n')
    return templates_list


def get_context():
    with open("data.txt", encoding="utf-8") as data_file:
        raw_data = data_file.readlines()
    data = [row for row in raw_data if ': ' in row and '#' not in row]
    context = {}
    for row in data:
        key, value = row.split(': ')
        context[key] = value.replace('\n', '')
    context['Ряды'] = ROWS[context['ДСП']]
    dsp_number = int(context['ДСП'])
    context['Конвейеры'] = f'{dsp_number*2-1}, {dsp_number*2}'

    print('Данные для заполнения НД:\n')
    for key, value in context.items():
        print(key, ': ', value)
    return context


def get_save_folder_name(date: str) -> str:
    prefix = ''
    prefix_number = 1
    while 1:
        if not os.path.isdir(f'{SAVE_FOLDER_NAME} {date}{prefix}/'):
            return f'{SAVE_FOLDER_NAME} {date}{prefix}/'
        else:
            prefix = '_' + str(prefix_number)
            prefix_number += 1


def make_documents(templates_list, context):
    save_folder = get_save_folder_name(context['Дата'])
    os.mkdir(save_folder)
    print('\nСоздание НД\n')
    for template in templates_list:
        document = DocxTemplate('templates/'+template)
        document.render(context)
        document.save(save_folder+template)
        print(f'{template} - сохранен')


def main():
    templates_list = get_templates_list()
    context = get_context()
    make_documents(templates_list, context)
    input("\n\nНажмите Enter для выхода...")


if __name__ == '__main__':
    main()
