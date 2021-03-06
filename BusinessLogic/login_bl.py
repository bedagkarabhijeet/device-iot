
from datetime import datetime, timedelta
import jwt


class LoginBL:
    """
    Business class used to managed Login operations
    """
    def __init__(self, logger, configuration):
        self.__logger = logger
        self.__config = configuration

        self.__fake_db = {
            "admin": "admin"
        }

    def verify_password(self, username, password):
        """
        Verify username and password of user

        :return: True if logic successful False otherwise
        """
        print(username, password)
        if username in self.__fake_db and self.__fake_db[username] == password:
            return True
        return False

    def generate_token(self, username):
        """
        Generate new JWT token using user details; Currently remains alive for 3 days
        :param username: Name of user user
        :return: JWT token
        """
        expire = datetime.utcnow() + timedelta(
            seconds=60 * 60 * 24 * 3
        )
        to_encode = {
            "exp": expire, "username": username
        }
        encoded_jwt = jwt.encode(to_encode, self.__config["SECRET_KEY"],
                                 algorithm=self.__config["SECURITY_ALGORITHM"])
        return encoded_jwt
