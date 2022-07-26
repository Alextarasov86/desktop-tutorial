from global_settings.models import Globals



def global_context(request, page):
    settings = Globals.get_solo()

    return {
        'logo': settings.logo,
        'privacy_policy': settings.privacy_policy
    }