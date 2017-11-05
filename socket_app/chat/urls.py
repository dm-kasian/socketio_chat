import views

routes = (
    dict(method='GET', path='/', handler=views.index, name='index'),
    dict(method='GET', path='/chat/{id:[\d\w-]{36}}', handler=views.chat, name='chat'),
    dict(method='POST', path='/login', handler=views.login, name='login'),
    dict(method='POST', path='/add_chat', handler=views.create_chat, name='add_chat'),
)