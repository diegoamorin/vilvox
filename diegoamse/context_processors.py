from django.conf import settings

site_name = settings.SITE_NAME


def nombres(request):
    return {"site_name": site_name}
