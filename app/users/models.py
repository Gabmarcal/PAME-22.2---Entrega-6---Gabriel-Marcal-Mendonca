from app.models import BaseModel
from app.extensions import db
import bcrypt

class Users(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30))
    idade = db.Column(db.Integer)
    password_hash = db.Column(db.LargeBinary(128))

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self,password) -> None:
        self.password_hash = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
    
    def check_password(self,password) -> bool:
        return bcrypt.checkpw(password.encode(),self.password_hash)