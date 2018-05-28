"""Init Pyramid WSGI application."""
import os
from pyramid.config import Configurator
# from pyramid_mailer import mailer_factory_from_settings


def main(global_config, **settings):
    """Function returns a Pyramid WSGI application."""
    # settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')
    # settings["mail.username"] = os.environ["MAIL_USERNAME"]
    # settings["mail.password"] = os.environ["MAIL_PASSWORD"]
    config = Configurator(settings=settings)
    config.include('pyramid_mailer')
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.views')
    config.include('.security')
    # config.registry['mailer'] = mailer_factory_from_settings(settings)
    config.scan()
    return config.make_wsgi_app()
