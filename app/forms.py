from .models import User
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, Length, DataRequired, EqualTo, ValidationError


class RegisterForm(FlaskForm):
    email = EmailField(
        'Elektron pochta',
        validators=[
            DataRequired(message='Elektron pochta kiritish majburiy.'),
            Email(message='To‘g‘ri elektron pochta manzilini kiriting!')
        ],
        render_kw={"placeholder": "foydalanuvchi@example.com"},
        description='Amaldagi elektron pochtangizni kiriting. U ro‘yxatdan o‘tishda va tizimga kirishda ishlatiladi.'
    )
    password = PasswordField(
        'Parol',
        validators=[
            DataRequired(message='Parol kiritish majburiy.'),
            Length(min=8, message='Parol kamida 8 ta belgidan iborat bo‘lishi kerak.')
        ],
        render_kw={"placeholder": "Yangi parol kiriting"},
        description='Parol kamida 8 ta belgidan iborat bo‘lishi kerak. Uni hech kim bilan bo‘lishmang.'
    )
    confirm_password = PasswordField(
        'Parolni tasdiqlang',
        validators=[
            DataRequired(message='Parolni tasdiqlash majburiy.'),
            EqualTo('password', message='Parollar mos kelmadi.')
        ],
        render_kw={"placeholder": "Parolni qayta kiriting"},
        description='Yuqorida kiritgan parolingizni qaytadan kiriting.'
    )
    submit = SubmitField('Ro‘yxatdan o‘tish')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Bu elektron pochta manzili allaqachon ro‘yxatdan o‘tgan.')


class LoginForm(FlaskForm):
    email = EmailField(
        'Elektron pochta',
        validators=[
            DataRequired(message='Elektron pochta kiritish majburiy.'),
            Email(message='To‘g‘ri elektron pochta manzilini kiriting!')
        ],
        render_kw={"placeholder": "foydalanuvchi@example.com"},
        description='Tizimga kirish uchun ro‘yxatdan o‘tgan elektron pochtangizni kiriting.'
    )
    password = PasswordField(
        'Parol',
        validators=[
            DataRequired(message='Parol kiritish majburiy.'),
            Length(min=8, message='Parol kamida 8 ta belgidan iborat bo‘lishi kerak.')
        ],
        render_kw={"placeholder": "Parolingizni kiriting"},
        description='Ro‘yxatdan o‘tishda belgilagan parolingizni kiriting.'
    )
    remember = BooleanField('Eslab qolish')
    submit = SubmitField('Kirish')
