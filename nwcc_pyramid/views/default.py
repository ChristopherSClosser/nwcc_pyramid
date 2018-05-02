"""Interstate Sales Views."""

from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config, forbidden_view_config
from ..security import is_authenticated
from ..models import MyModel
import shutil
import os


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    """Home view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'home').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    tri_info = [item for item in content if item.category == 'tri_info']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'tri_info': tri_info,
        'steps': steps,
    }


@view_config(route_name='about', renderer='../templates/about.jinja2')
def about_view(request):
    """About view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'main']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main[0],
    }


@view_config(route_name='values', renderer='../templates/values.jinja2')
def values_view(request):
    """Core Values view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'core_values']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main[1],
    }


@view_config(route_name='contact', renderer='../templates/contact.jinja2')
def contact_view(request):
    """Contact view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'contact']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main[1],
    }


@view_config(route_name='mission', renderer='../templates/mission.jinja2')
def mission_view(request):
    """Mission statement view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'mission_statement']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main[1],
    }


@view_config(route_name='staff', renderer='../templates/staff.jinja2')
def staff_view(request):
    """Mission statement view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'staff']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main,
    }


@view_config(route_name='council', renderer='../templates/council.jinja2')
def council_view(request):
    """Council view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'council']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main,
    }


@view_config(route_name='beliefs', renderer='../templates/beliefs.jinja2')
def beliefs_view(request):
    """What we believe view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'we_believe']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main,
    }


@view_config(route_name='im_new', renderer='../templates/im_new.jinja2')
def im_new_view(request):
    """What we believe view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'im_new']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main[1],
    }


@view_config(route_name='foursquare', renderer='../templates/foursquare.jinja2')
def foursquare_view(request):
    """What we believe view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'foursquare']
    return {
        'auth': auth,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main,
    }


@view_config(route_name='giving', renderer='../templates/giving.jinja2')
def giving_view(request):
    """Giving view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'giving').all()
    # submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    # main = [item for item in content if item.category == 'foursquare']
    return {
        'auth': auth,
        # 'submenu': submenu,
        'topimg': topimg[0],
        'main': content,
    }


@view_config(route_name='events', renderer='../templates/events.jinja2')
def events_view(request):
    """Events' view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'events').all()
    # submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    # main = [item for item in content if item.category == 'foursquare']
    return {
        'auth': auth,
        # 'submenu': submenu,
        'topimg': topimg[0],
        'main': content,
    }


@view_config(route_name='login', renderer='../templates/login.jinja2')
@forbidden_view_config(renderer='../templates/nonentry.jinja2')
def login(request):
    """Login view."""
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if is_authenticated(username, password):
            headers = remember(request, username)
            return HTTPFound(request.route_url('home'), headers=headers)
        return {'res': 'Username or Password Entered Incorrect'}


@view_config(route_name='logout')
def logout(request):
    """."""
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)
