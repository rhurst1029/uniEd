from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, QuestionForm, NextSubtopic, QuizForm, FinishQuiz
from app.models import User, Course, Lecture, Sub, Question, Discussion, Lab


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    courses = Course.query.all()
    instCourse = Course.query.first()
    lectures = Lecture.query.all()

    lecMap = []
    lastLec = None
    for lecture in lectures:
        if lecture.lecture_date <= current_user.current_date:
            lecMap.append(lecture)
        else:
            lastLec = lecMap[len(lecMap) - 1]

    lectures = Lecture.query.filter_by(lecture_week=lastLec.lecture_week).all()
    labs = Lab.query.filter_by(lab_week = lastLec.lecture_week).all()
    discussions = Discussion.query.filter_by(discussion_week = lastLec.lecture_week).all()

    return render_template('index.html', title='Home', courses=courses,
                           instCourse=instCourse, lectures=lectures, lastLec=lastLec, labs = labs, discussions = discussions)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/student_register', methods=['GET', 'POST'])
def student_register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, instructor=False)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered Student!')
        return redirect(url_for('login'))
    return render_template('student_register.html', title='Register', form=form)


@app.route('/instructor_register', methods=['GET', 'POST'])
def instructor_register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, instructor=True)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('instructor_register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('user.html', user=user)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/course_calendar/<course_id>', methods=['GET'])
@login_required
def course_calendar(course_id):
    course = Course.query.filter_by(course_id=course_id).first_or_404()
    lectures = Lecture.query.filter_by(course_num=course.course_id).order_by(Lecture.lecture_id).all()
    discussions = Discussion.query.all()
    labs = Lab.query.all()
    disc_arr = []
    lab_arr = []
    for week in range(15):
        lab_arr2 = []
        for lab in labs:
            if lab.lab_week == week:
                lab_arr2.append(lab)
        lab_arr.append(lab_arr2)

    for week in range(15):
        disc_arr2 = []
        for disc in discussions:
            if disc.discussion_week == week:
                disc_arr2.append(disc)
        disc_arr.append(disc_arr2)

    subMap = {}
    for lecture in lectures:
        if len(lecture.subtopics.all()) < 1:
            subMap[lecture] = None
        else:
            subMap[lecture] = min(lecture.subtopics.all(), key=lambda x: x.order_in_lecture)
    return render_template('course_calendar.html', title="Course Page", course=course, lectures=subMap,
                           discussions=discussions,
                           labs=labs, lab_arr=lab_arr, disc_arr=disc_arr)


@app.route("/lecture_page/<course_id>/<lecture_id>/<subtopic_id>", methods=["GET", "POST"])
def lecture_page( course_id, lecture_id, subtopic_id):
    lectures = Lecture.query.filter_by(lecture_id=lecture_id).first_or_404()
    subs = Sub.query.filter_by(id=subtopic_id).first_or_404()
    questions = Question.query.filter_by(subtopic_id=subs.id)

    ## QuestionForm is for uploading a student's question without refreshing webpage ###
    form = QuestionForm()
    if form.validate_on_submit():

        question = Question(user_id=current_user.id,
                            question=form.question.data,
                            subtopic_id=subtopic_id)

        db.session.add(question)
        print("Question added to database")
        db.session.commit()
        # return redirect(url_for('lecture_page', course_id=course_id, lecture_id=lecture_id, subtopic_id = subtopic_id))
        return

    form2 = NextSubtopic()
    if form2.validate_on_submit():

        subtopic_id2 = subtopic_id +1

        return redirect(url_for('quiz_page', course_id=1,
                                lecture_id=lecture_id, subtopic_id = subtopic_id2))

    return render_template('lecture_page.html', lecture=lectures, subtopics=lectures.subtopics,
                           form=form, subtopic_id=subtopic_id, sub=subs, questions=questions, form2 = form2)


@app.route("/quiz_page/<course_id>/<lecture_id>/<subtopic_id>", methods=["GET", "POST"])
def quiz_page( course_id, lecture_id, subtopic_id):
    lectures = Lecture.query.filter_by(lecture_id=lecture_id).first_or_404()
    subs = Sub.query.filter_by(id=subtopic_id).first_or_404()
    questions = Question.query.filter_by(subtopic_id=subs.id)

    form2 = FinishQuiz()
    if form2.validate_on_submit():

        subtopic_id2 = subtopic_id +1

        return redirect(url_for('lecture_page', course_id=1,
                                lecture_id=lecture_id, subtopic_id = subtopic_id2))
    form3 = QuizForm()
    if form2.validate_on_submit():
        subtopic_id2 = subtopic_id + 1

        return redirect(url_for('lecture_page', course_id=1,
                                lecture_id=lecture_id, subtopic_id=subtopic_id2))

    return render_template('quiz_page.html', lecture=lectures, subtopics=lectures.subtopics,
                           subtopic_id=subtopic_id, sub=subs, questions=questions, form2 = form2, form3 = form3)



@app.route("/pre_lecture_page/<course_id>/<lecture_id>", methods=["GET"])
def pre_lecture_page(course_id, lecture_id):
    lecture = Lecture.query.filter_by(lecture_id=lecture_id).first_or_404()
    return render_template('pre_lecture_page.html', lecture=lecture, subtopics=lecture.subtopics)


@app.route("/post_lecture_page/<course_id>/<lecture_id>", methods=["GET"])
def post_lecture_page(course_id, lecture_id):
    lecture = Lecture.query.filter_by(lecture_id=lecture_id).first_or_404()
    return render_template('post_lecture_page.html', lecture=lecture, subtopics=lecture.subtopics)


@app.route('/')
def refresh_question():
    name = request.args.get('name', 'Anonymous')
    if request.is_xhr:
        template_name = 'template_ajax.html'
    else:
        template_name = 'template.html'
    return render_template(template_name, name=name)


@app.route('/course_info/<course_id>', methods=['GET'])
def course_info(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    return render_template('course_info_page.html', course=course)


@app.route('/course_recourses/<course_id>', methods=['GET'])
def course_recourses(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    return render_template('course_recourse_page.html', course=course)


@app.route('/staff_page/<course_id>', methods=['GET'])
def staff_page(course_id):
    course = Course.query.filter_by(course_id=course_id).first_or_404()
    return render_template('staff_page.html', course=course)


@app.route('/addQuestion', methods=['POST'])
@login_required
def addQuestion():
    question = Question(user_id=request.form['user'], question=request.form['question'],
                        subtopic_id=request.form['sub'])
    db.session.add(question)
    db.session.commit()
    return jsonify({'question': request.form['question']})


@app.route('/upVote', methods = ['POST'])
def upVote():
    print("almost routed")
    print(request.form['question'])
    # Assume that request.form will have a key question_id
    question = Question.query.filter_by(question_id = request.form['question']).first_or_404()
    if question.question_score == None:
        question.question_score = 1
    else:
        question.question_score +=1
    db.session.add(question)
    db.session.commit()
    print("routed")
    return jsonify({"score": question.question_score})

