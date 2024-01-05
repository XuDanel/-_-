import pymysql
from PyQt5.QtWidgets import QMessageBox

import view
import sys

from model.student import Student

from util import dbUtil
from view.change_password import Ui_MainWindow
from PyQt5 import QtWidgets
from util.dbUtil import get_conn
import util.dbUtil
from model import student
from model.teacher import Teacher
from model.student import Student


class ChangePasswordUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, teacher):
        super(ChangePasswordUi, self).__init__()

        self.setupUi(self)
        self.teacher = teacher
        self.submit_button.clicked.connect(self.click_submit_button)


    def click_submit_button(self):
        old_p = self.old_password_line.text()
        new_p = self.newpassword_line.text()
        twice_p = self.twice_password_line.text()
        conn = get_conn()
        cur = conn.cursor()
        if len(old_p == 0) or len(new_p == 0) or len(twice_p == 0):
            QMessageBox.warning(self, "错误", "不能为空")
        elif old_p != self.teacher.info["password"]:
            QMessageBox.warning(self, "错误", "旧密码不正确")
        elif new_p != twice_p:
            QMessageBox.warning(self, "错误", "重复密码不正确")
        else:
            print(11111)
            modify_information_query = "UPDATE teacher SET password='{}'  WHERE teacher_id = '{}'".format(new_p, self.teacher.info["teacher_id"])
            try:
                print(modify_information_query)
                cur.execute(modify_information_query)
                conn.commit()
                QMessageBox.warning(self, "提示", "修改成功")
                conn.close()
                self.close()
            except pymysql.Error as e:
                print(e)
                conn.close()
