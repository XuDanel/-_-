from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QComboBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, \
    QTableWidgetItem

from view.create_hw import Ui_MainWindow
from util.dbUtil import get_conn
import pymysql

class CreateHwUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, course):
        super(CreateHwUi, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.base_set_button.clicked.connect(self.go_base_set)
        self.essay_button.clicked.connect(self.go_essay_button)
        self.multiple_choice_button.clicked.connect(self.go_multiple_choice)
        self.add_button2.clicked.connect(self.add_line2)
        self.add_button1.clicked.connect(self.add_line1)
        self.course = course
        self.submit_button.clicked.connect(self.submit)
        self.choice_table.setColumnCount(6)
        self.choice_table.setHorizontalHeaderLabels(["类型", "问题描述", "选项", "答案", "分值", "添加选项"])
        self.essay_table_2.setColumnCount(4)
        self.essay_table_2.setHorizontalHeaderLabels(["类型", "问题描述", "答案", "分值"])
        self.type_name = {"单选题": "choice"
            , "多选题": "multiple_choice"
            , "判断题": "true_or_false"
            , "简答题": "short_answer"
            , "匹配题": "matching"
            , "论述题": "essay"
            , "填空题": "fill_in_the_blank"
                          }

    def add_line2(self):
        rowPosition = self.choice_table.rowCount()
        self.choice_table.insertRow(rowPosition)
        comboBox = QComboBox()
        comboBox.addItems(["单选题", "多选题"])
        self.choice_table.setCellWidget(rowPosition, 0, comboBox)
        listButton = QPushButton('添加选项')
        listButton.clicked.connect(lambda: self.openContentDialog(rowPosition))
        self.choice_table.setCellWidget(rowPosition, 5, listButton)
        question = QLineEdit()
        answer = QLineEdit()
        value = QLineEdit()
        self.choice_table.setCellWidget(rowPosition, 1, question)
        self.choice_table.setCellWidget(rowPosition, 3, answer)
        self.choice_table.setCellWidget(rowPosition, 4, value)

    def openContentDialog(self, row):
        dialog = QDialog()
        dialog.setWindowTitle('添加选项')
        dialog.setModal(True)
        layout = QVBoxLayout()
        label = QLabel('输入选项:')
        inputLineEdit = QLineEdit()
        buttonBox = QHBoxLayout()
        okButton = QPushButton('确定')
        okButton.clicked.connect(lambda: self.updateList(row, inputLineEdit.text(), dialog))
        cancelButton = QPushButton('取消')
        cancelButton.clicked.connect(dialog.close)
        buttonBox.addWidget(okButton)
        buttonBox.addWidget(cancelButton)
        layout.addWidget(label)
        layout.addWidget(inputLineEdit)
        layout.addLayout(buttonBox)
        dialog.setLayout(layout)
        dialog.exec_()

    def updateList(self, row, content, dialog):
        currentText = self.choice_table.item(row, 2)
        if currentText:
            existingContent = currentText.text()
            newContent = f'{existingContent}, {content}'
        else:
            newContent = content

        item = QTableWidgetItem(newContent)
        self.choice_table.setItem(row, 2, item)
        dialog.close()

    def add_line1(self):
        rowPosition = self.essay_table_2.rowCount()
        self.essay_table_2.insertRow(rowPosition)
        comboBox = QComboBox()
        comboBox.addItems(["判断题", "简答题", "匹配题", "论述题", "填空题"])
        self.essay_table_2.setCellWidget(rowPosition, 0, comboBox)
        question = QLineEdit()
        answer = QLineEdit()
        value = QLineEdit()
        self.essay_table_2.setCellWidget(rowPosition, 1, question)
        self.essay_table_2.setCellWidget(rowPosition, 2, answer)
        self.essay_table_2.setCellWidget(rowPosition, 3, value)

    def go_base_set(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_essay_button(self):
        self.stackedWidget.setCurrentIndex(1)

    def go_multiple_choice(self):
        self.stackedWidget.setCurrentIndex(2)

    def submit(self):
        start_time = self.s_time_dte.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        end_time = self.e_time_dte.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        visible_start_time = self.sv_time_dte.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        visible_end_time = self.se_time_dte.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        title = self.title_line.text()
        conn = get_conn()
        cur = conn.cursor()
        try:
            create_assignment_query = "INSERT INTO assignment (course_id, title, creator_id, start_time, end_time,visible_start_time,visible_end_time) " \
                                      "VALUES (%s,%s, %s, %s, %s, %s, %s)"
            cur.execute(create_assignment_query,
                        (self.course.id, title, self.course.teacher_id, start_time, end_time, visible_start_time,
                         visible_end_time))
            cur.execute("SELECT LAST_INSERT_ID()")
            last_assignment_id = cur.fetchone()[0]
            for row in range(self.choice_table.rowCount()):
                question_type = self.choice_table.cellWidget(row, 0).currentText()
                question_text = self.choice_table.cellWidget(row, 1).text()
                answer = self.choice_table.cellWidget(row, 3).text()
                score = self.choice_table.cellWidget(row, 4).text()
                create_question_query = "INSERT INTO question (question_type, question_text, creator_id, answer, score) " \
                                        "VALUES (%s, %s, %s, %s, %s)"
                cur.execute(create_question_query,
                            (question_type, question_text, self.course.teacher_id, answer, score))
                # 获取刚刚插入的 question_id
                cur.execute("SELECT LAST_INSERT_ID()")
                last_question_id = cur.fetchone()[0]
                choices = self.choice_table.item(row, 2).text().split(",")
                for choice_text in choices:
                    create_choice_query = "INSERT INTO choice (question_id,choice_text)" \
                                          "VALUES (%s ,%s)"
                    cur.execute(create_choice_query, (last_question_id, choice_text))

                update_assignment_questions_query = "INSERT INTO assignment_question (question_id, assignment_id, question_text) " \
                                                    "VALUES (%s,%s, %s)"
                cur.execute(update_assignment_questions_query,
                            (last_question_id, last_assignment_id, question_text))
            for row2 in range(self.essay_table_2.rowCount()):
                question_type = self.essay_table_2.cellWidget(row2, 0).currentText()
                question_text = self.essay_table_2.cellWidget(row2, 1).text()
                answer = self.essay_table_2.cellWidget(row2, 2).text()
                score = self.essay_table_2.cellWidget(row2, 3).text()
                create_question_query = "INSERT INTO question (question_type, question_text, creator_id, answer, score) " \
                                        "VALUES (%s, %s, %s, %s, %s)"
                cur.execute(create_question_query,
                            (question_type, question_text, self.course.teacher_id, answer, score))
                cur.execute("SELECT LAST_INSERT_ID()")
                last_question_id = cur.fetchone()[0]
                update_assignment_questions_query = "INSERT INTO assignment_question (question_id, assignment_id, question_text) " \
                                                    "VALUES (%s,%s, %s)"
                cur.execute(update_assignment_questions_query,
                            (last_question_id, last_assignment_id, question_text))
            print("提交成功")
            conn.close()
        except pymysql.Error as e:
            print(e)
        self.close()
