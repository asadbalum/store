from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name) -> None:
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() ## same as => select * from item where name = name LIMIT=1

    def save_to_db(self):
        # save item to database
        db.session.add(self) # do update and insert if not exists
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()