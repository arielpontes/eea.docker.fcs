import json
from flask import Blueprint, Response
from flask.views import MethodView
from flask.ext.script import Manager
from fcs.models import (
    Undertaking, User, EuLegalRepresentativeCompany, Address, Country,
)

api = Blueprint('api', __name__)

api_manager = Manager()


@api_manager.command
def test():
    """ Return a list of all undertakings """
    import pprint

    undertakings = Undertaking.query.all()

    res = [u.as_dict() for u in undertakings]
    pprint.pprint(res)


class ApiView(MethodView):
    def dispatch_request(self):
        resp = super(ApiView, self).dispatch_request()

        if isinstance(resp, (dict, list, tuple)):
            return Response(json.dumps(resp), mimetype='application/json')

        return resp


class ListView(ApiView):
    def get_queryset(self):
        return self.model.query.all()

    def get(self):
        return [u.as_dict() for u in self.get_queryset()]


class UndertakingList(ListView):
    model = Undertaking

    def get(self):
        undertakings = []
        for undertaking in self.get_queryset():
            u = undertaking.as_dict()
            u['users'] = [cp.as_dict() for cp in undertaking.contact_persons]
            a_id = u.pop('address_id')
            u['address'] = Address.query.get(a_id).as_dict()
            c_id = u['address'].pop('country_id')
            u['address']['country'] = Country.query.get(c_id).as_dict()
            undertakings.append(u)
        return undertakings


class UserList(ListView):
    model = User


class CompaniesList(ListView):
    model = EuLegalRepresentativeCompany


api.add_url_rule('/undertaking/list',
                 view_func=UndertakingList.as_view('undertaking-list'))
api.add_url_rule('/user/list',
                 view_func=UserList.as_view('user-list'))
api.add_url_rule('/company/list',
                 view_func=CompaniesList.as_view('companies-list'))
# api.add_url_rule('company_for_user/<username>')