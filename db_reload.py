
# after running:
    # rm -rf app.db
    # rm -rf migrations/
    # flask db init
    # flask db migrate
    # flask db upgrade
    # then run python3 db_reload.py

from datetime import datetime
from app import app, db
from app.models import User, Post, Course, Lecture, Sub, Question, Assignment, Discussion, Lab, QuizQuestion


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Course': Course, "Lecture": Lecture,
            "Sub": Sub, "Question": Question, "Assignment": Assignment,
            "Discussion": Discussion, "Lab": Lab}

if Course:
    CS61b = Course(instructor="Josh Hug", course_name="CS61B")
    db.session.add(CS61b)
    db.session.commit()

    lecture_list = [Lecture(lecture_topic="Pre: An Outline of 61B", course_num=1, lecture_date=datetime(2020, 1, 20),
                            lecture_week=1, lecture_film=0),
                    Lecture(lecture_topic="Intro, Hello World Java", course_num=1, lecture_date=datetime(2020, 1, 22),
                            lecture_week=1, lecture_film=0),
                    Lecture(lecture_topic="Defining & Using Classes", course_num=1, lecture_date=datetime(2020, 1, 24),
                            lecture_week=1, lecture_film=0),
                    Lecture(lecture_topic="References, Recursion, and Lists", course_num=1,
                            lecture_date=datetime(2020, 1, 27), lecture_week=2, lecture_film=0),
                    Lecture(lecture_topic="SLLists, Nested Classes, Sential nodes", course_num=1,
                            lecture_date=datetime(2020, 1, 29), lecture_week=2, lecture_film=0),
                    Lecture(lecture_topic="DLLists, Arrays", course_num=1, lecture_date=datetime(2020, 1, 31),
                            lecture_week=2, lecture_film=0),
                    Lecture(lecture_topic="ALists, Resizing, vs. SLists", course_num=1,
                            lecture_date=datetime(2020, 2, 3), lecture_week=3, lecture_film=0),
                    Lecture(lecture_topic="Testing", course_num=1, lecture_date=datetime(2020, 2, 5), lecture_week=3,
                            lecture_film=0),
                    Lecture(lecture_topic="Inheritance, Implements", course_num=1, lecture_date=datetime(2020, 2, 7),
                            lecture_week=3, lecture_film=0)]
    for lecture in lecture_list:
        db.session.add(lecture)
    db.session.commit()



    assignments1 = [
        Assignment(assignment_week=1, assignment_name="HW 0: Basic Java Programs(optional)", exam_name=None),
        Assignment(assignment_week=2, assignment_name="Project 0: NBody (due 2/1 @ 11:59PM)", exam_name=None),
        Assignment(assignment_week=3, assignment_name="Project 1A: Data Structures (due 2/9 @ 11:59PM)",
                   exam_name=None)]
    for assignment in assignments1:
        db.session.add(assignment)
    db.session.commit()

    discussions1 = [Discussion(discussion_week=1, discussion_name="Intro to Java"),
                    Discussion(discussion_week=2, discussion_name="Scope, Pass-by-Value, Static"),
                    Discussion(discussion_week=2, discussion_name="Scope, Pass-by-Value, Static Exam Prep"),
                    Discussion(discussion_week=3, discussion_name="Linked Lists, Arrays"),
                    Discussion(discussion_week=3, discussion_name="Linked Lists, Arrays Exam Prep")]
    for discussion in discussions1:
        db.session.add(discussion)
    db.session.commit()



    labs1 = [Lab(lab_week=1, lab_name="Setting Up Your Computer"),
             Lab(lab_week=1, lab_name="javac, java, git (due 2/1)"),
             Lab(lab_week=2, lab_name="IntelliJ Home Setup"),
             Lab(lab_week=2, lab_name="IDEs (due 2/1)"),
             Lab(lab_week=3, lab_name="Testing, Debugging (due 2/8)")]
    for lab in labs1:
        db.session.add(lab)
    db.session.commit()

    subtopics = [Sub(subtopic="(1a) Beach Party: 800 corgis", lecture_num=1, lecture_video="embed/RAbHpkPl1Ww",
                     order_in_lecture=1),
                 Sub(subtopic="(1a) Corgi Videos Pt 2", lecture_num=1, lecture_video="embed/O-xAi7dIdV8",
                     order_in_lecture=2),
                 Sub(subtopic="(1a) Welcome to 61B", lecture_num=2, lecture_video="embed/h59h5DoNhL4",
                     order_in_lecture=1),
                 Sub(subtopic="(1b) Course Logistics", lecture_num=2, lecture_video="embed/uaA1hLH3LjY",
                     order_in_lecture=2),
                 Sub(subtopic="(1) Compilation", lecture_num=3, lecture_video="embed/Y2vC_SW00TE", order_in_lecture=1),
                 Sub(subtopic="(2a) Defining & Instantiating Classes", lecture_num=3, lecture_video="embed/xDPUHRjsgA4",
                     order_in_lecture=2),
                 Sub(subtopic="(2b) Defining & Instantiating Classes", lecture_num=3, lecture_video="embed/Hsor-iZ6-a4",
                     order_in_lecture=3),
                 Sub(subtopic="(2c) Terminology", lecture_num=3, lecture_video="embed/ewMzZBy1RO4", order_in_lecture=4),
                 Sub(subtopic="(2d) Arrays Of Objects", lecture_num=3, lecture_video="embed/GgoszMH1ak8",
                     order_in_lecture=5),
                 Sub(subtopic="(3a) Static vs Instance Methods", lecture_num=3, lecture_video="embed/l8Q6NXbAwNk",
                     order_in_lecture=6),
                 Sub(subtopic="(3b) Exercise", lecture_num=3, lecture_video="embed/8Gq-8mVbyFU", order_in_lecture=7),
                 Sub(subtopic="(3c) Exercise Solution", lecture_num=3, lecture_video="embed/Osuy8UEH03M",
                     order_in_lecture=8),
                 Sub(subtopic="(4) Public Static Void Main", lecture_num=3, lecture_video="embed/1ViQUHlRoyM",
                     order_in_lecture=9),
                 Sub(subtopic="(5) Using Libraries", lecture_num=3, lecture_video="embed/C6kbrsdNQaQ",
                     order_in_lecture=10)]
    for sub in subtopics:
        db.session.add(sub)
    db.session.commit()


    quiz_questions = [
        QuizQuestion(sub_id = 6, question = "What are the two commands to (1) compile a java file & (2) run the compiled file?",
                     choice1 = "(1) javac FileName.java (2) java FileName",
                     choice2="(1) java FileName (2) javac FileName.java",
                     choice3="(1) java FileName.java (2) javac FileName",
                     choice4="Pound your fists on the keyboard & hope for the best",
                     correct = 1
                     ),
        QuizQuestion(sub_id=7,
                     question="How would you define a 'Dog' class in java?",
                     choice1="public static Main Dog",
                     choice2="public void Dog",
                     choice3="public class dog",
                     choice4="Buy a dog whistle and use it in a dog park",
                     correct=3
                     ),
        QuizQuestion(sub_id=8,
                     question="Where do you declare Instance variables in a class?",
                     choice1="Below the class deceleration",
                     choice2="Below the main method",
                     choice3="In the constructor",
                     choice4="Outside of the class decleration",
                     correct=1
                     ),
        QuizQuestion(sub_id=9,
                     question="What does the constructor do?",
                     choice1="Defines the actions of a class",
                     choice2="Provides another method for the class",
                     choice3="Serves to be be invoked by an instance of the class",
                     choice4="Determines how to instanciate the class",
                     correct=4
                     ),
        QuizQuestion(sub_id=10,
                     question="Where do you declare variables in a class?",
                     choice1="Below the class deceleration",
                     choice2="Below the main method",
                     choice3="In the constructor",
                     choice4="Outside of the class decleration",
                     correct=1
                     ),
        QuizQuestion(sub_id=11,
                     question="Where do you declare variables in a class?",
                     choice1="Below the class deceleration",
                     choice2="Below the main method",
                     choice3="In the constructor",
                     choice4="Outside of the class decleration",
                     correct=1
                     ),
        QuizQuestion(sub_id=12,
                     question="Where do you declare variables in a class?",
                     choice1="Below the class deceleration",
                     choice2="Below the main method",
                     choice3="In the constructor",
                     choice4="Outside of the class decleration",
                     correct=1
                     ),
        QuizQuestion(sub_id=13,
                     question="Where do you declare variables in a class?",
                     choice1="Below the class deceleration",
                     choice2="Below the main method",
                     choice3="In the constructor",
                     choice4="Outside of the class decleration",
                     correct=1
                     ),
        QuizQuestion(sub_id=14,
                     question="Where do you declare variables in a class?",
                     choice1="Below the class deceleration",
                     choice2="Below the main method",
                     choice3="In the constructor",
                     choice4="Outside of the class deceleration",
                     correct= 1
                     )
    ]


    for question in quiz_questions:
        db.session.add(question)
    db.session.commit()











