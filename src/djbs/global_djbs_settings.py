from pathlib import Path
from .djbs_constants import *

BASE_DIR = Path(__file__).resolve().parent.parent

DJBSTHEME_DEFAULTS = {
    "SEARCH_URL": None,
    "SEARCH_PARAM": None,
    "MENU_FILE": BASE_DIR / "menu_conf.yaml",
    "CHECK_AS_SWITCH": True,
    "FILTER_STYLE": FILTER_STYLE_CLASSIC,
    "FIELDSET_STYLE": STYLE_CARD,
    "INLINESET_STYLE": STYLE_CARD,
    "BADGERIZE_FACETS": True,
    "ICON_SOURCE": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
    "ICON_TAG_PATTERN": '<i class="{icon} {classes}" {attrs}></i>',
    "ICONS": {
        "add": "bi bi-plus-square",
        "back": "bi bi-arrow-left-short",
        "check": "bi bi-check2",
        "check-all": "bi bi-check-all",
        "chevron-left": "bi bi-chevron-left",
        "chevron-right": "bi bi-chevron-right",
        "copy": "bi bi-copy",
        "default": "bi bi-wrench-adjustable-circle",
        "delete": "bi bi-trash3",
        "delete_selected": "bi bi-trash3",
        "dismiss": "bi bi-x",
        "edit": "bi bi-pencil-square",
        "forward": "bi bi-chevron-double-right",
        "help": "bi bi-question-circle",
        "hide": "bi bi-eye-slash",
        "history": "bi bi-clock-history",
        "link": "bi bi-link-45deg",
        "list-view": "bi bi-card-list",
        "remove": "bi bi-eraser",
        "rewind": "bi bi-chevron-double-left",
        "save": "bi bi-save",
        "search": "bi bi-search",
        "show": "bi bi-eye",
        "theme-auto": "bi bi-circle-half",
        "theme-light": "bi bi-sun-fill",
        "theme-dark": "bi bi-moon-stars-fill",
        "user": "bi bi-person-fill",
        "viewsite": "bi bi-globe2",
    },
}

ADMIN_CHANGEABLES = [
    "CHECK_AS_SWITCH",
    "FILTER_STYLE",
    "FIELDSET_STYLE",
    "INLINESET_STYLE",
    "BADGERIZE_FACETS",
]