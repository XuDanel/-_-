from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QComboBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, \
    QTableWidgetItem, QMessageBox

from view.create_course import Ui_MainWindow
from util.dbUtil import get_conn
import pymysql


class CreateCourseUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, teacher):
        super(CreateCourseUi, self).__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(self.click_submit_button)
        self.teacher = teacher

    def click_submit_button(self):
        course_id = self.course_id_line.text()
        course_name = self.course_name_line.text()
        course_time = self.course_time_line.text()
        if (len(course_time) == 0) or (len(course_name) == 0) or (len(course_id) == 0):
            QMessageBox.warning(self, "错误", "三项不能为空")
        else:
            conn = get_conn()
            cur = conn.cursor()
            try:
                create_course_query = "INSERT INTO course (course_id,course_name, academic_year_semester, teacher_id) " \
                                      "VALUES (%s,%s, %s, %s)"
                cur.execute(create_course_query,
                            (course_id, course_name, course_time, self.teacher.info["teacher_id"]))
                conn.commit()
                QMessageBox.warning(self, "提示", "课程创建成功")
                self.close()
            except pymysql.Error as e:
                QMessageBox.warning(self, "错误", "课程号存在")
