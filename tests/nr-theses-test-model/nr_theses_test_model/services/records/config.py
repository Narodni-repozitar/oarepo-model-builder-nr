from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import RecordServiceConfig
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from nr_metadata.theses.services.records.schema import NRThesesRecordSchema
from nr_theses_test_model.records.api import NrThesesTestModelRecord
from nr_theses_test_model.services.records.permissions import (
    NrThesesTestModelPermissionPolicy,
)
from nr_theses_test_model.services.records.search import NrThesesTestModelSearchOptions


class NrThesesTestModelServiceConfig(RecordServiceConfig):
    """NrThesesTestModelRecord service config."""

    url_prefix = "/nr-theses-test-model/"

    permission_policy_cls = NrThesesTestModelPermissionPolicy

    schema = NRThesesRecordSchema

    search = NrThesesTestModelSearchOptions

    record_cls = NrThesesTestModelRecord
    # todo should i leave this here?
    service_id = "nr_theses_test_model"

    components = [*RecordServiceConfig.components]

    model = "nr_theses_test_model"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return pagination_links("{self.url_prefix}{?args*}")
