"""NWCC routes."""


def includeme(config):
    """Defined routes."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('about', '/about_us')
    config.add_route('values', '/about_us/core_values')
