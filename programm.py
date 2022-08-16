import eel


@eel.expose
def foo(chat_id, message, select_list):
    print(type(select_list), len(select_list), '\n', select_list)
    return select_list


if __name__=='__main__':
    eel.init('wui')
    eel.start('ui.html', mode='chrome', size=(400, 600), position=(100, 200))
