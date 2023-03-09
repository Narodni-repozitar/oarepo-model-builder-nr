import marshmallow as ma
from edtf import Date as EDTFDate
from edtf import Interval as EDTFInterval
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import ValidationError
from marshmallow import fields as ma_fields
from marshmallow import validate as ma_validate
from marshmallow_utils import fields as mu_fields
from marshmallow_utils import schemas as mu_schemas
from nr_common.services.records.ui_schema import (
    AdditionalTitlesUISchema,
    NRAccessRightsVocabularyUISchema,
    NRAffiliationVocabularyUISchema,
    NRAuthorityIdentifierUISchema,
    NRAuthorityUIUISchema,
    NRAuthorityVocabularyUISchema,
    NRCommonMetadataUISchema,
    NRCountryVocabularyUISchema,
    NREventUISchema,
    NRExternalLocationUISchema,
    NRFunderVocabularyUISchema,
    NRFundingReferenceUISchema,
    NRGeoLocationPointUISchema,
    NRGeoLocationUISchema,
    NRItemRelationTypeVocabularyUISchema,
    NRLanguageVocabularyUISchema,
    NRLocationUISchema,
    NRObjectPIDUISchema,
    NRRelatedItemUISchema,
    NRResourceTypeVocabularyUISchema,
    NRSeriesUISchema,
    NRSubjectCategoryVocabularyUISchema,
    NRSubjectUISchema,
    NRSystemIdentifierUISchema,
)
from oarepo_runtime.ui import marshmallow as l10n
from oarepo_runtime.validation import validate_date


class NrCommonTestModelUISchema(ma.Schema):
    """NrCommonTestModelUISchema schema."""

    metadata = ma_fields.Nested(lambda: NRCommonMetadataUISchema())
