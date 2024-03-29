# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacherView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeacherWindow(object):
    def setupUi(self, TeacherWindow):
        TeacherWindow.setObjectName("TeacherWindow")
        TeacherWindow.resize(869, 703)
        self.centralwidget = QtWidgets.QWidget(TeacherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 831, 651))
        self.frame.setMinimumSize(QtCore.QSize(761, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(140, 441))
        self.frame_2.setMaximumSize(QtCore.QSize(140, 1000))
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.account_button = QtWidgets.QPushButton(self.frame_2)
        self.account_button.setMinimumSize(QtCore.QSize(100, 60))
        self.account_button.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.account_button.setFont(font)
        self.account_button.setAutoDefault(False)
        self.account_button.setObjectName("account_button")
        self.verticalLayout.addWidget(self.account_button)
        self.course_button = QtWidgets.QPushButton(self.frame_2)
        self.course_button.setMinimumSize(QtCore.QSize(100, 60))
        self.course_button.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.course_button.setFont(font)
        self.course_button.setAutoDefault(False)
        self.course_button.setObjectName("course_button")
        self.verticalLayout.addWidget(self.course_button)
        self.back_button = QtWidgets.QPushButton(self.frame_2)
        self.back_button.setMinimumSize(QtCore.QSize(100, 60))
        self.back_button.setMaximumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.back_button.setFont(font)
        self.back_button.setAutoDefault(False)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)
        self.horizontalLayout.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.main_page)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.stackedWidget.addWidget(self.main_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.info_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.info_page)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 441))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMinimumSize(QtCore.QSize(421, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setMaximumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.ID_label = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.ID_label.setFont(font)
        self.ID_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.ID_label.setObjectName("ID_label")
        self.horizontalLayout_2.addWidget(self.ID_label)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setMinimumSize(QtCore.QSize(421, 0))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_20 = QtWidgets.QLabel(self.frame_12)
        self.label_20.setMaximumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_11.addWidget(self.label_20)
        self.name_label = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_11.addWidget(self.name_label)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setMinimumSize(QtCore.QSize(421, 0))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_18 = QtWidgets.QLabel(self.frame_11)
        self.label_18.setMaximumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_10.addWidget(self.label_18)
        self.gender_label = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.gender_label.setFont(font)
        self.gender_label.setObjectName("gender_label")
        self.horizontalLayout_10.addWidget(self.gender_label)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setMinimumSize(QtCore.QSize(421, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setMaximumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.college_label = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.college_label.setFont(font)
        self.college_label.setObjectName("college_label")
        self.horizontalLayout_7.addWidget(self.college_label)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setMinimumSize(QtCore.QSize(421, 0))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_24 = QtWidgets.QLabel(self.frame_14)
        self.label_24.setMaximumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_13.addWidget(self.label_24)
        self.phone_label = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.horizontalLayout_13.addWidget(self.phone_label)
        self.verticalLayout_3.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setMinimumSize(QtCore.QSize(421, 0))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_22 = QtWidgets.QLabel(self.frame_13)
        self.label_22.setMaximumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.email_label = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.horizontalLayout_12.addWidget(self.email_label)
        self.verticalLayout_3.addWidget(self.frame_13)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(321, 65))
        self.frame_5.setMaximumSize(QtCore.QSize(1000, 65))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_info_button = QtWidgets.QPushButton(self.frame_5)
        self.change_info_button.setMinimumSize(QtCore.QSize(75, 45))
        self.change_info_button.setMaximumSize(QtCore.QSize(75, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.change_info_button.setFont(font)
        self.change_info_button.setAutoDefault(False)
        self.change_info_button.setObjectName("change_info_button")
        self.horizontalLayout_4.addWidget(self.change_info_button)
        self.change_password_button = QtWidgets.QPushButton(self.frame_5)
        self.change_password_button.setMinimumSize(QtCore.QSize(75, 45))
        self.change_password_button.setMaximumSize(QtCore.QSize(75, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.change_password_button.setFont(font)
        self.change_password_button.setAutoDefault(False)
        self.change_password_button.setObjectName("change_password_button")
        self.horizontalLayout_4.addWidget(self.change_password_button)
        self.change_password_button_2 = QtWidgets.QPushButton(self.frame_5)
        self.change_password_button_2.setMinimumSize(QtCore.QSize(75, 45))
        self.change_password_button_2.setMaximumSize(QtCore.QSize(75, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.change_password_button_2.setFont(font)
        self.change_password_button_2.setAutoDefault(False)
        self.change_password_button_2.setObjectName("change_password_button_2")
        self.horizontalLayout_4.addWidget(self.change_password_button_2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.info_page)
        self.discuss_page = QtWidgets.QWidget()
        self.discuss_page.setObjectName("discuss_page")
        self.stackedWidget.addWidget(self.discuss_page)
        self.course_page = QtWidgets.QWidget()
        self.course_page.setObjectName("course_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.course_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.course_page)
        self.frame_6.setMinimumSize(QtCore.QSize(331, 71))
        self.frame_6.setMaximumSize(QtCore.QSize(1000, 71))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.view_courses_button = QtWidgets.QPushButton(self.frame_6)
        self.view_courses_button.setMinimumSize(QtCore.QSize(91, 31))
        self.view_courses_button.setMaximumSize(QtCore.QSize(91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.view_courses_button.setFont(font)
        self.view_courses_button.setObjectName("view_courses_button")
        self.horizontalLayout_8.addWidget(self.view_courses_button)
        self.create_new_course_button = QtWidgets.QPushButton(self.frame_6)
        self.create_new_course_button.setMinimumSize(QtCore.QSize(91, 31))
        self.create_new_course_button.setMaximumSize(QtCore.QSize(91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.create_new_course_button.setFont(font)
        self.create_new_course_button.setObjectName("create_new_course_button")
        self.horizontalLayout_8.addWidget(self.create_new_course_button)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.course_table = QtWidgets.QTableWidget(self.course_page)
        self.course_table.setObjectName("course_table")
        self.course_table.setColumnCount(0)
        self.course_table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.course_table)
        self.stackedWidget.addWidget(self.course_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        TeacherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TeacherWindow)
        self.statusbar.setObjectName("statusbar")
        TeacherWindow.setStatusBar(self.statusbar)
        self.editInfo = QtWidgets.QAction(TeacherWindow)
        self.editInfo.setObjectName("editInfo")
        self.logout = QtWidgets.QAction(TeacherWindow)
        self.logout.setObjectName("logout")
        self.actiona = QtWidgets.QAction(TeacherWindow)
        self.actiona.setObjectName("actiona")
        self.actiona_2 = QtWidgets.QAction(TeacherWindow)
        self.actiona_2.setObjectName("actiona_2")
        self.actionb = QtWidgets.QAction(TeacherWindow)
        self.actionb.setObjectName("actionb")
        self.actionc = QtWidgets.QAction(TeacherWindow)
        self.actionc.setObjectName("actionc")
        self.actiona_3 = QtWidgets.QAction(TeacherWindow)
        self.actiona_3.setObjectName("actiona_3")
        self.actionb_2 = QtWidgets.QAction(TeacherWindow)
        self.actionb_2.setObjectName("actionb_2")
        self.actionc_2 = QtWidgets.QAction(TeacherWindow)
        self.actionc_2.setObjectName("actionc_2")
        self.actiond = QtWidgets.QAction(TeacherWindow)
        self.actiond.setObjectName("actiond")

        self.retranslateUi(TeacherWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TeacherWindow)

    def retranslateUi(self, TeacherWindow):
        _translate = QtCore.QCoreApplication.translate
        TeacherWindow.setWindowTitle(_translate("TeacherWindow", "欢迎你"))
        self.account_button.setText(_translate("TeacherWindow", "账号管理"))
        self.course_button.setText(_translate("TeacherWindow", "课程管理"))
        self.back_button.setText(_translate("TeacherWindow", "返回主页"))
        self.label.setText(_translate("TeacherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">欢迎你，教师xxx</span></p></body></html>"))
        self.label_6.setText(_translate("TeacherWindow", "ID"))
        self.ID_label.setText(_translate("TeacherWindow", "ID"))
        self.label_20.setText(_translate("TeacherWindow", "姓名"))
        self.name_label.setText(_translate("TeacherWindow", "ID"))
        self.label_18.setText(_translate("TeacherWindow", "性别"))
        self.gender_label.setText(_translate("TeacherWindow", "ID"))
        self.label_9.setText(_translate("TeacherWindow", "院系"))
        self.college_label.setText(_translate("TeacherWindow", "ID"))
        self.label_24.setText(_translate("TeacherWindow", "电话"))
        self.phone_label.setText(_translate("TeacherWindow", "ID"))
        self.label_22.setText(_translate("TeacherWindow", "邮箱"))
        self.email_label.setText(_translate("TeacherWindow", "ID"))
        self.change_info_button.setText(_translate("TeacherWindow", "修改信息"))
        self.change_password_button.setText(_translate("TeacherWindow", "修改密码"))
        self.change_password_button_2.setText(_translate("TeacherWindow", "退出账号"))
        self.view_courses_button.setText(_translate("TeacherWindow", "查看所有课程"))
        self.create_new_course_button.setText(_translate("TeacherWindow", "创建新课程"))
        self.editInfo.setText(_translate("TeacherWindow", "账户信息"))
        self.logout.setText(_translate("TeacherWindow", "退出账户"))
        self.actiona.setText(_translate("TeacherWindow", "查看所有课程"))
        self.actiona_2.setText(_translate("TeacherWindow", "创建新课程"))
        self.actionb.setText(_translate("TeacherWindow", "复制已有课程"))
        self.actionc.setText(_translate("TeacherWindow", "c"))
        self.actiona_3.setText(_translate("TeacherWindow", "查看讨论区"))
        self.actionb_2.setText(_translate("TeacherWindow", "b"))
        self.actionc_2.setText(_translate("TeacherWindow", "c"))
        self.actiond.setText(_translate("TeacherWindow", "d"))
