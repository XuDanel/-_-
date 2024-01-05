import pymysql
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QStyledItemDelegate, QItemDelegate
from util.dbUtil import get_conn
import view
import sys

from model.student import Student

from util import dbUtil
from view.correct_hw import Ui_MainWindow
from PyQt5 import QtWidgets
import util.dbUtil
from model import student
from model.teacher import Teacher


class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None

class CorrectHwUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, course, assignment_id):
        super(CorrectHwUi, self).__init__()
        self.setupUi(self)
        self.course = course
        self.correct_table.setColumnCount(5)
        self.correct_table.setHorizontalHeaderLabels(["学生学号", "作业", "学生回答", "评分", "评语"])
        self.assignment_id=assignment_id
        self.assignments = self.course.get_assignments_in_course(self.assignment_id)
        print(self.assignments)
        self.correct_table.setRowCount(len(self.assignments))
        for row in range(len(self.assignments)):
            if self.assignments[row][4] is not None:  # .submission_time
                item0=QTableWidgetItem(str(self.assignments[row][1]))
                self.correct_table.setItem(row, 0, item0)
                item1 = QTableWidgetItem(str(self.assignments[row][3]))
                self.correct_table.setItem(row, 1, item1)
                item2 = QTableWidgetItem(str(self.assignments[row][7]))
                self.correct_table.setItem(row, 2, item2)
                item3 = QTableWidgetItem(str(self.assignments[row][5]))
                self.correct_table.setItem(row, 3, item3)
                item4 = QTableWidgetItem(str(self.assignments[row][6]))
                self.correct_table.setItem(row, 4, item4)
                # student_id, assignment_title,student_answer,grade, comment
        #前三行不可编辑
        for i in range(3):
            self.correct_table.setItemDelegateForColumn(i,EmptyDelegate(self))
        self.correct_table.cellChanged.connect(self.change)

    def change(self,row,col):
        try:
            conn = get_conn()
            cur = conn.cursor()
            new_grade = self.correct_table.item(row, 3).text()
            new_comment = self.correct_table.item(row, 4).text()
            student_assignment_id = self.assignments[row][0]
            # print(row,col)
            # print(new_grade,new_comment,student_assignment_id)
            update_query = "UPDATE student_assignment " \
                           "SET grade = {}, comment ='{}' " \
                           "WHERE student_assignment_id = {}".format(new_grade, new_comment, student_assignment_id)
            print(update_query)
            cur.execute(update_query)
            conn.commit()
            print("修改成功")
            conn.close()
        except pymysql.Error as e:
            print(e)
