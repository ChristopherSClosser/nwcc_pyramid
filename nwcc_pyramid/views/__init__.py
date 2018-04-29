"""Map views with routes."""

from .default import (
    home_view,
    about_view,
    values_view,
    contact_view,
    mission_view,
    staff_view,
    council_view,
    beliefs_view,
    im_new_view,
    foursquare_view,
    giving_view,
)


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(home_view, route_name='home')
    config.add_view(about_view, route_name='about')
    config.add_view(values_view, route_name='values')
    config.add_view(contact_view, route_name='contact')
    config.add_view(mission_view, route_name='mission')
    config.add_view(staff_view, route_name='staff')
    config.add_view(council_view, route_name='council')
    config.add_view(beliefs_view, route_name='beliefs')
    config.add_view(im_new_view, route_name='im_new')
    config.add_view(foursquare_view, route_name='foursquare')
    config.add_view(giving_view, route_name='giving')
