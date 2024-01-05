from model import teacher
from ui.loginUi import LoginUi
from ui.teacher_ui import TeacherUi
from view import LoginView
import sys
from PyQt5 import QtWidgets

# 从登录界面进入
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    loginUi=LoginUi()
    loginUi.show()
    sys.exit(app.exec_())

