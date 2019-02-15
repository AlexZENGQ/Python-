#查找模糊文件

import os


#文件夹路径
root = 'F:\\ere\\PythonScript\\File'

def target(path):
	files = os.listdir(path)
	for file in files:
		#找到文件名中包含text,而且文件类型为.py的文件
		if 'text' in file and file.endswith('.py'):
			print('找到文件名:', file)
target(root)

