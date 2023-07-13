from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from invenio_records_resources.services.records.components import DataComponent
from nr_common_test_model.records.api import NrCommonTestModelRecord
from nr_common_test_model.services.records.permissions import (
    NrCommonTestModelPermissionPolicy,
)
from nr_common_test_model.services.records.search import NrCommonTestModelSearchOptions
from nr_metadata.common.services.records.schema import NRCommonRecordSchema
from oarepo_runtime.config.service import PermissionsPresetsConfigMixin


class NrCommonTestModelServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordServiceConfig
):
    """NrCommonTestModelRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-common-test-model/"

    base_permission_policy_cls = NrCommonTestModelPermissionPolicy

    schema = NRCommonRecordSchema

    search = NrCommonTestModelSearchOptions

    record_cls = NrCommonTestModelRecord

    service_id = "nr_common_test_model"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordServiceConfig.components,
        DataComponent,
    ]

    model = "nr_common_test_model"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{self.url_prefix}{?args*}"),
        }
