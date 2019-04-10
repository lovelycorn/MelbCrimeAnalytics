import pandas as pd
import xlrd
import numpy as np
import pandas

def get_data(filename,sheetnum):
	dir_case = 'test.xlsx'
	data = xlrd.open_workbook(dir_case)
	table = data.sheets()[sheetnum]
	nor = table.nrows
	nol = table.ncols

	dict = {}
	'''
	for i in range(1,nor):
		for j in range(nol):
			title = table.cell_value(0,j)
			value = table.cell_value(i,j)
			dict[title] = value
		#yield dict
	'''
	data = [{'year': 2010.0, 'type': 'b01', 'num': 3.0},
	{'year': 2010.0, 'type': 'a01', 'num': 2.0},
	{'year': 2012.0, 'type': 'a01', 'num': 4.0}]

	dictToList = []
	for i in range(len(data)):
		dictToList.append(list(data[i].values()))
	print(dictToList)
	#data2 = {value: key for key, value in data[1].items()}
	df1 = pd.DataFrame(dictToList,index=[0,1,2],columns=['year','a01','b01'])
	#for i in dict.items:




	yield df1
'''
	np.array([[dict[LGA][TYPE] for TYPE in dict[LGA]] for LGA in dict])

	TYPE = ['a01','b01']
	list_of_lists = []
	for name, LGA in sorted(dict.items()):
		titles = []
		for types in TYPE:
			try:
				titles.append(LGA[types])
			except KeyError:
				titles.append(0)
		list_of_lists.append(titles)

	books_array = numpy.array(list_of_lists)
'''
if __name__ == '__main__':
	for i in get_data('add_user',0):
		print(i)


#def xlsx_to_csv_pd():
    #data_xls = pd.read_excel('test.xlsx', index_col=0)

    #data_xls.to_csv('1.csv', encoding='utf-8')


#if __name__ == '__main__':
    #xlsx_to_csv_pd()
