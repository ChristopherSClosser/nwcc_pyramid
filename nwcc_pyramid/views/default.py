"""NWCC Views."""

import os
from datetime import datetime
from pyramid.security import remember, forget
from pyramid.view import view_config, forbidden_view_config
from pyramid.view import notfound_view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid_mailer.message import Message
from ..models import MyModel
from ..security import is_authenticated


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    """."""
    query = request.dbsession.query(MyModel)
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    request.response.status = 404
    return {
        'main_menu': main_menu,
    }


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    """Home view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
        auth_tools = request.dbsession.query(
            MyModel
        ).filter(MyModel.category == 'admin').all()
    except KeyError:
        auth_tools = []
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'home').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    specialimg = [item for item in content if item.category == 'specialimg']
    topimg = [item for item in content if item.category == 'topimg']
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'specialimg': specialimg,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'steps': steps,
        'auth_tools': auth_tools,
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
    main = [item for item in content if item.subcategory == 'main']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main[0],
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
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'tri_img': tri_img,
        'quad_info': quad_info,
        'main': main[0],
        'steps': steps,
    }


@view_config(route_name='go_deeper', renderer='../templates/ministries.jinja2')
def go_deeper_view(request):
    """Ministry view."""
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


@view_config(
    route_name='bible_studies',
    renderer='../templates/bible_studies.jinja2'
)
def bible_studies_view(request):
    """Bible studies view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
        auth_tools = request.dbsession.query(
            MyModel
        ).filter(MyModel.category == 'admin').all()
    except KeyError:
        auth_tools = []
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
        'auth_tools': auth_tools,
    }


@view_config(
    route_name='life_groups',
    renderer='../templates/life_groups.jinja2'
)
def life_groups_view(request):
    """Life groups view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(
        MyModel.page == 'ministries'
    ).order_by(MyModel.id.asc())
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


@view_config(route_name='bobs', renderer='../templates/bobs.jinja2')
def bobs_view(request):
    """Walk the walk view."""
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
    main = [item for item in content if item.category == 'bobs']
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
    title = [item for item in content if item.category == 'worship_title']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'title': title[0],
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
    tri_img = [item for item in content if item.category == 'tri_img']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'main']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
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
        auth_tools = request.dbsession.query(
            MyModel
        ).filter(MyModel.category == 'admin').all()
    except KeyError:
        auth_tools = []
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'message').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    title = [item for item in content if item.category == 'audio_title']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = query.filter(
        MyModel.subcategory == 'track'
    ).order_by(MyModel.id.desc())
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'title': title[0],
        'quad_info': quad_info,
        'main': main[:12],
        'steps': steps,
        'auth_tools': auth_tools,
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
    title = [item for item in content if item.subcategory == 'title']
    quad_info = [item for item in content if item.category == 'quad_info']
    main = [item for item in content if item.category == 'children']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'topimg': topimg[0],
        'title': title[0],
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
    menu_content = query.filter(MyModel.page == 'ministries')
    submenu = [
        item for item in menu_content if item.title == 'menu_place_holder'
    ]
    title = [item for item in content if item.subcategory == 'title']
    main = [item for item in content if item.subcategory == 'Food Bank']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'imgtitle': title[0],
        'main': main,
    }


@view_config(
    route_name='first_impressions',
    renderer='../templates/first_impressions.jinja2'
)
def first_impressions_view(request):
    """First impressions view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    main = [item for item in content if item.category == 'first_impressions']
    steps = [item for item in content if item.category == 'steps']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'content': content,
        'submenu': submenu,
        'main': main,
        'steps': steps,
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
    main = [item for item in content if item.category == 'core_values']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'main': main[1],
    }


