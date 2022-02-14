import sys
from PyQt5 import QtCore, QtWidgets, uic
from plyer import notification

Form, _ = uic.loadUiType('calendar.ui')

class MainWindow(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #Connect the selection changed event in the calendar widget to call calendar_date
        self.calendar.selectionChanged.connect(self.calendar_date)
    
    #Calendar date function, sends notification to OS with date clicked.
    def calendar_date(self):
        notification.notify(
            title = "", 
            message = str(self.calendar.selectedDate().toPyDate()), 
            app_icon = None, 
            timeout = 10, 
            ticker="", 
            toast = False)

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()