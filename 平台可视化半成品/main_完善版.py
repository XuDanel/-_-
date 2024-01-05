from typing import Tuple, Any
from random_words import RandomWords
import pymysql
from datetime import datetime


class Teacher:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def modify_personal_information(self):
        key_id_list = ["teacher_id","name","gender","phone_number","email","password","college_id"]
        print("---------个人信息修改页面-----------")
        print("----- 请选择修改项：-------")
        print("-----1、职工号---")
        print("-----2、姓名----")
        print("-----3、性别----")
        print("-----4、电话----")
        print("-----5、邮箱-------")
        print("-----6、密码-------")
        print("-----7、学院-------")
        print("-----0、退出-------")
        print("----------------------")
        mod_key = int(input())
        if mod_key<=0 or mod_key>= 8:
            return
        else:
            print("输入新信息：")
            if mod_key==1 or mod_key == 7:
                new_info = int(input())
            else:
                new_info = input()
            modify_information_query = f"UPDATE teacher SET {key_id_list[mod_key-1]} = %s WHERE teacher_id = %s"
            try:
                cur.execute(modify_information_query, (new_info,self.id))
                print("修改成功！")
                if mod_key == 1:
                    self.id = new_info
                elif mod_key == 2:
                    self.name = new_info
                sql = 'SELECT * FROM teacher where teacher_id=%s'
                cur.execute(sql, self.id)
                teacher_info = cur.fetchall()
                if teacher_info:
                    print(
                        f'职工号: {teacher_info[0][0]}  姓名: {teacher_info[0][1]}  性别: {teacher_info[0][2]}  电话：{teacher_info[0][3]} 邮箱：{teacher_info[0][4]} 学院：{teacher_info[0][6]}')

            except pymysql.Error as e:
                print(e)
                print("请联系管理员修改")


    # 查看该教师的所有课程
    def get_teacher_courses(self):
        get_teacher_courses_query = "SELECT * FROM course WHERE teacher_id = %s"
        cur.execute(get_teacher_courses_query, (self.id,))
        teacher_course_info = cur.fetchall()
        print("---------您开设的课程信息如下-----------")
        if teacher_course_info:
            print("课程号   课程名称          开课时间")
            for row in teacher_course_info:
                print(f'{row[0]}      {row[1]}        {row[2]}')
            return 1
        else:
            print("暂时没有课程信息")

    # 教师端页面
    def teacher_page(self, teacher_info):
        print("-----欢迎登录教师端-----")
        print(
            f'职工号: {teacher_info[0][0]}  姓名: {teacher_info[0][1]}  性别: {teacher_info[0][2]}  邮箱: {teacher_info[0][4]}')
        print("-----请选择功能：-------")
        print("-----1、查看所有课程----")
        print("-----2、创建新的课程----")
        print("-----3、复制已有课程----")
        print("-----4、修改个人信息----")
        print("-----0、退出系统-------")
        print("----------------------")

    # 创建新课程
    def create_course(self, course_id, course_name, academic_year_semester):
        try:
            create_course_query = "INSERT INTO course (course_id,course_name, academic_year_semester, teacher_id) " \
                                  "VALUES (%s,%s, %s, %s)"
            cur.execute(create_course_query, (course_id, course_name, academic_year_semester, self.id))
            print("课程创建成功！")
            return 0
        except pymysql.Error as e:
            return -1

    # 复制已有课程
    def copy_course(self):
        sql = 'SELECT * FROM course'
        cur.execute(sql)
        course_info = cur.fetchall()
        print("----------全部课程信息-----------")
        print("课程号   课程名称          开课时间")
        for row in course_info:
            print(row[0], "  ", row[1], "   ", row[2])
        print("-------------------------------")
        print("请输入要复制的课程的课程号：", end="")
        existing_course_id = int(input())
        flag = 1
        for row in course_info:
            if row[0] == existing_course_id:
                flag = 0
                course_name = row[1]
                academic_year_semester = row[2]
                trial = 0
                while trial < 3:
                    print("请输入新的课程的课程号：")
                    new_course_id = int(input())
                    course_id = new_course_id
                    # 在执行插入之前先查询目标表
                    cur.execute("SELECT course_id FROM course WHERE course_id = %s", (new_course_id,))
                    existing_courses = cur.fetchall()
                    # 如果存在重复，打印错误信息并提示用户重新输入
                    if existing_courses:
                        print("错误：系统里已存在该课程号，请重新输入")
                    else:
                        break
                    trial += 1
                if trial == 3:
                    print("课程复制失败，请确认新课程号后再次尝试")
                    break
                    # 执行插入操作
                create_course_query = "INSERT INTO course (course_id,course_name, academic_year_semester, teacher_id) " \
                                      "VALUES (%s,%s, %s, %s)"
                cur.execute(create_course_query, (new_course_id, course_name, academic_year_semester, self.id))
                print("课程复制成功")
                break
        if flag:
            print("该课程不存在！")
        print("-------------------------------")

    # 创建作业
    def create_assignment(self):
        get_teacher_courses_query = "SELECT * FROM course WHERE teacher_id = %s"
        cur.execute(get_teacher_courses_query, (self.id,))
        teacher_course_info = cur.fetchall()
        print("请选择要添加作业的课程号：", end='')
        course_id = int(input())
        temp = 1
        for row in teacher_course_info:
            if row[0] == course_id:
                temp = 0
                break
        if temp:
            print("请输入正确的课程号（课程号必须是您本人开设的课程）！")
        else:
            try:
                # print("请输入新添加的作业编号：",end="")
                # assignment_id=int(input())
                print("请输入新添加的作业标题：", end="")
                title = input()
                creator_id = self.id
                print("请输入新添加作业的开始时间：(如：2022-02-01 10:00:00)", end="")
                start_time = input()
                print("请输入新添加作业的截止时间：(如：2022-02-10 10:00:00)", end="")
                end_time = input()
                print("请输入新添加作业的可见开始时间：(如：2022-02-01 10:00:00)", end="")
                visible_start_time = input()
                print("请输入新添加作业的可见截止时间：(如：2022-02-10 10:00:00)", end="")
                visible_end_time = input()
                create_assignment_query = "INSERT INTO assignment (course_id, title, creator_id, start_time, end_time,visible_start_time,visible_end_time) " \
                                          "VALUES (%s,%s, %s, %s, %s, %s, %s)"
                cur.execute(create_assignment_query,
                            (course_id, title, creator_id, start_time, end_time, visible_start_time, visible_end_time))
                print("作业创建成功！")
                cur.execute("SELECT LAST_INSERT_ID()")
                last_assignment_id = cur.fetchone()[0]

                print("请选择是否添加问题：1:是  0:否", end="")
                key = int(input())
                # 添加新的问题
                if key:
                    print("请输入要添加的问题数量：", end="")
                    num = int(input())
                    while num > 0:
                        num = num - 1
                        # print("请输入问题编号：",end='')
                        # question_id=int(input())
                        print(f"请从以下选项中选择题目类型：num={num}")
                        print("1、单选题")
                        print("2、多选题")
                        print("3、判断题")
                        print("4、简答题")
                        print("5、匹配题")
                        print("6、论述题")
                        print("7、填空题")
                        print("请输入类型选择：", end="")
                        type_choice = int(input())
                        if type_choice == 1:
                            question_type = "choice"
                        elif type_choice == 2:
                            question_type = "multiple_choice"
                        elif type_choice == 3:
                            question_type = "true_or_false"
                        elif type_choice == 4:
                            question_type = "short_answer"
                        elif type_choice == 5:
                            question_type = "matching"
                        elif type_choice == 6:
                            question_type = "essay"
                        elif type_choice == 7:
                            question_type = "fill_in_the_blank"

                        print("请输入问题描述：", end='')
                        question_text = input()
                        print("请输入问题答案：", end='')
                        answer = input()
                        print("请输入问题分值，1-10分：", end='')
                        score = float(input())
                        creator_id = self.id
                        create_question_query = "INSERT INTO question (question_type, question_text, creator_id, answer, score) " \
                                                "VALUES (%s, %s, %s, %s, %s)"
                        cur.execute(create_question_query, (question_type, question_text, creator_id, answer, score))
                        # 获取刚刚插入的 question_id
                        cur.execute("SELECT LAST_INSERT_ID()")
                        last_question_id = cur.fetchone()[0]
                        # 更新choice表
                        if type_choice == 1 or type_choice == 2:
                            print("请输入选项数量：", end='')
                            num_choices = int(input())
                            for num in range(1, num_choices + 1):
                                print(f"请输入选项{num}：", end='')
                                choice_text = input()
                                create_choice_query = "INSERT INTO choice (question_id,choice_text)" \
                                                      "VALUES (%s ,%s)"
                                cur.execute(create_choice_query, (last_question_id, choice_text))
                        # 更新assignment_question表
                        update_assignment_questions_query = "INSERT INTO assignment_question (question_id, assignment_id, question_text) " \
                                                            "VALUES (%s,%s, %s)"
                        cur.execute(update_assignment_questions_query,
                                    (last_question_id, last_assignment_id, question_text))
            except pymysql.Error as e:
                print(e)

        # 待办：每添加assignment之后，就立即插入student_assignment表！

    # 查看课程的所有作业以及对应作业的所有问题
    def get_all_assignments_with_questions(self):
        get_teacher_courses_query = "SELECT * FROM course WHERE teacher_id = %s"
        cur.execute(get_teacher_courses_query, (self.id,))
        teacher_course_info = cur.fetchall()
        print("请选择要查看作业的课程号：", end='')
        course_id = int(input())
        temp = 1
        for row in teacher_course_info:
            if row[0] == course_id:
                temp = 0
                break
        if temp:
            print("请输入正确的课程号（课程号必须是您本人开设的课程）！")
        else:
            try:
                get_all_assignments_query = "SELECT * FROM assignment WHERE course_id=%s"
                cur.execute(get_all_assignments_query, course_id)
                assignments = cur.fetchall()

                assignments_with_questions = []
                for assignment in assignments:
                    assignment_id = assignment[0]
                    get_questions_for_assignment_query = "SELECT question_text FROM assignment_question " \
                                                         "WHERE assignment_id = %s"
                    cur.execute(get_questions_for_assignment_query, (assignment_id,))
                    questions = cur.fetchall()
                    assignment_with_questions = {
                        "作业编号": assignment_id,
                        "作业题目": assignment[2],
                        "问题": questions
                    }
                    assignments_with_questions.append(assignment_with_questions)
                for row in assignments_with_questions:
                    print(row)
            except pymysql.Error as e:
                print(e)

    # 查看某课程的学生提交的作业
    def view_and_grade_assignments(self):
        get_teacher_courses_query = "SELECT * FROM course WHERE teacher_id = %s"
        cur.execute(get_teacher_courses_query, (self.id,))
        teacher_course_info = cur.fetchall()
        print("请选择要查看作业提交情况和批改的课程号：", end='')
        course_id = int(input())
        temp = 1
        for row in teacher_course_info:
            if row[0] == course_id:
                temp = 0
                break
        if temp:
            print("请输入正确的课程号（课程号必须是您本人开设的课程）！")
        else:
            view_assignments_query = "SELECT sa.student_assignment_id, sa.student_id, sa.assignment_id, " \
                                     "a.title AS assignment_title, sa.submission_time, sa.grade, sa.comment, " \
                                     "sa.student_answer " \
                                     "FROM student_assignment sa " \
                                     "JOIN assignment a ON sa.assignment_id = a.assignment_id " \
                                     "WHERE a.course_id = %s"
            cur.execute(view_assignments_query, (course_id,))
            assignments = cur.fetchall()
            print("学生学号 作业            学生回答           评分    评语")
            for row in assignments:
                if row[4] is not None:
                    print(row[1], '     ', row[3], "  ", row[7], "        ", row[5], "  ", row[6])
            print("是否要批改作业：1、是  2、否")
            k = int(input())
            if k == 1:
                for row in assignments:
                    if row[4] is not None and( row[6] == '' or row[6] is None) :
                        print(row[1], '     ', row[3], "  ", row[7])
                        print("请输入评分：", end='')
                        new_grade = float(input())
                        print("请输入评价：", end='')
                        new_comment = input()
                        student_assignment_id = row[0]
                        # 更新学生作业的评分和评论
                        update_query = "UPDATE student_assignment " \
                                       "SET grade = %s, comment = %s " \
                                       "WHERE student_assignment_id = %s"
                        cur.execute(update_query, (new_grade, new_comment, student_assignment_id))

        # 查看所有选修特定课程的学生

    def get_students_in_course(self):
        print("请输入要查看的课程号：", end='')
        course_id = int(input())
        query = "SELECT s.student_id, s.name " \
                "FROM student s " \
                "JOIN course_enrollment cr ON s.student_id = cr.student_id " \
                "WHERE cr.course_id = %s"
        cur.execute(query, (course_id,))
        course_student = cur.fetchall()
        if course_student:
            print("学号     姓名")
            for row in course_student:
                print(row[0], "   ", row[1])
        else:
            print("暂无选课学生")

    # 创建讨论区板块
    def create_forum_section(self, course_id, section_name):
        create_forum_section_query = "INSERT INTO forum_section (section_name,course_id) " \
                                     "VALUES (%s, %s)"
        cur.execute(create_forum_section_query, (section_name, course_id))
        print("创建模块成功！")

    # 展示讨论区
    def show_section_post_replay(self, course_id):
        # print(course_id)
        # print("SELECT course_name FROM course WHERE course_id = %s"%(course_id,))
        cur.execute("SELECT course_name FROM course WHERE course_id = %s", (course_id,))
        course_name_of_id = cur.fetchone()
        if course_name_of_id:
            print(f"课程号：{course_id}  课程名: {course_name_of_id[0]}")
        # 查询所有讨论区的模块
        cur.execute(f"SELECT * FROM forum_section WHERE forum_section.course_id = {course_id}")
        sections = cur.fetchall()

        # 遍历每个模块
        for section in sections:
            section_id = section[0]
            section_name = section[1]
            print(f"讨论区模块: {section_name}")

            # 查询该模块下的所有帖子
            cur.execute(f"SELECT * FROM forum_post WHERE section_id = {section_id}")
            posts = cur.fetchall()

            # 遍历每个帖子
            for post in posts:
                post_id = post[0]
                post_content = post[5]
                print(f"  帖子内容: {post_content}")

                # 查询该帖子下的所有回复
                cur.execute(f"SELECT * FROM forum_reply WHERE post_id = {post_id}")
                replies = cur.fetchall()

                # 遍历每个回复
                for reply in replies:
                    reply_content = reply[4]
                    print(f"    回复内容: {reply_content}")

    # 创建讨论帖子
    def create_forum_post(self, course_id):
        cur.execute("SELECT * FROM forum_section WHERE forum_section.course_id = %s", (course_id,))
        sections = cur.fetchall()
        for section in sections:
            section_id = section[0]
            section_name = section[1]
            print(f"讨论区模块: {section_id, section_name}")
        if not sections:
            print(f"该课程暂无模块，请先创建模块")
            return -1

        print('请选择您要创建帖子的模块号：', end='')
        section_id = int(input())
        print('请输入创建的帖子内容：', end='')
        post_content = input()
        post_time = datetime.now()
        create_forum_post_query = "INSERT INTO forum_post (section_id, teacher_id,post_content,post_time) " \
                                  "VALUES (%s, %s, %s,%s)"
        cur.execute(create_forum_post_query, (section_id, self.id, post_content, post_time))
        print('帖子创建成功！')

    # 创建讨论回复
    def create_forum_reply(self, course_id):
        # 查询所有讨论区的模块
        cur.execute("SELECT * FROM forum_section WHERE forum_section.course_id = %s", (course_id,))
        sections = cur.fetchall()
        if not sections:
            print(f"该课程暂无模块，请先创建模块")
        # 遍历每个模块
        for section in sections:
            section_id = section[0]
            section_name = section[1]
            print(f"讨论区模块: {section_name}")

            # 查询该模块下的所有帖子
            cur.execute(f"SELECT * FROM forum_post WHERE section_id = {section_id}")
            posts = cur.fetchall()
            if not posts:
                print(f"该模块暂无帖子，请先发布帖子")
            # 遍历每个帖子
            for post in posts:
                post_id = post[0]
                post_content = post[5]
                print(f"  帖子内容: {post_id, post_content}")

        print("请输入要回复的帖子编号：", end='')
        post_id = int(input())
        print("请输入您的回复：", end="")
        reply_content = input()
        reply_time = datetime.now()
        create_forum_reply_query = "INSERT INTO forum_reply (post_id, teacher_id, reply_content,reply_time) " \
                                   "VALUES (%s, %s, %s,%s)"
        cur.execute(create_forum_reply_query, (post_id, self.id, reply_content, reply_time))
        print("回复成功！")

    def forum_section_function_choice(self):
        cur.execute(f"SELECT course_id FROM course WHERE course.teacher_id = {self.id}")
        for course_id1 in (cur.fetchall()):
            self.show_section_post_replay(course_id1[0])
        while True:
            print("请输入想进入讨论区的课程号，或输入0回到上一级：", end="")
            course_id = int(input())
            if course_id == 0:
                break
            cur.execute("SELECT course_name FROM course WHERE course_id = %s", (course_id,))
            course_name_of_id = cur.fetchone()
            if course_name_of_id is None:
                print("请输入正确的课程号（课程号必须是您本人开设的课程）！")
                continue

            while True:
                print("------------------------")
                print(f"-----欢迎进入课程{course_name_of_id[0]}的讨论区--------")
                print("-----可以选择以下功能------")
                print("-----1、创建模块----------")
                print("-----2、创建帖子----------")
                print("-----3、回复帖子----------")
                print("-----4、查看讨论区---------")
                print("-----0、返回上一级---------")
                print("------------------------")
                print("请输入您的选择：", end='')
                m = int(input())
                if m == 1:
                    print("请输入要创建的模块数：")
                    num = int(input())
                    while num > 0:
                        print("请输入新创建的模块名：", end='')
                        new_section_name = input()
                        self.create_forum_section(course_id, new_section_name)
                        num = num - 1
                elif m == 2:
                    self.create_forum_post(course_id)
                elif m == 3:
                    self.create_forum_reply(course_id)
                elif m == 4:
                    self.show_section_post_replay(course_id)
                elif m == 0:
                    break

    def submit_course_material(self):
        print("您需要为所有课程自动上传教材资源吗？1：自动上传，0：退出上传")
        auto = int(input())
        if auto == 1:
            from random_words import RandomWords
            rw = RandomWords()
            course_query = "SELECT course_id FROM course WHERE teacher_id = %s"
            cur.execute(course_query,(self.id,))
            course_res = cur.fetchall()
            if not course_res:
                print("请您先创建课程")
            else:
                for row in course_res:
                    num_book = 10
                    for j in range(num_book):
                        title = rw.random_word() + ' '+rw.random_word() + ' '+rw.random_word()
                        content = rw.random_word() + ' ' + rw.random_word() + ' ' + rw.random_word()
                        insert_mat_query = "INSERT INTO course_material(course_id,title,uploader_id,content,visibility) VALUES(%s,%s,%s,%s,%s)"
                        cur.execute(insert_mat_query, (row[0], title,self.id,content,'Public'))
                    print(f"已成功为课程{row[0]}上传{num_book}份教材！")



