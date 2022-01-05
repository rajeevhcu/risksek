from .. import db
from sqlalchemy.dialects.mysql import INTEGER, TEXT


class AccessHistory(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'access_history'

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    created_date_time = db.Column(db.BIGINT, nullable=False)
    parameter = db.Column(TEXT, nullable=False)
