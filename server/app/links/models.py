from app.database import db
from hashids import Hashids


class LinksModel(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, autoincrement=True,
                   unique=True, primary_key=True)
    url = db.Column(db.String(150), nullable=False)
    hashed_url = db.Column(db.String(20), unique=True)
    count_visited = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_to_db(self):
        db.session.add(self)
        db.session.flush()
        db.session.refresh(self)
        self.hashed_url = LinksModel.hash_url(self.url, self.id)
        db.session.commit()

    def increment_count_visited(self):
        db.session.add(self)
        self.count_visited += 1
        db.session.commit()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    def find_by_hashed_url(cls, hashed_url):
        return cls.query.filter_by(hashed_url=hashed_url).first()

    @staticmethod
    def hash_url(url, pk):
        # pk = object's id
        hashids = Hashids(salt=url, min_length=7)
        link_id = hashids.encode(pk)
        return link_id
