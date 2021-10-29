"""Collection of graphql schema."""

FIND_USER = """
query FindUser($email: String, $username: String) {
  users(where: {_or: [{email: {_eq: $email}}, {username: {_eq: $username}}]}) {
    id
    email
    username
    password
    is_active
    is_email_verified
    is_superuser
    last_login
  }
}
"""

CREATE_USER = """
mutation CreateUser($email: String, $full_name: String, $password: String, $username: String, $last_login: timestamptz) {
  insert_users_one(object: {email: $email, full_name: $full_name, password: $password, username: $username, last_login: $last_login}) { # noqa B950
    id
  }
}
"""

GET_USER = """
query GetUser($id: uuid = "%s") {
  users_by_pk(id: $id) {
    id
    email
    username
    password
    is_active
    is_email_verified
    is_superuser
    last_login
  }
}
"""

CHANGE_USER_PASSWORD = """
mutation ChangeUserPassword($id: uuid = "%(user_id)s", $password: String = "%(new_password)s") {
  update_users_by_pk(pk_columns: {id: $id}, _set: {password: $password}) {
    id
  }
}
"""


VERIFY_USER_EMAIL = """
mutation VerifyUserEmail($id: uuid = "%(user_id)s", $is_email_verified: Boolean = "%(is_email_verified)s") {
  update_users_by_pk(pk_columns: {id: $id}, _set: {is_email_verified: $is_email_verified}) {
    id
  }
}
"""


LAST_LOGIN = """
mutation LastLogin($id: uuid = "%(user_id)s", $last_login: timestamptz = "%(last_login)s") {
  update_users_by_pk(pk_columns: {id: $id}, _set: {last_login: $last_login}) {
    last_login
  }
}
"""


CHANGE_USER_EMAIL = """
mutation ChangeUserEmail($id: uuid = "%(user_id)s", $email: String = "%(email)s") {
  update_users_by_pk(pk_columns: {id: $id}, _set: {email: $email, is_email_verified: false}) {
    id
  }
}
"""
