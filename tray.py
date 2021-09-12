from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import os
  
app = QApplication([])
app.setQuitOnLastWindowClosed(False)
  
# Adding an icon
icon = QIcon("icon.png")
  
# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

def f_s1():
  os.system('sudo battmngr -s 1')
  os.system('notify-send -a 性能管理 智能冷却')
def f_s2():
  os.system('sudo battmngr -s 2')
  os.system('notify-send -a 性能管理 极致性能')
def f_s3():
  os.system('sudo battmngr -s 3')
  os.system('notify-send -a 性能管理 省电')
def f_sc1():
  os.system('sudo battmngr -sc 1')
  os.system('notify-send -a 性能管理 快速充电开启')
def f_sc2():
  os.system('sudo battmngr -sc 2')
  os.system('notify-send -a 性能管理 快速充电关闭')
def f_sc3():
  os.system('sudo battmngr -sc 3')
  os.system('notify-send -a 性能管理 电池保护开启')
def f_sc4():
  os.system('sudo battmngr -sc 4')
  os.system('notify-send -a 性能管理 电池保护关闭')

# Creating the options
menu = QMenu()
s1 = QAction("智能冷却")
s2 = QAction("极致性能")
s3 = QAction("省电")
sc1 = QAction("快速充电开启")
sc2 = QAction("快速充电关闭")
sc3 = QAction("电池保护开启")
sc4 = QAction(("电池保护关闭"))
menu.addAction(s1)
menu.addAction(s2)
menu.addAction(s3)
menu.addAction(sc1)
menu.addAction(sc2)
menu.addAction(sc3)
menu.addAction(sc4)

s1.triggered.connect(f_s1)
s2.triggered.connect(f_s2)
s3.triggered.connect(f_s3)
sc1.triggered.connect(f_sc1)
sc2.triggered.connect(f_sc2)
sc3.triggered.connect(f_sc3)
sc4.triggered.connect(f_sc4)

# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)
  
# Adding options to the System Tray
tray.setContextMenu(menu)
  
app.exec_()