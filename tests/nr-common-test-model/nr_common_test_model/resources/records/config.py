import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig
from nr_common_test_model.resources.records.ui import NrCommonTestModelUIJSONSerializer


class NrCommonTestModelResourceConfig(RecordResourceConfig):
    """NrCommonTestModelRecord resource config."""

    blueprint_name = "NrCommonTestModel"
    url_prefix = "/nr-common-test-model/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.nr_common_test_model.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                NrCommonTestModelUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
