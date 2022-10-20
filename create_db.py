import os

import pandas
import peewee

from models import *


class MakeBD():
    """Класс создает базу данных db_name на основе данных прочитанных
    из таблицы MS Excel excel_file_name.
    """
    def __init__(self, excel_file_name, db_name):
        if os.path.isfile(excel_file_name): 
            self.excel_data_df = pandas.read_excel(
                excel_file_name, sheet_name=0).fillna(False)
        else:
            raise FileNotFoundError(
                "The file itr_list.xlsx does not exist!!!")

        self.connect = SqliteDatabase(db_name)

        try:
            self.connect.connect()
            Person.create_table(safe=True)
        except peewee.InternalError as px:
            print(str(px))

        Person.delete().execute()

        self.fields = list(Person._meta.fields.keys())[1:]
        self.data = [tuple(self.excel_data_df.values[index])
                     for index in
                     range(self.excel_data_df.shape[0])]
        Person.insert_many(
            self.data,
            fields=self.fields).execute()


def main() -> None:
    db_inst = MakeBD('itr_list.xlsx', 'itr.sqlite')

if __name__=='__main__':
    main()
