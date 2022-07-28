from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'blog',
    'review',
    'global_settings'

]

GARPIX_PAGE_GLOBAL_CONTEXT = 'app.global_context.global_context'
