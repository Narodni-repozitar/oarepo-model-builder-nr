from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import RecordServiceConfig
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from nr_documents_test_model.records.api import NrDocumentsTestModelRecord
from nr_documents_test_model.services.records.permissions import (
    NrDocumentsTestModelPermissionPolicy,
)
from nr_documents_test_model.services.records.search import (
    NrDocumentsTestModelSearchOptions,
)
from nr_metadata.documents.services.records.schema import NRDocumentRecordSchema


class NrDocumentsTestModelServiceConfig(RecordServiceConfig):
    """NrDocumentsTestModelRecord service config."""

    url_prefix = "/nr-documents-test-model/"

    permission_policy_cls = NrDocumentsTestModelPermissionPolicy

    schema = NRDocumentRecordSchema

    search = NrDocumentsTestModelSearchOptions

    record_cls = NrDocumentsTestModelRecord
    service_id = "nr_documents_test_model"

    components = [*RecordServiceConfig.components]

    model = "nr_documents_test_model"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return pagination_links("{self.url_prefix}{?args*}")
