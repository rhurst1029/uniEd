from datetime import datetime




from app import app, db
from app.models import User, Post, Course, Lecture, Sub, Question, Assignment, Discussion, Lab, QuizQuestion
import time
import uuid
from datetime import datetime
from decimal import Decimal

from dynamodb_json import json_util as json

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Course': Course, "Lecture": Lecture,
            "Sub": Sub, "Question": Question, "Assignment": Assignment,
            "Discussion": Discussion, "Lab": Lab}

lectures = db.session.query(Lecture.lecture_id, Lecture.lecture_topic, Lecture.lecture_date,
                 Lecture.lecture_week, Lecture.subtopics,
                 Lecture.lecture_film).order_by(Lecture.lecture_id).all()

out = open("lecturedata.json", 'w', encoding='utf-8')

out.writelines(json.dumps([ row._asdict() for row in lectures ]))

subtopics = db.session.query(Sub.id, Sub.subtopic, Sub.lecture_num, Sub.questions, Sub.quiz_questions, Sub.lecture_video).order_by(Sub.id).all()
out2 = open("subtopicdata.json", 'w', encoding='utf-8')

out2.writelines(json.dumps([ row._asdict() for row in  subtopics]))


labs = db.session.query(Lab.lab_id, Lab.lab_week, Lab.lab_name).order_by(Lab.lab_id).all()
out3 = open("labdata.json", 'w', encoding='utf-8')

out3.writelines(json.dumps([ row._asdict() for row in  labs]))

discussions = db.session.query(Discussion.discussion_id,Discussion.discussion_name, Discussion.discussion_week).order_by(Discussion.discussion_id).all()
out4 = open("discussiondata.json", 'w', encoding='utf-8')

out4.writelines(json.dumps([ row._asdict() for row in  discussions]))

quizQuestions = db.session.query(QuizQuestion.id, QuizQuestion.sub_id,
                                 QuizQuestion.question, QuizQuestion.choice1,
                                 QuizQuestion.choice2, QuizQuestion.choice3, QuizQuestion.choice4).order_by(QuizQuestion.id).all()
out5 = open("quizQuestiondata.json", 'w', encoding='utf-8')

out5.writelines(json.dumps([ row._asdict() for row in  quizQuestions]))

