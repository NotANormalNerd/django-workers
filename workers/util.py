import logging

from importlib import import_module


log = logging.getLogger(__name__)


def autodiscover():
    """
    Autodiscover `tasks.py` files in much the same way Django admin discovers `admin.py`

    """
    from django.conf import settings

    for app in settings.INSTALLED_APPS:
        try:
            import_module('tasks', app)
            log.info(f'Sucessfully imported {app}.tasks.')
        except ImportError:
            continue
        except Exception as e:
            log.error('failed to autodiscover {0}: does it have an __init__.py file?'.format(app))
            continue

        log.debug('discovered {0}.tasks'.format(app))
        import_module("%s.tasks" % app)
