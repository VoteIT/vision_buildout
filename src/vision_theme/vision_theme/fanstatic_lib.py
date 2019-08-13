from arche.interfaces import IBaseView
from arche.interfaces import IViewInitializedEvent
from fanstatic import Library
from fanstatic import Resource
from js.bootstrap import bootstrap_css
from voteit.core.fanstaticlib import voteit_main_css


library = Library('vision_theme', 'static')


vision_custom_bootstrap_css = Resource(library, 'css/bootstrap.css', supersedes=(bootstrap_css,))
vision_theme_css = Resource(library, 'css/main.css', depends = (vision_custom_bootstrap_css, voteit_main_css))


def need_subscriber(view, event):
    vision_theme_css.need()


def includeme(config):
    config.add_subscriber(need_subscriber, [IBaseView, IViewInitializedEvent])
