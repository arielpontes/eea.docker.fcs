from datetime import date

from factory.alchemy import SQLAlchemyModelFactory
from factory import SubFactory, post_generation

from fcs import models


class CountryFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Country
        sqlalchemy_session = models.db.session

    code = 'c'
    name = 'n'
    type = 't'


class AddressFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Address
        sqlalchemy_session = models.db.session

    country = SubFactory(CountryFactory)

    street = 's'
    number = 'n'
    city = 'c'
    zipcode = 'z'


class RepresentativeFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.EuLegalRepresentativeCompany
        sqlalchemy_session = models.db.session

    name = 'n'
    vatnumber = 'vat'
    contact_first_name = 'first'
    contact_last_name = 'last'
    contact_email = 'email'
    address = SubFactory(AddressFactory)


class BusinessProfileFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.BusinessProfile
        sqlalchemy_session = models.db.session


class UndertakingFactory(SQLAlchemyModelFactory):

    class Meta:
        model = models.Undertaking
        sqlalchemy_session = models.db.session

    id = 1
    external_id = 10
    name = 'n'
    website = 'w'
    phone = 'p'
    domain = 'd'
    status = 's'
    date_created = date(2015, 1, 1)
    date_updated = date(2015, 1, 1)
    undertaking_type = 'FGASUndertaking'
    vat = 'v'
    types = 't'
    oldcompany_verified = True
    oldcompany_account = 'oldcompany_account'
    oldcompany_extid = 100
    address = SubFactory(AddressFactory)
    represent = SubFactory(RepresentativeFactory)
    businessprofile = SubFactory(BusinessProfileFactory)

    @post_generation
    def contact_persons(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for cp in extracted:
                self.contact_persons.add(cp)


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.User
        sqlalchemy_session = models.db.session

    username = 'username'
    first_name = 'first'
    last_name = 'last'
    email = 'email@example.com'


class MatchingLog(SQLAlchemyModelFactory):
    class Meta:
        model = models.MatchingLog
        sqlalchemy_session = models.db.session


class MailAddress(SQLAlchemyModelFactory):
    class Meta:
        model = models.MailAddress
        sqlalchemy_session = models.db.session

    mail = 'test@test.com'
    first_name = 'first_name'
    last_name = 'last_name'
