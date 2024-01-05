import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox

from model.course import Course
from ui.change_info_ui import ChangeInfoUi
from ui.change_password_ui import ChangePasswordUi
from ui.course_ui import CourseUi
from util import dbUtil
from view.teacherView import Ui_TeacherWindow
from PyQt5 import QtWidgets
from util.dbUtil import get_conn
from model import student
from model.teacher import Teacher
from ui.create_course_ui import CreateCourseUi


class TeacherUi(QtWidgets.QMainWindow, Ui_TeacherWindow):
    def __init__(self, teacher):
        super(TeacherUi, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.teacher = teacher
        self.setWindowTitle("欢迎你，教师" + teacher.info["name"])
        self.label.setText("欢迎你，教师" + self.teacher.info["name"])
        self.account_button.clicked.connect(self.go_account)
        self.course_button.clicked.connect(self.go_course)
        self.back_button.clicked.connect(self.go_back)
        self.view_courses_button.clicked.connect(self.view_courses)
        self.change_info_button.clicked.connect(self.change_info)
        self.create_new_course_button.clicked.connect(self.click_new_course)
        self.change_info_button.clicked.connect(self.click_change_info)
        self.change_password_button.clicked.connect(self.click_change_password)

    def click_change_info(self):
        self.change_info_ui = ChangeInfoUi(self.teacher)
        self.change_info_ui.show()
    def click_change_password(self):
        self.change_password_ui=ChangePasswordUi(self.teacher)
        self.change_password_ui.show()
    def click_new_course(self):
        self.create_course_ui = CreateCourseUi(self.teacher)
        self.create_course_ui.show()

    def go_account(self):
        conn = get_conn()
        cur = conn.cursor()
        sql = "SELECT * FROM teacher where teacher_id={}".format(self.teacher.info["teacher_id"])
        # print(sql)
        cur.execute(sql)
        teacher_info = cur.fetchall()
        print(teacher_info)
        teacher = Teacher(teacher_info[0])
        self.teacher = teacher
        self.ID_label.setText(self.teacher.info["teacher_id"])
        self.email_label.setText(self.teacher.info["email"])
        self.phone_label.setText(self.teacher.info["phone_number"])
        self.college_label.setText(self.teacher.info["college_id"])
        self.gender_label.setText(self.teacher.info["gender"])
        self.name_label.setText(self.teacher.info["name"])
        self.stackedWidget.setCurrentIndex(1)

    # 展示总体课程面板
    def go_course(self):
        self.course_table.clearContents()
        self.stackedWidget.setCurrentIndex(3)
        self.course_table.setRowCount(100)
        self.course_table.setColumnCount(4)
        self.course_table.setHorizontalHeaderLabels(["课程号", "课程名称", "开课时间", "操作"])
        info = self.teacher.get_teacher_courses()
        print(info)
        for row in range(len(info)):
            for col in range(3):
                item = QTableWidgetItem(str(info[row][col]))
                self.course_table.setItem(row, col, item)
            button = QPushButton("详情", self.course_table)
            button.clicked.connect(lambda checked, r=row: self.click_button(r))
            self.course_table.setCellWidget(row, 3, button)

    # 点击“详情”进入具体课程操作页面
    def click_button(self, row):
        course_id = self.course_table.item(row, 0).text()
        course_name = self.course_table.item(row, 1).text()
        print(course_id, course_name)
        course = Course(course_id, course_name, self.teacher.info["teacher_id"])
        self.course_ui = CourseUi(course)
        self.course_ui.show()

    def go_back(self):
        self.stackedWidget.setCurrentIndex(0)

    # 点击“查看所有课程”，刷新课程表格
    def view_courses(self):
        self.course_table.clearContents()
        info = self.teacher.get_teacher_courses()
        print(info)
        for row in range(len(info)):
            for col in range(3):
                item = QTableWidgetItem(str(info[row][col]))
                self.course_table.setItem(row, col, item)
            button = QPushButton("详情")
            button.clicked.connect(self.click_button)
            self.course_table.setCellWidget(row, 3, button)

    def change_info(self):
        pass
