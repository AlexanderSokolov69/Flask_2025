from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = IntegerField('ID руководителя', validators=[DataRequired()])
    job = TextAreaField("Содержание задачи", validators=[DataRequired()])
    work_size = IntegerField("Объём в часах", validators=[DataRequired()])
    collaborators = StringField('ID исполнителей через запятую')
    start_date = DateField('Начало работ')
    end_date = DateField('Окончание работ')
    is_finished = BooleanField('Задача завершена')
    submit = SubmitField('Создать')