@view_config(route_name='means', renderer='../templates/means.jinja2')
def means_view(request):
    """Love boldly means view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
    except KeyError:
        pass
    query = request.dbsession.query(MyModel)
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    return {
        'auth': auth,
        'main_menu': main_menu,
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
    main = [item for item in content if item.category == 'contact']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
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
    main = [item for item in content if item.category == 'mission_statement']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
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
    menu_title = [item for item in submenu if item.category == 'staff']
    main = [item for item in content if item.category == 'staff']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'menu_title': menu_title[0],
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
    menu_title = [item for item in submenu if item.category == 'council']
    main = query.filter(
        MyModel.category == 'council'
    ).order_by(MyModel.title.asc())
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'menu_title': menu_title[0],
        'main': main,
    }


@view_config(route_name='beliefs', renderer='../templates/beliefs.jinja2')
def beliefs_view(request):
    """What we believe view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
        auth_tools = request.dbsession.query(
            MyModel
        ).filter(MyModel.category == 'admin').all()
    except KeyError:
        auth_tools = []
    query = request.dbsession.query(MyModel)
    content = query.filter(MyModel.page == 'about').all()
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    submenu = [item for item in content if item.title == 'menu_place_holder']
    menu_title = [item for item in submenu if item.category == 'we_believe']
    main = [item for item in content if item.category == 'we_believe']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'menu_title': menu_title[0],
        'main': main,
        'auth_tools': auth_tools,
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
    main = [item for item in content if item.category == 'im_new']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
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
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    cc_email = os.environ['MAIL_SEND_TO']

    if request.method == 'POST':
        info = request.POST
        tmp = """
            First Name: {0}\n
            Last Name: {1}\n
            Address: {2}\n
            {3}, {4} {5}\n
            Phone: {6}\n
            Email: {7}\n
            Comment: {8}\n
            How they found us: {9}\n
            I am {10} age {11}, children in {12}\n
            I desire {13}
        """
        question_2 = []
        question_3 = []
        question_4 = []
        for item in list(info.keys()):
            if 'question_2' in item:
                question_2.append(info[item])
            if 'question_3' in item:
                question_3.append(info[item])
            if 'question_4' in item:
                question_4.append(info[item])

        email_body = tmp.format(
            info['firstName'],
            info['lastName'],
            info['address'],
            info['city'],
            info['state'],
            info['zip'],
            info['phone'],
            info['email'],
            info['comment'],
            info['question_1'],
            ' & '.join(str(i) for i in question_2),
            ' & '.join(str(i) for i in question_3),
            ' & '.join(str(i) for i in question_4),
            info['question_5'],
        )

        mailer = request.mailer
        message = Message(
            subject="New connection card!",
            sender="weloveboldly@gmail.com",
            recipients=[cc_email],
            body=email_body,
        )

        mailer.send_immediately(message)
        return HTTPFound(request.route_url('home'))
    return {
        'auth': auth,
        'main_menu': main_menu,
    }


@view_config(
    route_name='foursquare',
    renderer='../templates/foursquare.jinja2'
)
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
    menu_title = [item for item in submenu if item.category == 'foursquare']
    main = [item for item in content if item.category == 'foursquare']
    return {
        'auth': auth,
        'main_menu': main_menu,
        'submenu': submenu,
        'menu_title': menu_title[0],
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
    return {
        'auth': auth,
        'main_menu': main_menu,
        'main': content,
    }


@view_config(route_name='events', renderer='../templates/events.jinja2')
def events_view(request):
    """Events' view."""
    auth = False
    try:
        auth = request.cookies['auth_tkt']
        auth_tools = request.dbsession.query(
            MyModel
        ).filter(MyModel.category == 'admin').all()
    except KeyError:
        auth_tools = []
    query = request.dbsession.query(MyModel)
    content = query.filter(
        MyModel.page == 'events'
    ).order_by(MyModel.date.asc())
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    main = [item for item in content if item.category == 'events']
    topimg = [item for item in content if item.category == 'topimg']
    current = [item for item in content if item.category == 'special_events']
    events = [item for item in current if item.date > datetime.now().date()]
    return {
        'auth': auth,
        'main_menu': main_menu,
        'events': events,
        'topimg': topimg[0],
        'main': main,
        'auth_tools': auth_tools,
    }


@view_config(route_name='login', renderer='../templates/login.jinja2')
@forbidden_view_config(renderer='../templates/nonentry.jinja2')
def login(request):
    """Login view."""
    query = request.dbsession.query(MyModel)
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if is_authenticated(username, password):
            headers = remember(request, username)
            return HTTPFound(request.route_url('home'), headers=headers)
        return {'res': 'Username or Password Entered Incorrect'}
    return {'main_menu': main_menu}


@view_config(route_name='logout')
def logout(request):
    """."""
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)


