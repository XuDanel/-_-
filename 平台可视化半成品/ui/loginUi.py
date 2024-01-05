import pymysql
from PyQt5.QtWidgets import QMessageBox

import view
import sys

from model.student import Student
from ui.teacher_ui import TeacherUi
from util import dbUtil
from view.LoginView import Ui_MainWindow
from PyQt5 import QtWidgets
import util.dbUtil
from model import student
from model.teacher import Teacher

class LoginUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()
        self.setupUi(self)

    def clickLoginButton(self):
        id = self.idLine.text()
        password = self.passwordLine.text()
        identity = self.identityBox.currentText()
        # 要加一个是否为空的判断
        if ""==id:
            QMessageBox.warning(self, "错误", "ID不能为空")
        elif ""==password:
            QMessageBox.warning(self, "错误", "密码不能为空")
        else:
            conn = dbUtil.get_conn()
            cur = conn.cursor()
            print(identity)
            if identity == "学生":
                sql = "SELECT * FROM student where student_id={}".format(id)
                cur.execute(sql)
                student_info = cur.fetchall()
                if student_info:
                    stu = Student(student_info[0])
                    if stu.info["password"] == password:

                        pass
                        # studentlogin
                    else:
                        QMessageBox.warning(self, "错误", "密码错误")
                else:
                    QMessageBox.warning(self, "错误", "用户不存在")
            elif identity == "教师":
                sql = "SELECT * FROM teacher where teacher_id={}".format(id)
                # print(sql)
                cur.execute(sql)
                teacher_info = cur.fetchall()
                if teacher_info:
                    teacher = Teacher(teacher_info[0])
                    if teacher.info["password"] == password:
                        self.teacher_ui = TeacherUi(teacher)
                        self.teacher_ui.show()
                        self.close()
                    else:
                        QMessageBox.warning(self, "错误", "密码错误")
                else:
                    QMessageBox.warning(self, "错误", "用户不存在")
            elif identity == "管理员":
                sql = "SELECT * FROM admin where teacher_id={}".format(id)
                cur.execute(sql)
                admin_info = cur.fetchall()
                if admin_info:
                    admin = Student(admin_info[0])
                    if admin.info["password"] == password:
                        pass
                        # studentlogin
                    else:
                        QMessageBox.warning(self, "错误", "密码错误")
                else:
                    QMessageBox.warning(self, "错误", "用户不存在")
                # elif identity=="教师":
                #
                # elif identity=="管理员":
            conn.close()



