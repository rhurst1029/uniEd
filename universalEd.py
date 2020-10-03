from app import app, db
from app.models import User, Post, Course, Lecture, \
    Sub, Question, Assignment, Discussion, Lab, QuizQuestion


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Course': Course, "Lecture": Lecture,
            "Sub": Sub, "Question": Question, "Assignment": Assignment,
            "Discussion": Discussion, "Lab": Lab, "QuizQuestion": QuizQuestion}
