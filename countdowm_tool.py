#倒计时工具

from tkinter import  *
import threading
import time


info = {
	'total_time' : 60
}

#定义界面
def counter_app():
	window = Tk()
	Label(name='lb', text=0, font=["times",30,"bold"]).pack()
	Entry(name='ipt').pack()
	Button(name='btn', text='开始', command=time_counts).pack()
	window.geometry('200x200')
	return window

#定义倒计时数字
def time_counts():
	def timedowm():
		while info['total_time']:
			info['total_time'] -= 1
			print(info['total_time'])
			time.sleep(1)

	t = threading.Thread(target=timedowm, name='timer')
	t.start()

#定义停止状态
def time_stop():
	info['total_time'] = 0

#界面功能集合
def interface():

	#定义输入框状态
	def update_input():
		ipt = window.children['ipt']
		timer = [t for t in threading.enumerate() if t.name == 'timer']
		ipt['state'] = 'disabled' if timer else 'normal'

	#定义按钮状态
	def update_button():
		btn = window.children['btn']
		timer = [t for t in threading.enumerate() if t.name == 'timer']
		btn['text'] = '停止' if timer else '开始'
		btn['command'] = time_stop if timer else time_counts

	#获得输入框中填入的数字
	def get_time():
		ipt = window.children['ipt']
		timer = [t for t in threading.enumerate() if t.name == 'timer']
		if not timer and ipt.get():	
			info['total_time'] = int(ipt.get())

	#时刻刷新时间
	def update_time():
			window.children['lb']['text'] = info['total_time']

	#主函数
	def _main():
		while True:
			print('show you')
			print(threading.enumerate())
			get_time()
			update_time()
			update_button()
			update_input()
			time.sleep(0.5)
		
	t = threading.Thread(target=_main, name='watcher')
	t.start()

if __name__ == '__main__':
	window = counter_app()
	window.after(0, interface)
	window.mainloop()











