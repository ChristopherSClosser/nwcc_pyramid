from .default import (
    home_view,
    about_view,
    values_view,
)


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(home_view, route_name='home')
    config.add_view(about_view, route_name='about')
    config.add_view(values_view, route_name='values')
