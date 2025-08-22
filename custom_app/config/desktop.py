from . import __version__ as app_version


def get_data():
    return [
        {
            "module_name": "Custom App",
            "category": "Modules",
            "label": "Custom App",
            "icon": "octicon octicon-file-directory",
            "items": [
                {"type": "doctype", "name": "Worker", "label": "Worker"}
            ]
        }
    ]
