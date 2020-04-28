""" Qt based TaskUI implementation """


from ..task import Task


from ..ui import TaskUI

from PyQt5.QtWidgets import QMainWindow, QWidget, QProgressBar
from PyQt5.QtWidgets import QApplication

class _TaskUIQt(TaskUI):
    def __init__(self, task):
        super().__init__(task)

    def run(self):
        import sys
        import threading

        app = QApplication(sys.argv)

        uiMain = QMainWindow()
        taskName = 'dummy'
        uiMain.setWindowTitle(f"QBackup: [{taskName}]")

        taskGauge = QProgressBar(uiMain)
        taskGauge.setMaximum(100)
        taskGauge.setMinimum(0)
        taskGauge.setValue(0)

        uiMain.setCentralWidget(taskGauge)        

        uiMain.setGeometry(300, 300, 350, 50)
        uiMain.show()

        self._task.run(wait = False)

        def task_monitor():
            taskGauge.setValue(self._task.progress * 100)
            if self._task.status != Task.Status.DONE:
                self.timer = threading.Timer(1, task_monitor)
                self.timer.start()
            else:
                print('done')

        self.timer = threading.Timer(1, task_monitor)
        self.timer.start()

        app.exec_()


def run(task):
    _TaskUIQt(task).run()
