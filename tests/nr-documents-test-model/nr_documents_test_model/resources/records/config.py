import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig
from nr_documents_test_model.resources.records.ui import (
    NrDocumentsTestModelUIJSONSerializer,
)


class NrDocumentsTestModelResourceConfig(RecordResourceConfig):
    """NrDocumentsTestModelRecord resource config."""

    blueprint_name = "nr_documents_test_model"
    url_prefix = "/nr-documents-test-model/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.nr_documents_test_model.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                NrDocumentsTestModelUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
