import pymysql

from util.dbUtil import get_conn


class Course:
    def __init__(self, id_, name_, teacher_id_):
        self.id = id_
        self.name = name_
        self.teacher_id = teacher_id_

    def get_students_in_course(self):
        conn = get_conn()
        cur = conn.cursor()
        query = "SELECT s.student_id, s.name " \
                "FROM student s " \
                "JOIN course_enrollment cr ON s.student_id = cr.student_id " \
                "WHERE cr.course_id = %s"
        cur.execute(query, self.id)
        course_student = cur.fetchall()
        conn.close()
        return course_student

    def get_assignments_in_course(self, assignment_id):
        conn = get_conn()
        cur = conn.cursor()
        view_assignments_query = "SELECT sa.student_assignment_id, sa.student_id, sa.assignment_id, " \
                                 "a.title AS assignment_title, sa.submission_time, sa.grade, sa.comment, " \
                                 "sa.student_answer " \
                                 "FROM student_assignment sa " \
                                 "JOIN assignment a ON sa.assignment_id = a.assignment_id " \
                                 "WHERE a.course_id = %s AND sa.assignment_id=%s"
        cur.execute(view_assignments_query, (self.id, assignment_id))
        assignments = cur.fetchall()
        conn.close()
        return assignments

    def get_hw_in_course(self):
        conn = get_conn()
        cur = conn.cursor()
        try:
            get_all_assignments_query = "SELECT * FROM assignment WHERE course_id=%s"
            cur.execute(get_all_assignments_query, self.id)
            assignments = cur.fetchall()
            assignments_with_questions = []
            for assignment in assignments:
                assignment_id = assignment[0]
                get_questions_for_assignment_query = "SELECT question_text FROM assignment_question " \
                                                     "WHERE assignment_id = %s"
                cur.execute(get_questions_for_assignment_query, (assignment_id,))
                questions = cur.fetchall()
                assignment_with_question = (assignment_id, assignment[2], questions,)
                assignments_with_questions.append(assignment_with_question)
            return assignments_with_questions
        except pymysql.Error as e:
            print(e)

    # 返回section_id 和section_name
    def get_sections(self):
        # print(course_id)
        # print("SELECT course_name FROM course WHERE course_id = %s"%(course_id,))
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM forum_section WHERE forum_section.course_id = {self.id}")
        sections = cur.fetchall()
        conn.close()
        return sections
