"""Interstate Sales Views."""

import os
import shutil
from ..models import MyModel
from ..security import is_authenticated
from pyramid_mailer.message import Message
from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config, forbidden_view_config
from pyramid.view import notfound_view_config


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    """."""
    query = request.dbsession.query(MyModel)
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    request.response.status = 404
    return {
        'main_menu': main_menu,
    }


"""
    mailer = request.mailer
    message = Message(
        subject="hello world",
        sender="admin@mysite.com",
        recipients=["arthur.dent@gmail.com"],
        body="hello, arthur")

    mailer.send(message)
"""


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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'steps': steps,
    }


@view_config(route_name='welcome', renderer='../templates/welcome.jinja2')
def welcome_view(request):
    """Welcome view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'welcome').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    about = query.filter(MyModel.page == 'about').all()
    submenu = [item for item in about if item.title == 'menu_place_holder']
    main = [item for item in about if item.category == 'main']
    tri_img = [item for item in content if item.category == 'tri_img']
    tri_info = [item for item in content if item.category == 'tri_info']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'submenu': submenu,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'tri_info': tri_info,
        'steps': steps,
        'main': main[0]
    }


@view_config(route_name='sundays', renderer='../templates/sundays.jinja2')
def sundays_view(request):
    """Sunday mornings view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'sundays').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'steps': steps,
    }


@view_config(route_name='youth_kids', renderer='../templates/youth.jinja2')
def youth_kids_view(request):
    """Youth & kids view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'youth_kids').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main[0],
        'steps': steps,
    }


@view_config(route_name='go_deeper', renderer='../templates/ministries.jinja2')
def go_deeper_view(request):
    """Ministries view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'ministries').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    steps_info = query.filter(MyModel.page == 'home').all()
    topimg = [item for item in content if item.category == 'topimg']
    submenu = [item for item in content if item.title == 'menu_place_holder']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in steps_info if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main[0],
        'steps': steps,
    }


@view_config(route_name='bible_studies', renderer='../templates/bible_studies.jinja2')
def bible_studies_view(request):
    """Bible studies view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'ministries').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'bible_studies']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main,
    }


@view_config(route_name='life_groups', renderer='../templates/life_groups.jinja2')
def life_groups_view(request):
    """Life groups view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'ministries').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'life_groups']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main,
    }


@view_config(route_name='military', renderer='../templates/military.jinja2')
def military_view(request):
    """Military view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'ministries').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'military_ministries']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main,
    }


@view_config(route_name='worship', renderer='../templates/worship.jinja2')
def worship_view(request):
    """Worship view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'worship').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main[0],
        'steps': steps,
    }


@view_config(route_name='hebrews', renderer='../templates/hebrews.jinja2')
def hebrews_view(request):
    """He brews boldly view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'hebrews').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main[0],
        'steps': steps,
    }


@view_config(route_name='message', renderer='../templates/message.jinja2')
def message_view(request):
    """Message view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'message').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main,
        'steps': steps,
    }


@view_config(route_name='children', renderer='../templates/children.jinja2')
def children_view(request):
    """Nursery & kids church view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'children').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main,
        'steps': steps,
    }


@view_config(route_name='foodbank', renderer='../templates/foodbank.jinja2')
def foodbank_view(request):
    """Foodbank view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'foodbank').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    # submenu = [item for item in content if item.title == 'menu_place_holder']
    title = [item for item in content if item.subcategory == 'title']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.subcategory == 'info']
    return {
        'auth': auth,
        'main_menu': main_menu,
        # 'submenu': submenu,
        'imgtitle': title[0],
        'topimg': topimg[0],
        'main': main,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'main']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'core_values']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'contact']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'mission_statement']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'staff']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'council']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'we_believe']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'im_new']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'topimg': topimg[0],
        'main': main[1],
    }


@view_config(route_name='connect', renderer='../templates/connect.jinja2')
def connect_view(request):
    """Connect view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'connect').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'connect_form']
    # cc_email = os.environ['MAIL_SEND_TO']
    # if request.method == 'POST':
    #     mailer = request.mailer
    #     message = Message(
    #         subject="New connection card!",
    #         sender="weloveboldly@gmail.com",
    #         recipients=[cc_email],
    #         body="hello, arthur")
    #
    #     mailer.send_immediately(message)
    #     # transaction.commit()
    #     return HTTPFound(request.route_url('home'))
    return {
        'auth': auth,
        'main_menu': main_menu,
        # 'submenu': submenu,
        # 'topimg': topimg[0],
        # 'main': main[1],
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    main = [item for item in content if item.category == 'foursquare']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    # submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    # main = [item for item in content if item.category == 'foursquare']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    # submenu = [item for item in content if item.title == 'menu_place_holder']
    topimg = [item for item in content if item.category == 'topimg']
    # main = [item for item in content if item.category == 'foursquare']
    return {
        'auth': auth,
        'main_menu': main_menu,
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
