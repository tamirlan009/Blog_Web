from flask import redirect, url_for, request
from app import app
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from models import *

from flask_security import current_user


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self,name,  **kwargs):
        return redirect(url_for('security.login', next = request.url))

class BaseModelChange(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelChange, self).on_model_change(form, model, is_created)


class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class PostModelView(AdminMixin, BaseModelChange):
    form_columns = ['title', 'body']



admin = Admin(app, 'FlaskApp', url = '/', index_view = HomeAdminView(name = 'Home'))
admin.add_view(PostModelView(Post, db.session))