class Student:
    def __init__(self,stuInfo,name,id) -> None:
        self.header = ["student_id","name","gender","phone_number","email","password","grade","college_id"]
        if len(stuInfo) == len(self.header):
            self.info = dict(zip(self.header, stuInfo))
            print(self.info)
        else:
            print("Error: Incorrect number of elements in stuInfo.")
        self.name = name
        self.id  = id

    def show_section_post_replay(self, course_id):
        cur.execute("SELECT course_name FROM course WHERE course_id = %s", (course_id,))
        course_name_of_id = cur.fetchone()
        if course_name_of_id is not None:
            print(f"课程号：{course_id}  课程名: {course_name_of_id[0]}")
        # 查询所有讨论区的模块
        cur.execute(f"SELECT * FROM forum_section WHERE forum_section.course_id = {course_id}")
        sections = cur.fetchall()

        # 遍历每个模块
        for section in sections:
            section_id = section[0]
            section_name = section[1]
            print(f"讨论区模块: {section_name}")

            # 查询该模块下的所有帖子
            cur.execute(f"SELECT * FROM forum_post WHERE section_id = {section_id}")
            posts = cur.fetchall()

            # 遍历每个帖子
            for post in posts:
                post_id = post[0]
                post_content = post[5]
                print(f"  帖子内容: {post_content}")

                # 查询该帖子下的所有回复
                cur.execute(f"SELECT * FROM forum_reply WHERE post_id = {post_id}")
                replies = cur.fetchall()

                # 遍历每个回复
                for reply in replies:
                    reply_content = reply[4]
                    print(f"    回复内容: {reply_content}")

    # 创建讨论帖子
    def create_forum_post(self, course_id):
        cur.execute("SELECT * FROM forum_section WHERE forum_section.course_id = %s", (course_id,))
        sections = cur.fetchall()
        for section in sections:
            section_id = section[0]
            section_name = section[1]
            print(f"讨论区模块: {section_id, section_name}")
        if not sections:
            print(f"该课程暂无模块，请等待教师创建模块")
            return -1

        print('请选择您要创建帖子的模块号：', end='')
        section_id = int(input())
        print('请输入创建的帖子内容：', end='')
        post_content = input()
        post_time = datetime.now()
        create_forum_post_query = "INSERT INTO forum_post (section_id, student_id, post_content,post_time) " \
                                  "VALUES (%s, %s, %s,%s)"
        cur.execute(create_forum_post_query, (section_id, self.id, post_content, post_time))
        print('帖子创建成功！')

    # 创建讨论回复
    def create_forum_reply(self, course_id):
        # 查询所有讨论区的模块
        cur.execute("SELECT * FROM forum_section WHERE forum_section.course_id = %s", (course_id,))
        sections = cur.fetchall()
        if not sections:
            print(f"该课程暂无模块，请等待教师创建模块")
        # 遍历每个模块
        for section in sections:
            section_id = section[0]
            section_name = section[1]
            print(f"讨论区模块: {section_name}")

            # 查询该模块下的所有帖子
            cur.execute(f"SELECT * FROM forum_post WHERE section_id = {section_id}")
            posts = cur.fetchall()
            if not posts:
                print(f"该模块暂无帖子，请先发布帖子")
            # 遍历每个帖子
            for post in posts:
                post_id = post[0]
                post_content = post[5]
                print(f"  帖子内容: {post_id, post_content}")

        print("请输入要回复的帖子编号：", end='')
        post_id = int(input())
        print("请输入您的回复：", end="")
        reply_content = input()
        reply_time = datetime.now()
        create_forum_reply_query = "INSERT INTO forum_reply (post_id, student_id, reply_content,reply_time) " \
                                   "VALUES (%s, %s, %s,%s)"
        cur.execute(create_forum_reply_query, (post_id, self.id, reply_content, reply_time))
        print("回复成功！")

    def show_learning_page(self, student_info):
        print(
            f'学号: {student_info[0][0]}  姓名: {student_info[0][1]}  性别: {student_info[0][2]}  邮箱: {student_info[0][4]}')
        print("--------------------------")
        while True:
            print("以下功能可以选择：")
            print("1、查看选课信息")
            print("2、查看所有作业")
            print("3、查看未提交作业")
            print("4、提交未提交作业")
            print("5、查看课程材料信息")
            print("6、进入讨论区")
            print("0、退出程序")
            choice = int(input())
            if choice == 1:
                # 查询学生选课信息 ,显示所选的所有课程
                course_query = "SELECT c.course_id,c.course_name, c.academic_year_semester FROM course_enrollment ce " \
                               "JOIN course c ON ce.course_id = c.course_id " \
                               " WHERE ce.student_id = %s"
                cur.execute(course_query, (self.id,))
                course_info = cur.fetchall()
                print("----------选课信息----------")
                print("   课程名称        学年学期")
                for row in course_info:
                    print("  ", row[1], "  ", row[2])
                print("--------------------------")



            elif choice == 2:
                print("-----所有需要提交作业--------")
                # 查询最近需要提交的作业信息
                student_assignments = "SELECT c.course_id, c.course_name, a.assignment_id, a.title, a.end_time  FROM course c " \
                                      "JOIN course_enrollment cs ON c.course_id = cs.course_id " \
                                      "JOIN assignment a ON c.course_id = a.course_id " "WHERE cs.student_id = %s"
                cur.execute(student_assignments, (self.id,))
                assignment_info = cur.fetchall()
                print("课程名称   课程作业编号     作业题目    截止时间")
                for row in assignment_info:
                    print(row[1], "   ", row[2], "    ", row[3], "  ", row[4])
                print("--------------------------")
                # print("-----所有需要提交作业--------")
                # # 查询最近需要提交的作业信息
                # student_assignments = "SELECT c.course_id, c.course_name, a.assignment_id, a.title, a.end_time ,sa.submission_time  FROM course c " \
                #                       "JOIN course_enrollment cs ON c.course_id = cs.course_id " \
                #                       "JOIN assignment a ON c.course_id = a.course_id " \
                #                       "JOIN student_assignment sa ON sa.student_id = %s and sa.assignment_id = a.assignment_id " \
                #                       "WHERE cs.student_id = %s"
                # cur.execute(student_assignments, (self.id, self.id))
                # assignment_info = cur.fetchall()
                # print("课程名称   课程作业编号     作业题目    截止时间   提交时间")
                # for row in assignment_info:
                #     print(row[1], "   ", row[2], "    ", row[3], "  ", row[4], row[5])
                # print("--------------------------")




            elif choice == 3:
                # 查找未提交作业
                print("---------未提交的作业--------")
                student_assignments_sub = "SELECT c.course_id, c.course_name, a.assignment_id, a.title, a.end_time FROM course c " \
                                          "JOIN course_enrollment ce ON c.course_id = ce.course_id " \
                                          "JOIN assignment a ON c.course_id = a.course_id " \
                                          "LEFT JOIN student_assignment sa ON a.assignment_id = sa.assignment_id AND sa.student_id = %s " \
                                          "WHERE ce.student_id = %s AND sa.assignment_id IS NULL"
                cur.execute(student_assignments_sub, (self.id, self.id))
                assignment_info_sub = cur.fetchall()
                if len(assignment_info_sub) > 0:
                    print("课程名   作业编号   作业题目       截止日期")
                    for row in assignment_info_sub:
                        print(row[1], row[2], "   ", row[3], "   ", row[4])
                print("--------------------------")



            elif choice == 4:
                #提交未提交作业
                student_assignments_sub = "SELECT c.course_id, c.course_name, a.assignment_id, a.title, a.end_time FROM course c " \
                                          "JOIN course_enrollment ce ON c.course_id = ce.course_id " \
                                          "JOIN assignment a ON c.course_id = a.course_id " \
                                          "LEFT JOIN student_assignment sa ON a.assignment_id = sa.assignment_id AND sa.student_id = %s " \
                                          "WHERE ce.student_id = %s AND sa.assignment_id IS NULL"

                # student_assignments_sub = "SELECT c.course_id, c.course_name, a.assignment_id, a.title, a.end_time FROM course c " \
                #                           "JOIN course_enrollment ce ON c.course_id = ce.course_id " \
                #                           "JOIN assignment a ON c.course_id = a.course_id " \
                #                           "LEFT JOIN student_assignment sa ON a.assignment_id = sa.assignment_id AND (sa.student_id = %s AND (sa.submission_time IS NULL OR sa.submission_time = '')) " \
                #                           "WHERE ce.student_id = %s AND (sa.assignment_id IS NULL OR sa.submission_time IS NULL OR sa.submission_time = '')"
                cur.execute(student_assignments_sub, (id, id))
                assignment_info_sub = cur.fetchall()
                print("请输入要提交的作业编号：", end='')
                assignment_id = int(input())
                flag = 1
                for i in range(len(assignment_info_sub)):
                    if assignment_info_sub[i][2] == assignment_id:
                        flag = 0
                        print("作业题目：", assignment_info_sub[i][3], "  请输入您的回答：", end='')
                        student_answer = input()
                        submission_time = datetime.now()
                        sql = "INSERT INTO student_assignment (student_id, assignment_id, submission_time, student_answer) VALUES (%s, %s, %s, %s)"
                        cur.execute(sql, (self.id, assignment_id, submission_time, student_answer))
                        print("作业提交成功！")
                if flag:
                    print("请输入正确的作业编号！")
                print("--------------------------")



            elif choice == 5:
                print("-------课程相关材料---------")
                print("课程名           课程相关材料名称      简要内容 ")

                # 查询最近发布的相关课程材料
                material_query = "SELECT cm.material_id, cm.title, cm.visibility, cm.content, c.course_name " \
                                 "FROM course_material cm " \
                                 "JOIN course c ON cm.course_id = c.course_id " \
                                 "JOIN course_enrollment ce ON c.course_id = ce.course_id " \
                                 "WHERE ce.student_id = %s " \
                                 "ORDER BY cm.material_id DESC LIMIT 5"
                cur.execute(material_query, (self.id,))
                material_info = cur.fetchall()
                if not material_info:
                    print("暂无课程材料")
                else:
                    for row in material_info:
                        if row[2] == 'Public':
                            print(row[4], "  ", row[1], "  ", row[3])

            elif choice == 6:
                while True:
                    print("------------------------")
                    print("-----欢迎进入讨论区--------")
                    print("-----可以选择以下功能------")
                    print("-----1、创建帖子----------")
                    print("-----2、回复帖子----------")
                    print("-----3、查看讨论区---------")
                    print("-----0、返回上一级---------")
                    print("------------------------")
                    print("请输入功能选择：", end='')

                    k = int(input())
                    if k == 0:
                        break

                    get_student_courses_query = "SELECT ce.course_id, c.course_name " \
                                                "FROM course_enrollment ce " \
                                                "JOIN course c ON ce.course_id = c.course_id " \
                                                "WHERE ce.student_id = %s"
                    cur.execute(get_student_courses_query, (self.id,))
                    course_name_of_id = cur.fetchall()
                    for course_name in course_name_of_id:
                        print(f"课程号：{course_name[0]}  课程名: {course_name[1]}")


                    print("请输入想进入讨论区的课程号，或输入0返回上一级:", end="")
                    course_id = int(input())
                    if course_id != 0:
                        if k == 1:
                            self.create_forum_post(course_id)
                        elif k == 2:
                            self.create_forum_reply(course_id)
                        elif k == 3:
                            self.show_section_post_replay(course_id)
                        # elif k == 0:
                        #     break
            elif choice == 0:
                break


