from datetime import datetime

import pymysql
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton

import view
import sys

from model.student import Student

from util import dbUtil
from view.discuss import Ui_MainWindow
from PyQt5 import QtWidgets
from util.dbUtil import get_conn
from model import student
from model.teacher import Teacher


class DiscussUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, section_id,teacher_id):
        super(DiscussUi, self).__init__()
        self.current_post_id=0
        self.current_row=-1
        self.teacher_id=teacher_id
        self.setupUi(self)
        self.post_table.clear()
        self.post_table.setColumnCount(3)
        self.post_table.setHorizontalHeaderLabels(["内容", "时间", "回复"])
        self.section_id = section_id
        self.reply_table.clear()
        self.posts = self.get_post()
        self.post_table.setRowCount(len(self.posts))
        for row in range(len(self.posts)):
            # print(str(self.posts[row][5]))
            content = QTableWidgetItem(str(self.posts[row][5]))
            self.post_table.setItem(row, 0, content)
            # print(self.posts[row][6])
            time = QTableWidgetItem(str(self.posts[row][6]))
            self.post_table.setItem(row, 1, time)
            button = QPushButton("查看")
            button.clicked.connect(lambda checked, row_=row: self.click_button(row_))
            self.post_table.setCellWidget(row, 2, button)
        self.reply_table.setColumnCount(2)
        self.reply_table.setHorizontalHeaderLabels(["内容", "时间"])
        self.post_button.clicked.connect(self.click_post_button)
        self.reply_button.clicked.connect(self.click_reply_button)

    def click_button(self, row):
        post_id = self.posts[row][0]
        self.current_post_id = post_id
        self.current_row=row
        self.reply_table.clearContents()
        replies = self.get_reply(post_id)# [4] [5]
        self.reply_table.setRowCount(len(replies))
        for row in range(len(replies)):
            for col in range(2):
                content=QTableWidgetItem(str(replies[row][col+4]))
                self.reply_table.setItem(row,col,content)



    def click_post_button(self):
        post_content = self.post_line.text()
        if len(post_content)==0:
            QMessageBox.warning(self,"错误","不允许空白输入")
        try:
            self.post_line.clear()
            conn = get_conn()
            cur = conn.cursor()

            post_time = datetime.now()
            create_forum_post_query = "INSERT INTO forum_post (section_id, teacher_id,post_content,post_time) " \
                                      "VALUES (%s, %s, %s,%s)"
            cur.execute(create_forum_post_query, (self.section_id, self.teacher_id, post_content, post_time))
            conn.commit()
            conn.close()
            QMessageBox.warning(self,"提示","发布成功")
            self.post_table.clearContents()
            self.posts = self.get_post()
            self.post_table.setRowCount(len(self.posts))
            for row in range(len(self.posts)):
                # print(str(self.posts[row][5]))
                content = QTableWidgetItem(str(self.posts[row][5]))
                self.post_table.setItem(row, 0, content)
                # print(self.posts[row][6])
                time = QTableWidgetItem(str(self.posts[row][6]))
                self.post_table.setItem(row, 1, time)
                button = QPushButton("查看")
                button.clicked.connect(lambda checked, row_=row: self.click_button(row_))
                self.post_table.setCellWidget(row, 2, button)
        except pymysql.Error as e:
            print(e)

    def get_post(self):
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM forum_post WHERE section_id = {self.section_id}")
            posts = cur.fetchall()
            return posts
        except pymysql.Error as e:
            print(e)

    def get_reply(self, post_id):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM forum_reply WHERE post_id = {post_id}")
        replies = cur.fetchall()
        conn.close()
        return replies

    def click_reply_button(self):
        reply_content = self.reply_line.text()
        if self.current_post_id==0:
            QMessageBox.warning(self, "错误", "请选择模块")
        elif len(reply_content)==0:
            QMessageBox.warning(self,"错误","不许空白输入")
        else:
            self.reply_line.clear()
            conn = get_conn()
            cur = conn.cursor()
            try:
                reply_time = datetime.now()
                create_forum_reply_query = "INSERT INTO forum_reply (post_id, teacher_id, reply_content,reply_time) " \
                                           "VALUES (%s, %s, %s,%s)"
                cur.execute(create_forum_reply_query,
                            (self.current_post_id, self.teacher_id, reply_content, reply_time))
                conn.commit()
                QMessageBox.warning(self,"提示","回复成功")
                self.click_button(self.current_row)
            except pymysql.Error as e:
                print(e)
            conn.close()