@view_config(
    route_name='new',
    renderer='../templates/entry.jinja2',
    permission='secret',
)
def create_view(request):
    """Display create a list entry."""
    query = request.dbsession.query(MyModel)
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    if request.POST:
        entry = MyModel(
            page=request.POST['page'],
            category=request.POST['category'],
            subcategory=request.POST['subcategory'],
            title=request.POST['title'],
            img=request.POST['img'],
            imgsrc=request.POST['imgsrc'],
            markdown=request.POST['markdown'],
            extra=request.POST['extra'],
            date=datetime.strptime(request.POST['date'], '%b %d %Y'),
        )
        request.dbsession.add(entry)
        return HTTPFound()
    return {'main_menu': main_menu}


@view_config(
    route_name='delete',
    renderer='../templates/delete.jinja2',
    permission='secret',
)
def delete_view(request):
    """."""
    ident = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(ident)
    query = request.dbsession.query(MyModel)
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    if request.POST:
        request.dbsession.delete(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('home'))
    form_fill = {
        'page': entry.page,
        'category': entry.category,
        'subcategory': entry.subcategory,
        'title': entry.title,
        'img': entry.img,
        'imgsrc': entry.imgsrc,
        'markdown': entry.markdown,
        'extra': entry.extra,
        'date': entry.date,
    }
    return {'main_menu': main_menu, 'entry': form_fill}


@view_config(
    route_name='edit',
    renderer='../templates/edit.jinja2',
    permission='secret',
)
def update_view(request):
    """Display the update entry."""
    ident = int(request.matchdict['id'])
    entry = request.dbsession.query(MyModel).get(ident)
    query = request.dbsession.query(MyModel)
    main_menu = query.filter(MyModel.subcategory == 'base').all()
    if not entry:
        raise HTTPNotFound()
    if request.POST:
        entry.page = request.POST['page']
        entry.category = request.POST['category']
        entry.subcategory = request.POST['subcategory']
        entry.title = request.POST['title']
        entry.img = request.POST['img']
        entry.imgsrc = request.POST['imgsrc']
        entry.markdown = request.POST['markdown']
        entry.extra = request.POST['extra']
        entry.date = datetime.strptime(request.POST['date'], '%b %d %Y'),

        request.dbsession.flush()
        return HTTPFound()

    form_fill = {
        'page': entry.page,
        'category': entry.category,
        'subcategory': entry.subcategory,
        'title': entry.title,
        'img': entry.img,
        'imgsrc': entry.imgsrc,
        'markdown': entry.markdown,
        'extra': entry.extra,
        'date': entry.date.strftime('%b %d %Y'),
    }
    return {'main_menu': main_menu, 'entry': form_fill}


@view_config(renderer='json', route_name='api')
def api_view(request):
    """Display entries as json."""
    query = request.dbsession.query(MyModel)
    entries = query.order_by(MyModel.id.asc()).all()
    return {
        'entries': [
            {
                'id': entry.id,
                'page': entry.page,
                'category': entry.category,
                'subcategory': entry.subcategory,
                'title': entry.title,
                'img': entry.img,
                'imgsrc': entry.imgsrc,
                'markdown': entry.markdown,
                'extra': entry.extra,
                'date': entry.date.strftime('%b %d %Y'),
            }
            for entry in entries
        ]
    }