# 连接MYSQL库
# connection_info = {
#     'host': 'localhost',
#     'user': 'teacher', #three types: student or teacher or root,对应不同的权限
#     'password': '123456',
#     'database': 'WeiMingMuKePingTai',
#     'autocommit': True
# }
connection_info = {
    'host': 'localhost',
    'user': 'root', #three types: student or teacher or root,对应不同的权限
    'password': '123456',
    'database': 'weiming',
    'autocommit': True
}

# 登录身份选额
db = pymysql.connect(**connection_info)
print("请选择登录身份：")
print("1、学生登录")
print("2、教师登录")
print("3、超级管理员登录")
identity = int(input())

# 输入学号/教职工号进行登录
print("请输入学号/教职工号：", end='')
id = int(input())
print("请输入密码：", end='')
password = input()

try:
    cur = db.cursor()
    if identity == 1:
        sql = 'SELECT * FROM student where student_id=%s'
        cur.execute(sql, id)
        # student_info: Tuple[Tuple[Any, ...], ...] = cur.fetchall()
        student_info = cur.fetchall()
        if student_info:
            if student_info[0][5] == password:
                name = student_info[0][1]
                print(list(student_info[0]))
                st = Student(list(student_info[0]), name, id)
                st.show_learning_page(student_info)
            else:
                print("密码错误")
        else:
            print("用户不存在")
    elif identity == 2:
        sql = 'SELECT * FROM teacher where teacher_id=%s'
        cur.execute(sql, id)
        teacher_info = cur.fetchall()
        if teacher_info:
            if teacher_info[0][5] == password:
                while True:
                    tc = Teacher(teacher_info[0][1], teacher_info[0][0])
                    tc.teacher_page(teacher_info)
                    choice = int(input())
                    if choice == 1:
                        flag = tc.get_teacher_courses()
                        while flag:
                            print("----------------------------------")
                            print("---------您可以选择以下操作-----------")
                            print("---------1、创建作业----------------")
                            print("---------2、查看学生信息-------------")
                            print("---------3、查看提交作业-------------")
                            print("---------4、查看课程作业-------------")
                            print("---------5、进入课程讨论区-----------")
                            print("---------6、上传课程材料-----------")
                            print("---------0、返回上一级---------------")
                            n = int(input())
                            if n == 0:
                                break;
                            elif n == 1:
                                tc.create_assignment()
                            elif n == 2:
                                tc.get_students_in_course()
                            elif n == 3:
                                tc.view_and_grade_assignments()
                            elif n == 4:
                                tc.get_all_assignments_with_questions()
                            elif n == 5:
                                tc.forum_section_function_choice()
                            elif n == 6:
                                tc.submit_course_material()


                    elif choice == 2:
                        print("请输入新建课程的名称：", end="")
                        course_name = input()
                        print("请输入新建课程的开课时间：", end='')
                        academic_year_semester = input()
                        trial = 0
                        while trial < 3:
                            print("请输入新建课程的课程号：", end="")
                            course_id = int(input())
                            result = tc.create_course(course_id, course_name, academic_year_semester)
                            if result == 0:
                                break
                            else:
                                print("错误：系统里已存在该课程号，请重新输入")
                            trial += 1
                        if trial == 3:
                            print("课程创建失败，请确认新课程号后再次尝试")
                    elif choice == 3:
                        tc.copy_course()
                    elif choice==4:
                        tc.modify_personal_information()
                    elif choice == 0:
                        break

            else:
                print("密码错误")
        else:
            print("用户不存在")


    elif identity == 3:
        if id == 12138:
            if password == '123456':
                print("超级管理员登录成功")
            else:
                print("密码错误")

except pymysql.Error as e:
    print(e)

finally:
    # 关闭游标和连接
    cur.close()
    db.close()
