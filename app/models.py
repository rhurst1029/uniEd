from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    instructor = db.Column(db.Boolean)
    current_date = datetime(2020, 1, 25, 0, 0)
    question_posts = db.relationship("Question", backref="author", lazy="dynamic")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    instructor = db.Column(db.String(36))
    course_name = db.Column(db.String(36))
    lectures = db.relationship('Lecture', backref='topic', lazy='dynamic')

    def __repr__(self):
        return '<Course {}>'.format(self.course_name)

    def avatar(self, size):
        digest = md5(self.course_name.encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Lecture(db.Model):
    # course_name represents the course for each lecture:
    # "course.course_name" is course_name instance variable from Course Class
    lecture_id = db.Column(db.Integer, primary_key=True)
    lecture_topic = db.Column(db.String(36))
    course_num = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    lecture_date = db.Column(db.DateTime)
    lecture_week = db.Column(db.Integer())
    subtopics = db.relationship('Sub', backref='lecture', lazy='dynamic')
    lecture_film = db.Column(db.Integer())

    def __repr__(self):
        return '<Lecture {}>'.format(self.lecture_topic)


class Sub(db.Model):
    # SubTopic class serves to provide subtopics for pulldown bar in lecture page
    # Pulldown bar is provided by _subtopicPulldown.html

    id = db.Column(db.Integer, primary_key=True)
    subtopic = db.Column(db.String(42))
    lecture_num = db.Column(db.Integer, db.ForeignKey("lecture.lecture_id"))
    questions = db.relationship("Question", backref="topicsub", lazy="dynamic")
    quiz_questions = db.relationship("QuizQuestion", backref = "questionsub", lazy = "dynamic")
    lecture_video = db.Column(db.String(86))
    order_in_lecture = db.Column(db.Integer())

    def __repr__(self):
        return '<Sub {}>'.format(self.subtopic)


class Assignment(db.Model):
    # Contains Weekly: Assignments/exams
    assignment_id = db.Column(db.Integer, primary_key=True)
    assignment_week = db.Column(db.Integer, db.ForeignKey("lecture.lecture_week"))
    assignment_name = db.Column(db.String(42))
    exam_name = db.Column(db.String(42))

    def __repr__(self):
        return '<Assignment {}>'.format(self.assignment_name)


class Discussion(db.Model):
    # Contains: Weekly Discussions
    discussion_id = db.Column(db.Integer, primary_key=True)
    discussion_week = db.Column(db.Integer, db.ForeignKey("lecture.lecture_week"))
    discussion_name = db.Column(db.String(64))

    def __repr__(self):
        return '<Discussion {}>'.format(self.discussion_name)


class Lab(db.Model):
    lab_id = db.Column(db.Integer, primary_key=True)
    lab_week = db.Column(db.Integer, db.ForeignKey("lecture.lecture_week"))
    lab_name = db.Column(db.String(64))

    def __repr__(self):
        return '<Lab {}>'.format(self.lab_name)


class Question(db.Model):
    # Question class serves to save questions posted on the lecture page
    question_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subtopic_id = db.Column(db.Integer, db.ForeignKey('sub.id'))
    question = db.Column(db.String(180))
    question_score = db.Column(db.Integer)

    def __repr__(self):
        return '<Question {}>'.format(self.question)


class QuizQuestion(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sub_id = db.Column(db.Integer, db.ForeignKey("sub.id"))

    question = db.Column(db.String(128), unique=False, nullable=False)
    choice1 = db.Column(db.String(128), unique=False, nullable=False)
    choice2 = db.Column(db.String(128), unique=False, nullable=False)
    choice3 = db.Column(db.String(128), unique=False, nullable=False)
    choice4 = db.Column(db.String(128), unique=False, nullable=False)
    correct = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "< Question - id: {} sub_id: {}  question: {}  {} {} {} {} {} >".format(
            self.id,
            self.sub_id,
            self.question,
            self.choice1,
            self.choice2,
            self.choice3,
            self.choice4,
            self.correct
        )


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
