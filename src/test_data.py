from collections import namedtuple

from faker import Faker


class TestData:

    fake = Faker()

    user = namedtuple("User", ["name", "email"])

    test_user = user("Igor", "igorqa.9@gmail.com")

    def text_generator(self, max_length=25):
        return self.fake.text(max_nb_chars=max_length)
