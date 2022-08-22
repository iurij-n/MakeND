import eel


@eel.expose
def foo(dsp, date, admitting, issuing, approving):
    print('Переданые данные:')
    print('Номер ДСП: ', dsp, '       ', 'Тип переменной - ', type(dsp))
    print('Дата ремонта: ', date, '       ', 'Тип переменной - ', type(date))
    print('Допускающий НД: ', admitting, '       ', 'Тип переменной - ', type(admitting))
    print('Выдающий НД: ', issuing, '       ', 'Тип переменной - ', type(issuing))
    print('Согласующий НД: ', approving, '       ', 'Тип переменной - ', type(approving))
    ## return select_list


if __name__=='__main__':
    eel.init('wui')
    eel.start('ui.html', mode='edge', size=(500, 800), position=(100, 200))
