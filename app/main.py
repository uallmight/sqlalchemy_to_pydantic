from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm.session import Session
from app import models

engine: Engine = create_engine("sqlite://", echo=True)


def _seed_database():
    with Session(engine) as session:
        session: Session  # added for typehint
        models.AppMetaData.create_all(bind=engine)

        user_one = models.UserOrm(
            username="username_1",
            email="username_1@example.com",
        )
        user_two = models.UserOrm(
            username="username_2",
            email="username_2@example.com",
        )
        active_role = models.RoleOrm(
            name="Active Role",
        )
        inactive_role = models.RoleOrm(
            name="Inactive Role",
        )
        session.add_all([user_one, user_two, active_role, inactive_role])
        session.flush()
        session.commit()


def _run():
    _seed_database()


if __name__ == "__main__":
    _run()
