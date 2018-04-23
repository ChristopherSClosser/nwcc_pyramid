"""NWCC routes."""


def includeme(config):
    """Defined routes."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
