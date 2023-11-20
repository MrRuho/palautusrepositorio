from stub_io import StubIO
from repositories.user_repository import UserRepository
from services.user_service import UserService
from app import App


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._user_repository = UserRepository()
        self._user_service = UserService(self._user_repository)

        self._app = App(
            self._user_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    def create_user(self, username, password):
        if not username.isalpha() or len(username) < 3:
            self._io.write("Virheellinen käyttäjänimi")
        elif not (any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and len(password) >= 8):
            self._io.write("Virheellinen salasana")
        else:
            self._io.write("Kelvollinen käyttäjänimi ja salasana")
            self._user_service.create_user(username, password)


