import eel
import os

from docxtpl import DocxTemplate


SAVE_FOLDER_NAME = 'Готовые наряды на'
ROWS = {
    '1': 'A - D',
    '2': 'D - F',
    '3': 'F - H',
    '4': 'H - K'
}



@eel.expose
def foo(dsp, date, admitting, issuing, approving):
    print('Переданые данные:')
    print('Номер ДСП: ', dsp, '       ', 'Тип переменной - ', type(dsp))
    print('Дата ремонта: ', date, '       ', 'Тип переменной - ', type(date))
    print('Допускающий НД: ', admitting, '       ', 'Тип переменной - ', type(admitting))
    print('Выдающий НД: ', issuing, '       ', 'Тип переменной - ', type(issuing))
    print('Согласующий НД: ', approving, '       ', 'Тип переменной - ', type(approving))
    ## return select_list


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


def format_date(date):
    date = [symbol for symbol in date]
    return f'{"".join(date[8:])}.{"".join(date[5:7])}.{"".join(date[:4])}'


def get_context(dsp, date, admitting, issuing, approving):
    context = {}
    context['ДСП'] = dsp
    
    if date == '':
        context['Дата'] = '01.01.1990'
    else:
        context['Дата'] = format_date(date)
    
    context['Допускающий'] = admitting
    context['Выдающий'] = issuing
    context['Согласующий'] = approving
    
    return context


def get_save_folder_name(date: str) -> str:
    prefix = ''
    prefix_number = 1
    while 1:
        if not os.path.isdir(f'{SAVE_FOLDER_NAME} {date}{prefix}/'):
            print(f'explorer.exe {os.getcwd()}\\{SAVE_FOLDER_NAME} {date}{prefix}\\')
            
            return f'{SAVE_FOLDER_NAME} {date}{prefix}/'
        else:
            prefix = '_' + str(prefix_number)
            prefix_number += 1


def make_documents(templates_list, context):
    save_folder = get_save_folder_name(context['Дата'])
    os.mkdir(save_folder)
    os.startfile(f'{os.getcwd()}\\{save_folder}')
    print('\nСоздание НД\n')
    for template in templates_list:
        document = DocxTemplate('templates/'+template)
        document.render(context)
        document.save(save_folder+template)
        print(f'{template} - сохранен')


def main():
    eel.init('wui')
    eel.start('ui.html', mode='edge', size=(500, 800), position=(100, 200))


@eel.expose
def make_nd(dsp, date, admitting, issuing, approving):
    
    templates_list = get_templates_list()
    context = get_context(dsp, date, admitting, issuing, approving)
    
    make_documents(templates_list, context)


if __name__ == '__main__':
    main()
