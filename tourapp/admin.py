from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import request
from tourapp import app, db, utils
from tourapp.models import Product, Category,UserRole, Bill

admin = Admin(app=app, name="VIETNAM BOOKING", template_mode='bootstrap4')


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated \
               and current_user.user_role.__eq__(UserRole.ADMIN)


class ProductView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['name', 'time']
    column_filters = ['name', 'price_big', 'price_small']

class BillView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['name', 'cccd', 'phone']
    column_filters = ['total', 'pay_date']


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

class StatsView(BaseView):
    @expose('/')
    def index(self):
        stats = utils.stats_revenue(month=request.args.get('month'))
        total = utils.total_revenue(month=request.args.get('month'))[0]
        return self.render('admin/stats.html',stats=stats,total=total)

class TourView(BaseView):
    @expose('/')
    def index(self):
        stats = utils.count_tour_by_cate(month=request.args.get('month'))
        return self.render('admin/tour.html', stats=stats)

admin.add_view(AuthenticatedModelView(Category, db.session,name='Vùng miền'))
admin.add_view(ProductView(Product, db.session,name='Tour du lịch'))
admin.add_view(BillView(Bill, db.session, name='Hóa đơn'))
admin.add_view(StatsView(name='Thống kê doanh thu'))
admin.add_view(TourView(name='Thống kê Tour'))
admin.add_view(LogoutView(name='Logout'))

