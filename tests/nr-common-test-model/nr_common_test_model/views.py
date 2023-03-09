from flask import Blueprint


def create_blueprint_from_app_nr_common_test_model(app):
    """Create  blueprint."""
    blueprint = app.extensions["nr_common_test_model"].resource.as_blueprint()
    blueprint.record_once(init_create_blueprint_from_app_nr_common_test_model)

    # calls record_once for all other functions starting with "init_addons_"
    # https://stackoverflow.com/questions/58785162/how-can-i-call-function-with-string-value-that-equals-to-function-name
    funcs = globals()
    funcs = [
        v
        for k, v in funcs.items()
        if k.startswith("init_addons_nr_common_test_model") and callable(v)
    ]
    for func in funcs:
        blueprint.record_once(func)

    return blueprint


def init_create_blueprint_from_app_nr_common_test_model(state):
    """Init app."""
    app = state.app
    ext = app.extensions["nr_common_test_model"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(ext.service, service_id="nr_common_test_model")

    # Register indexer
    if hasattr(ext.service, "indexer"):
        iregistry = app.extensions["invenio-indexer"].registry
        iregistry.register(ext.service.indexer, indexer_id="nr_common_test_model")


def create_blueprint_from_app_nr_common_test_modelExt(app):
    """Create -ext blueprint."""
    blueprint = Blueprint(
        "nr_common_test_model-ext", __name__, url_prefix="nr_common_test_model"
    )
    blueprint.record_once(init_create_blueprint_from_app_nr_common_test_model)

    # calls record_once for all other functions starting with "init_app_addons_"
    # https://stackoverflow.com/questions/58785162/how-can-i-call-function-with-string-value-that-equals-to-function-name
    funcs = globals()
    funcs = [
        v
        for k, v in funcs.items()
        if k.startswith("init_app_addons_nr_common_test_model") and callable(v)
    ]
    for func in funcs:
        blueprint.record_once(func)

    return blueprint
