from app.models import engine, Base, Session, AdsModel
from pytest import fixture


@fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()


@fixture()
def create_ad():
    with Session() as session:
        new_ad = AdsModel(user_id= 10, title='112233')
        session.add(new_ad)
        session.commit()
        return {
            'id': new_ad.id,
            'title': new_ad.title
        }
