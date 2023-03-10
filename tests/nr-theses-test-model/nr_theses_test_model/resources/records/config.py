import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig
from nr_theses_test_model.resources.records.ui import NrThesesTestModelUIJSONSerializer


class NrThesesTestModelResourceConfig(RecordResourceConfig):
    """NrThesesTestModelRecord resource config."""

    blueprint_name = "NrThesesTestModel"
    url_prefix = "/nr-theses-test-model/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.nr_theses_test_model.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                NrThesesTestModelUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
