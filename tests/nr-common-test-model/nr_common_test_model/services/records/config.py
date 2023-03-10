from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import RecordServiceConfig
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from nr_common_test_model.records.api import NrCommonTestModelRecord
from nr_common_test_model.services.records.permissions import (
    NrCommonTestModelPermissionPolicy,
)
from nr_common_test_model.services.records.search import NrCommonTestModelSearchOptions
from nr_metadata.common.services.records.schema import NRCommonRecordSchema


class NrCommonTestModelServiceConfig(RecordServiceConfig):
    """NrCommonTestModelRecord service config."""

    url_prefix = "/nr-common-test-model/"

    permission_policy_cls = NrCommonTestModelPermissionPolicy

    schema = NRCommonRecordSchema

    search = NrCommonTestModelSearchOptions

    record_cls = NrCommonTestModelRecord
    # todo should i leave this here?
    service_id = "nr_common_test_model"

    components = [*RecordServiceConfig.components]

    model = "nr_common_test_model"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return pagination_links("{self.url_prefix}{?args*}")
