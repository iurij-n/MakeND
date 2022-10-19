import os
import pandas
import peewee

from models import *

if os.path.isfile('itr_list.xlsx'): 
  excel_data_df = pandas.read_excel(
    'itr_list.xlsx', sheet_name=0).fillna(False)
else:
  raise FileNotFoundError("The file itr_list.xlsx does not exist!!!")

# print whole sheet data

# print(excel_data_df)

# print(list(excel_data_df.values))

for index, value in enumerate(excel_data_df.values):
    print(index, '-----', tuple(excel_data_df.values[index]))
# a = list(excel_data_df.values)

# for index, value in enumerate(a):
#     print(f'Элемнт с индексом {index} - {value}, его тип - {type(value)}')
#     if value == False:
#         print('1111111111111')
# # print(excel_data_df.columns.ravel())

# # for row in excel_data_df:
# #     print(row)

connect = SqliteDatabase('itr.db')

try:
    connect.connect()
    Person.create_table(safe=True)
except peewee.InternalError as px:
    print(str(px))
    
query = Person.delete()
query.execute()

for index, value in enumerate(excel_data_df.values):
    data = tuple(excel_data_df.values[index])
    row = Person(
        last_name = data[0],
        name = data[1],
        patronymic = data[2],
        is_admitting = data[3],
        is_issuing = data[4],
        is_approving = data[5],
    )
    row.save()