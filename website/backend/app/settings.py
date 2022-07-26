from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'blog',
    'global_settings',
    'feedback'

]

GARPIX_PAGE_GLOBAL_CONTEXT = 'app.global_context.global_context'
