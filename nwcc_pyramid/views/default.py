"""Interstate Sales Views."""

# from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config, forbidden_view_config
# from ..security import is_authenticated
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
        'topimg': topimg,
        'tri_img': tri_img,
        'tri_info': tri_info,
    }
