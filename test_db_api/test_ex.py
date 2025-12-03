from test_db_api.models.user import User


def test_user_all(db_session):
    users = db_session.query(User).all()

    if users:
        for user in users:
            print(f"\nID: {user.id}")
            print(f"  Username: {user.username}")
            print(f"  Email: {user.email}")
            print(f"  Role: {user.role}")
    else:
        print("  Пользователей нет")
