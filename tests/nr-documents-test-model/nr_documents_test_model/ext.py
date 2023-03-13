import re

from nr_documents_test_model import config as config


class NrDocumentsTestModelExt:
    """nr_documents_test_model extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        self.resource = None
        self.service = None

        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""

        self.init_config(app)
        if not self.is_inherited():
            self.init_resource(app)
            self.register_flask_extension(app)

    def register_flask_extension(self, app):
        app.extensions["nr_documents_test_model"] = self

    def init_resource(self, app):
        """Initialize vocabulary resources."""
        self.service = app.config[
            "NR_DOCUMENTS_TEST_MODEL_SERVICE_CLASS_NR_DOCUMENTS_TEST_MODEL"
        ](
            config=app.config[
                "NR_DOCUMENTS_TEST_MODEL_SERVICE_CONFIG_NR_DOCUMENTS_TEST_MODEL"
            ](),
        )
        self.resource = app.config[
            "NR_DOCUMENTS_TEST_MODEL_RESOURCE_CLASS_NR_DOCUMENTS_TEST_MODEL"
        ](
            service=self.service,
            config=app.config[
                "NR_DOCUMENTS_TEST_MODEL_RESOURCE_CONFIG_NR_DOCUMENTS_TEST_MODEL"
            ](),
        )

    def init_config(self, app):
        """Initialize configuration."""
        for identifier in dir(config):
            if re.match("^[A-Z_0-9]*$", identifier) and not identifier.startswith("_"):
                app.config.setdefault(identifier, getattr(config, identifier))

    def is_inherited(self):
        from importlib_metadata import entry_points

        ext_class = type(self)
        for ep in entry_points(group="invenio_base.apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        for ep in entry_points(group="invenio_base.api_apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        return False
