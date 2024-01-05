import pymysql
from PyQt5.QtWidgets import QMessageBox

import view
import sys

from model.student import Student

from util import dbUtil
from view.edit_info_view import Ui_edit_info
from PyQt5 import QtWidgets
from util.dbUtil import get_conn
import util.dbUtil
from model import student
from model.teacher import Teacher
from model.student import Student


class ChangeInfoUi(QtWidgets.QMainWindow, Ui_edit_info):
    def __init__(self, teacher):
        super(ChangeInfoUi, self).__init__()
        self.setupUi(self)
        self.button_confirm.clicked.connect(self.click_confirm_button)
        self.teacher = teacher

    def click_confirm_button(self):
        email = self.line_email.text()
        phone = self.line_phone.text()
        gender = self.line_gender.text()
        conn=get_conn()
        cur=conn.cursor()
        modify_information_query = f"UPDATE teacher SET email='{email}',gender='{gender}',phone_number='{phone}'  WHERE teacher_id = %s"
        try:
            cur.execute(modify_information_query, self.teacher.info["teacher_id"])
            conn.commit()
            QMessageBox.warning(self,"提示","修改成功")

            conn.close()
            self.close()
        except pymysql.Error as e:
            print(e)
            conn.close()
