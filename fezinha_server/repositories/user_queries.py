
#user é o nome da tabela?
INSERT_USER = "INSERT INTO user (id, name, login, password) VALUES (%(id)s, %(name)s, %(login)s, %(password)s)"
UPDATE_USER = "UPDATE user SET name=%(name)s, login=%(login)s, password=%(password)s WHERE id = %(id)s"
DELETE_USER = "DELETE FROM user WHERE id = %(id)s"
SELECT_USER = "SELECT id, name, login, password FROM user WHERE id = %(id)s"
SELECT_USER_LOGIN = "SELECT id, name, login, password FROM user WHERE login = %(login)s"
