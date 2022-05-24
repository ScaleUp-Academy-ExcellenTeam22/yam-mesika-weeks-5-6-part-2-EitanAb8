class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient,message_title, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_title: The title of the message.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message(self.message_id, message_title, message_body, sender)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, number_of_messages=None):
        """Returns first N number/all of messages in inbox


        :param str username: The message sender's username.
        :param int number_of_messages: Number of messages to return.
        :return: N first numbers of messages in inbox.
        :rtype: list
        :raises KeyError: if the recipient's username does not exist.
        """
        messages = []
        counter = 0
        messages_to_read = number_of_messages
        if number_of_messages is None:
            messages_to_read = len(self.boxes[username])
        for message in self.boxes[username]:
            if counter < messages_to_read:
                if not message.read:
                    message.read = True
                    counter += 1
                    messages.append(message)
            else:
                break
        return messages

    def search_inbox(self, username, string):
        """
        Return list of all messages contained the string in the title or body.

        :param str username: The message sender's username.
        :param str string: The string.
        :return: A list of messages which has the string in the title or body of the message.
        """
        return [message for message in self.boxes[username] if string in message.title
                or string in message.body]


class Message:
    def __init__(self, message_id, title, body, sender):
        """
        The constructor of Message class.
        :param id_number: The message id number.
        :param title: The message's title.
        :param body: The message's body.
        :param sender: The message's sender.
        """
        self.message_id = message_id
        self.title = title
        self.body = body
        self.sender = sender
        self.read = False

    def __str__(self):
        """
        The function converts and returns the message into a string.
        :return: A string of the message content.
        """
        return f"The message was sent by: {self.sender} \nThe title of the message:\n {self.title}\n " \
               f"The body of the message:\n {self.body}"

    def __repr__(self):
        """
        The function returns the message as string.
        :return: The message content as string.
        """
        return self.__str__()

    def __len__(self):
        """
        The function returns the length of the message's body.
        :return (int): The message's length.
        """
        return len(self.body)


def main():
    post_office = PostOffice(["Alice", "Bob", "Eitan"])
    post_office.send_message(sender="Alice", recipient="Bob", message_title="Hi its Alice",
                             message_body="How are you?")
    post_office.send_message(sender="Bob", recipient="Alice", message_title="Hi its Bob",
                             message_body="I am ok, how are you?")
    post_office.send_message(sender="Bob", recipient="Eitan", message_title="Hi its Bob",
                             message_body="Hi Eitan. Wanna hack with me?")
    post_office.send_message(sender="Eitan", recipient="Bob", message_title="Hi its Eitan",
                             message_body="Sure. who will be the victim?")
    post_office.send_message(sender="Bob", recipient="Eitan", message_title="Hi its Bob",
                             message_body="Alice :D")

    print(post_office.read_inbox("Eitan"), 1)
    print(post_office.read_inbox("Bob"))
    print(post_office.search_inbox("Bob", "Eitan"))


if __name__ == "__main__":
    main()



