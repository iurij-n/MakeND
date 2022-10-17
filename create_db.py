import pandas

excel_data_df = pandas.read_excel('itr_list.xlsx', sheet_name=0).fillna(False)

# print whole sheet data

print(excel_data_df)

print(list(excel_data_df.values))

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