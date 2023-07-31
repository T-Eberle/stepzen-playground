from app.storage.users.users import user_data


class UserNotFound(Exception):
    pass


def get_user(user_id: str):
    if user_id not in user_data:
        raise UserNotFound()
    else:
        return user_data[user_id]
