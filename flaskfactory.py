# --------------------------------------------------------------------------- #
#                                                                             #
#                           Core Imports                                      #
#                                                                             #
# --------------------------------------------------------------------------- #

from datetime import timedelta

from flask import Flask

from config.configuration import DEBUG, SESSION_LIFETIME, STATIC, TEMPLATES
import base64

# --------------------------------------------------------------------------- #
#                                                                             #
#                       Default Configuration                                 #
#                                                                             #
# --------------------------------------------------------------------------- #


class FlaskFactory:
    NAME = __name__

    @staticmethod
    def _format_app_abbrev(string: str) -> str:
        if len(string) < 1:
            return 'Error'

        if string.__contains__(' '):
            string_split = string.split(' ')
        elif string.__contains__('_'):
            string_split = string.split('_')
        elif string.__contains__('-'):
            string_split = string.split('-')
        else:
            string_split = [string]

        formatted = []
        for split in string_split:
            if len(split) > 1:
                formatted.append(
                    f'{split[0].upper()}{split[1:].lower()}')
            else:
                formatted.append(f'{split[0].upper()}')
        return ' '.join(formatted)

    @staticmethod
    def create(name: str) -> Flask:
        app = Flask(
            name.lower(),
            static_url_path='',
            static_folder=STATIC,
            template_folder=TEMPLATES
        )

        display_name = FlaskFactory._format_app_abbrev(name)
        app.__name__ = display_name
        app.title = display_name
        app.config.from_object(name.lower())

        app.config.update(
            SESSION_COOKIE_DOMAIN=name,
            SESSION_COOKIE_NAME=name,
            DEBUG=DEBUG
        )

        app.secret_key = str(
            base64.standard_b64encode(
                bytes(
                    name, 'utf-8')))[
            2:-1]
        app.permanent_session_lifetime = timedelta(
            days=SESSION_LIFETIME)

        return app
