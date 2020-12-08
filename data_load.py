from datetime import datetime
from app import app, db
from app.models import User, Post, Course, Lecture, Sub, Question, Assignment, Discussion, Lab, QuizQuestion
import json, os

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Course': Course, "Lecture": Lecture,
            "Sub": Sub, "Question": Question, "Assignment": Assignment,
            "Discussion": Discussion, "Lab": Lab}



def loadJson(filename):
    # read JSON file which is in the next parent folder
    file = os.path.abspath('/Users/ryanhurst/uniEd/') + filename
    json_data=open(file).read()
    json_obj = json.loads(json_data)
    return json_obj

def loadLectureData():
    jsonData = loadJson('/lecturedata.json')
    for i, item in enumerate(jsonData):
        lecture_topic = item.get("lecture_topic", None)
        course_num = item.get("course_num", None)
        lecture_date = item.get("lecture_date", None)
        lecture_week = item.get("lecture_week", None)
        lecture_film = item.get("lecture_film", None)
        lecture = Lecture(lecture_topic=lecture_topic, course_num=course_num, lecture_date=lecture_date,
                                lecture_week=lecture_week, lecture_film=lecture_film)
        try:
            # db.session.add(lecture)
            # db.session.commit()
            print(lecture)
        except:
            print('Insert failed')

def main():
    return loadLectureData()
if __name__ == '__main__':
    main()
