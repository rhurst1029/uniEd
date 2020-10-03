"""empty message

Revision ID: 242b89747b8f
Revises: 
Create Date: 2020-06-27 17:58:21.182441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '242b89747b8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('instructor', sa.String(length=36), nullable=True),
    sa.Column('course_name', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('instructor', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('lecture',
    sa.Column('lecture_id', sa.Integer(), nullable=False),
    sa.Column('lecture_topic', sa.String(length=36), nullable=True),
    sa.Column('course_num', sa.Integer(), nullable=True),
    sa.Column('lecture_date', sa.DateTime(), nullable=True),
    sa.Column('lecture_week', sa.Integer(), nullable=True),
    sa.Column('lecture_film', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_num'], ['course.course_id'], ),
    sa.PrimaryKeyConstraint('lecture_id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('assignment',
    sa.Column('assignment_id', sa.Integer(), nullable=False),
    sa.Column('assignment_week', sa.Integer(), nullable=True),
    sa.Column('assignment_name', sa.String(length=42), nullable=True),
    sa.Column('exam_name', sa.String(length=42), nullable=True),
    sa.ForeignKeyConstraint(['assignment_week'], ['lecture.lecture_week'], ),
    sa.PrimaryKeyConstraint('assignment_id')
    )
    op.create_table('discussion',
    sa.Column('discussion_id', sa.Integer(), nullable=False),
    sa.Column('discussion_week', sa.Integer(), nullable=True),
    sa.Column('discussion_name', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['discussion_week'], ['lecture.lecture_week'], ),
    sa.PrimaryKeyConstraint('discussion_id')
    )
    op.create_table('lab',
    sa.Column('lab_id', sa.Integer(), nullable=False),
    sa.Column('lab_week', sa.Integer(), nullable=True),
    sa.Column('lab_name', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['lab_week'], ['lecture.lecture_week'], ),
    sa.PrimaryKeyConstraint('lab_id')
    )
    op.create_table('sub',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subtopic', sa.String(length=42), nullable=True),
    sa.Column('lecture_num', sa.Integer(), nullable=True),
    sa.Column('lecture_video', sa.String(length=86), nullable=True),
    sa.Column('order_in_lecture', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lecture_num'], ['lecture.lecture_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('subtopic_id', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(length=180), nullable=True),
    sa.Column('question_score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subtopic_id'], ['sub.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('question_id')
    )
    op.create_table('quiz_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sub_id', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(length=128), nullable=False),
    sa.Column('choice1', sa.String(length=128), nullable=False),
    sa.Column('choice2', sa.String(length=128), nullable=False),
    sa.Column('choice3', sa.String(length=128), nullable=False),
    sa.Column('choice4', sa.String(length=128), nullable=False),
    sa.Column('correct', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sub_id'], ['sub.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz_question')
    op.drop_table('question')
    op.drop_table('sub')
    op.drop_table('lab')
    op.drop_table('discussion')
    op.drop_table('assignment')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('lecture')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('course')
    # ### end Alembic commands ###