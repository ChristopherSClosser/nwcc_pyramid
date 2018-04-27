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
    return {
        'auth': auth,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'tri_info': tri_info,
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
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'main']
    return {
        'auth': auth,
        'content': content,
        'topimg': topimg[0],
        'main': main[0],
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
