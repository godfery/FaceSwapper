# coding:utf-8
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField,IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError
# from models.models import User
# from route.func import get_category


"""
登录表单：
1.账号
2.密码
3.登录按钮
"""


class ImageForm(FlaskForm):
    photo = FileField(
        
    )
    photo1 = FileField(
        
    )
    submit = SubmitField(
        u'转换',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

class LoginForm(FlaskForm):
    name = StringField(
        label=u"账号",
        validators=[
            DataRequired(u'账号不能为空')
        ],
        description=u"账号",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号'
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u'密码不能为空')
        ],
        description=u'密码',
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入密码'
        }
    )
    submit = SubmitField(
        u'登录',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

    def validate_pwd(self, field):
        # pwd = field.data
        # user = User.query.filter_by(name=self.name.data).first()
        # if user is not None and not user.check_pwd(pwd):
        #     raise ValidationError(u'密码错误')
        pass
    def validate_name(self, field):
        # name = field.data
        # user = User.query.filter_by(name=name).first()
        # if not user:
        #     raise ValidationError(u'不存在的用户名')
        pass
