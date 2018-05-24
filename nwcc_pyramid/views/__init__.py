"""Map views with routes."""

from .default import (
    home_view,
    welcome_view,
    sundays_view,
    youth_kids_view,
    go_deeper_view,
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
    events_view,
    foodbank_view,
    connect_view,
)


def includeme(config):
    """List of views to include for the configurator object."""
    config.add_view(home_view, route_name='home')
    config.add_view(welcome_view, route_name='welcome')
    config.add_view(sundays_view, route_name='sundays')
    config.add_view(youth_kids_view, route_name='youth_kids')
    config.add_view(go_deeper_view, route_name='go_deeper')
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
    config.add_view(events_view, route_name='events')
    config.add_view(foodbank_view, route_name='foodbank')
    config.add_view(connect_view, route_name='connect')
