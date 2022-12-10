import uuid

from sqlalchemy.sql.schema import MetaData, Column
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.sql.sqltypes import String, Boolean

AppMetaData = MetaData()
BaseOrm = declarative_base(metadata=AppMetaData)


class UserOrm(BaseOrm):
    id = Column(String(32), default=lambda: str(uuid.uuid4()), primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)

    __tablename__ = "users"


class RoleOrm(BaseOrm):
    id = Column(String(32), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = Column(String(100), nullable=False)
    is_active = Column(Boolean(), nullable=False, default=True)

    __tablename__ = "roles"

