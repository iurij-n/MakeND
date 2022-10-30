import eel
import os

from docxtpl import DocxTemplate

from create_db import ExcelToDB
from models import Person


SAVE_FOLDER_NAME = 'Готовые НД T1'
ROWS = {
    '1': 'A - D',
    '2': 'D - F',
    '3': 'F - H',
    '4': 'H - K'
}
SKIP = 'Пропустить'
SKIP_ADMITTING_VALUE = ''
SKIP_ISSUING_VALUE = ' ' * 60
SKIP_APPROVING_VALUE = ' ' * 100
APPROVER_POSITION = 'заместитель начальника цеха по выплавке'


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
    if approving != SKIP_APPROVING_VALUE:
        approving = f'{APPROVER_POSITION} {approving}'
    context['Согласующий'] = approving
    context['Ряды'] = ROWS[context['ДСП']]
    dsp_number = int(context['ДСП'])
    context['Конвейеры'] = f'{dsp_number*2-1}, {dsp_number*2}'
    
    return context


def get_save_folder_name(date: str, dsp: int) -> str:
    prefix = ''
    prefix_number = 1
    while 1:
        if not os.path.isdir(f'{SAVE_FOLDER_NAME} ДСП-{dsp} {date}{prefix}/'):
            print(f'explorer.exe {os.getcwd()}\\{SAVE_FOLDER_NAME} ДСП-{dsp} {date}{prefix}\\')

            return f'{SAVE_FOLDER_NAME} ДСП-{dsp} {date}{prefix}/'
        else:
            prefix = '_' + str(prefix_number)
            prefix_number += 1


def make_documents(templates_list, context):
    save_folder = get_save_folder_name(context['Дата'], context['ДСП'])
    os.mkdir(save_folder)
    os.startfile(f'{os.getcwd()}\\{save_folder}')
    print('\nСоздание НД\n')
    templates_count = len(templates_list)
    for number, template in enumerate(templates_list):
        document = DocxTemplate('templates/'+template)
        document.render(context)
        document.save(save_folder+template)
        print(f'{number+1}/{templates_count} {template} - сохранен')
        eel.progress_bar(f'{number+1}/{templates_count}')
    print('Все файлы успешно сохранены!')
    eel.progress_bar('Все файлы успешно сохранены!')


def main():
    eel.init('wui')

    db_inst = ExcelToDB('itr_list.xlsx', 'itr.sqlite', Person)
    admitting_list = db_inst.get_name_list('is_admitting', False)
    admitting_value_list = db_inst.get_name_list('is_admitting')
    issuing_list = db_inst.get_name_list('is_issuing', False)
    issuing_value_list = db_inst.get_name_list('is_issuing', False)
    approving_list = db_inst.get_name_list('is_approving', False)
    approving_value_list = db_inst.get_name_list('is_approving')
    admitting_list.append(SKIP)
    admitting_value_list.append(SKIP_ADMITTING_VALUE)
    issuing_list.append(SKIP)
    issuing_value_list.append(SKIP_ISSUING_VALUE)
    approving_list.append(SKIP)
    approving_value_list.append(SKIP_APPROVING_VALUE)

    eel.generate_forms(admitting_list,
                       admitting_value_list,
                       issuing_list,
                       issuing_value_list,
                       approving_list,
                       approving_value_list)
    try:
        eel.start('ui.html',
                  mode='chrome',
                  size=(500, 850),
                  position=(100, 200))
    except:
        return


@eel.expose
def make_nd(dsp, date, admitting, issuing, approving):

    db_inst = ExcelToDB('itr_list.xlsx', 'itr.sqlite', Person)
    admitting_list = db_inst.get_name_list('is_admitting', False)
    print(admitting, admitting_list)
    
    templates_list = get_templates_list()
    context = get_context(dsp, date, admitting, issuing, approving)

    make_documents(templates_list, context)


if __name__ == '__main__':
    main()
