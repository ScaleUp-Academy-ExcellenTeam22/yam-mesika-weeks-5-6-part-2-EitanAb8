
class User:
    """
    This class represents a user in the system.
    A user can be regular user or admin user.
    """
    def __init__(self, username: str, password: str, permissions : bool):
        self.username = username
        self.password = password
        self.is_admin = permissions


class UserManager:
    """
    This class represents a UserManager,
    which can control users and operates system commands.
    """
    def __init__(self):
        self.users = []

    def add_user(self, new_user: User):
        """
        The function adds a new user to the user list.
        :param new_user: A new user.
        :return: None
        """
        self.users.append(User)


class File:
    """
    This class represent a File in a system.
    """
    def __init__(self, file_name: str, content, creator: User):
        self.name = file_name
        self.content = content
        self.creator = creator


class BinaryFile(File):
    """
    This class represent a binary file.
    """
    def __init__(self, file_name: str, content, creator: User, size: float):
        super().__init__(file_name, content, creator)
        self.size_by_kilo_bytes = size

    def get_dimensions(self) -> str:
        """
        This function returns the dimensions of the binary file.
        :return: A string of the file dimensions.
        """
        return "rows: x, cols: y"

    def read(self, user: User):
        """
        The function returns the content if the asking user has permissions to make this action.
        :param user: The asking user for this service.
        :return: The content of the file if the user has permissions, None either.
        """
        return self.content if user.is_admin or user == self.creator else None


class TextualFile(File):
    """
    This class represents a textual file.
    """
    def __init__(self, file_name: str, content, creator: User, size: float):
        super().__init__(file_name, content, creator)
        self.size_by_kilo_bytes = size

    def count(self, text: str) -> int:
        return self.content.count(text)

    def read(self, user: User):
        """
        The function returns the content if the asking user has permissions to make this action.
        :param user: The asking user for this service.
        :return: The content of the file if the user has permissions, None either.
        """
        return self.content if user.is_admin or user == self.creator else None


class Directory(File):
    """
    This class represent a directory of files.
    """
    def __init__(self, file_name: str, content, creator: User, size: float):
        super().__init__(file_name, content, creator)
        self.files_list = []

    def add_file(self, file: File):
        self.files_list.append(file)

    def remove_file(self, file: File):
        self.files_list.remove(file)
