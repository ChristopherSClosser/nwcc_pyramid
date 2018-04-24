from .default import (
    home_view,
)


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(home_view, route_name='home')
