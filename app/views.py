import requests
from flask import jsonify, request
from flask.views import MethodView
from models import AdsModel, Session
from errors import ApiError


class AdsView(MethodView):

    def get(self, ad_id: int):
        with Session() as session:
            ad = session.query(AdsModel).get(ad_id)
            if ad is None:
                raise ApiError('404', 'ad is not found')

            return jsonify(
                {
                    "id": ad.id,
                    "user_id": ad.user_id,
                     "title": ad.title,
                     "description": ad.description,
                     "create_date": ad.create_date.isoformat()
                }
            )

    def post(self):
        ad_data = request.json
        with Session() as session:
            new_ad = AdsModel(**ad_data)
            session.add(new_ad)
            session.commit()
            return jsonify(
                    {
                        "id": new_ad.id,
                        "user_id": new_ad.user_id,
                        "title": new_ad.title,
                        "description": new_ad.description,
                        "create_date": new_ad.create_date.isoformat()
                    }
                )
    def patch(self, ad_id):
        ad_data = request.json
        with Session() as session:
            ad = session.query(AdsModel).get(ad_id)
            for field, value in ad_data.items():
                setattr(ad, field, value)
            session.add(ad)
            session.commit()
            return jsonify(
                {
                    "id": ad.id,
                    "user_id": ad.user_id,
                    "title": ad.title,
                    "description": ad.description,
                    "create_date": ad.create_date.isoformat()
                }
            )


    def delete(self, ad_id):
        with Session() as session:
            ad = session.query(AdsModel).get(ad_id)
            session.delete(ad)
            session.commit()
        return jsonify({'DELETE':'OK'})