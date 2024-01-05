import pymysql
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton
from random_words import RandomWords
import view
import sys

from model.student import Student
from ui.correct_hw_ui import CorrectHwUi
from ui.create_hw_ui import CreateHwUi
from ui.discuss_ui import DiscussUi
from util import dbUtil
from view.LoginView import Ui_MainWindow
from PyQt5 import QtWidgets
from view.course_view import Ui_MainWindow
from model.course import Course
import util.dbUtil
from model import student
from model.teacher import Teacher
from model.teacher import Teacher
from util.dbUtil import get_conn


class CourseUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, course):
        super(CourseUi, self).__init__()
        self.setupUi(self)
        self.course = course
        self.course_name.setText(course.name)
        self.discuss_button.clicked.connect(self.click_discuss_button)
        self.material_button.clicked.connect(self.click_material_button)
        self.view_hw_button.clicked.connect(self.click_view_hw_button)
        self.create_hw_button.clicked.connect(self.click_create_hw_button)
        self.stu_info_button.clicked.connect(self.click_stu_info_button)

    def click_stu_info_button(self):
        course_stu = self.course.get_students_in_course()
        print(course_stu)
        self.info_table.clear()
        if len(course_stu) == 0:
            self.info_table.setRowCount(0)
            self.info_table.setColumnCount(2)
            self.info_table.setHorizontalHeaderLabels(["学号", "姓名"])
        else:
            len_row = len(course_stu)
            len_col = len(course_stu[0])
            self.info_table.setRowCount(len_row)
            self.info_table.setColumnCount(len_col)
            self.info_table.setHorizontalHeaderLabels(["学号", "姓名"])
            for row in range(len_row):
                for col in range(len_col):
                    item = QTableWidgetItem(str(course_stu[row][col]))
                    self.info_table.setItem(row, col, item)

    def click_material_button(self):
        rw = RandomWords()
        course_query = "SELECT course_id FROM course WHERE teacher_id = %s"
        conn = get_conn()
        cur = conn.cursor()
        num_book = 10
        for j in range(num_book):
            title = rw.random_word() + ' ' + rw.random_word() + ' ' + rw.random_word()
            content = rw.random_word() + ' ' + rw.random_word() + ' ' + rw.random_word()
            insert_mat_query = "INSERT INTO course_material(course_id,title,uploader_id,content,visibility) VALUES(%s,%s,%s,%s,%s)"
            cur.execute(insert_mat_query, (self.course.id, title, self.course.teacher_id, content, 'Public'))
        QMessageBox.warning(self, "提示", f"已成功为本课程上传{num_book}份教材！")
        conn.close()

    def click_view_hw_button(self):
        assignments = self.course.get_hw_in_course()
        self.info_table.clear()
        self.info_table.setColumnCount(4)
        self.info_table.setHorizontalHeaderLabels(["作业编号", "作业题目", "问题", "批改"])
        if len(assignments) == 0:
            self.info_table.setRowCount(0)
        if len(assignments) != 0:
            len_row = len(assignments)
            len_col = len(assignments[0])
            self.info_table.setRowCount(len_row)
            for row in range(len_row):
                for col in range(len_col):
                    item = QTableWidgetItem(str(assignments[row][col]))
                    self.info_table.setItem(row, col, item)
                correct_button = QPushButton("批改")
                correct_button.clicked.connect(lambda checked, row_=row: self.click_correct_button(row_))
                self.info_table.setCellWidget(row, 3, correct_button)

    def click_correct_button(self, row):
        assignment_id = self.info_table.item(row, 0).text()
        print(assignment_id)
        self.correct_hw_ui = CorrectHwUi(self.course, assignment_id)
        self.correct_hw_ui.show()

    def click_create_hw_button(self):
        self.create_hw_ui = CreateHwUi(self.course)
        self.create_hw_ui.show()

    def click_discuss_button(self):
        self.info_table.clear()
        sections = self.course.get_sections()
        self.info_table.setColumnCount(3)
        self.info_table.setHorizontalHeaderLabels(["模块号", "模块名", "进入"])
        if len(sections) == 0:
            self.info_table.setRowCount(0)
        else:
            len_row = len(sections)
            len_col = 3
            self.info_table.setRowCount(len_row)
            for row in range(len_row):
                for col in range(len_col - 1):
                    item = QTableWidgetItem(str(sections[row][col]))
                    self.info_table.setItem(row, col, item)
                enter_button = QPushButton("进入")
                enter_button.clicked.connect(lambda checked, row_=row: self.click_enter_button(row_))
                self.info_table.setCellWidget(row, 2, enter_button)

    def click_enter_button(self, row):
        section_id = self.info_table.item(row, 0).text()
        self.discuss_ui = DiscussUi(section_id, self.course.teacher_id)
        self.discuss_ui.show()
