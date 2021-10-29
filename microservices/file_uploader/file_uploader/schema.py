"""Collection of graphql schema."""
CHANGE_USER_PICTURE = """
mutation ChangeUserPassword($id: uuid = "%(user_id)s", $picture_url: String = "%(picture)s") {
  update_users_by_pk(pk_columns: {id: $id}, _set: {picture_url: $picture_url}) {
    picture_url
  }
}
"""
