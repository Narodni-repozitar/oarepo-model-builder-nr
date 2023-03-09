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
from nr_common.services.records.schema import (
    AdditionalTitlesSchema,
    NRAccessRightsVocabularySchema,
    NRAffiliationVocabularySchema,
    NRAuthorityIdentifierSchema,
    NRAuthoritySchema,
    NRAuthorityVocabularySchema,
    NRCommonMetadataSchema,
    NRCommonRecordSchema,
    NRCountryVocabularySchema,
    NREventSchema,
    NRExternalLocationSchema,
    NRFunderVocabularySchema,
    NRFundingReferenceSchema,
    NRGeoLocationPointSchema,
    NRGeoLocationSchema,
    NRItemRelationTypeVocabularySchema,
    NRLanguageVocabularySchema,
    NRLocationSchema,
    NRObjectPIDSchema,
    NRRelatedItemSchema,
    NRResourceTypeVocabularySchema,
    NRSeriesSchema,
    NRSubjectCategoryVocabularySchema,
    NRSubjectSchema,
    NRSystemIdentifierSchema,
)
from oarepo_runtime.ui import marshmallow as l10n
from oarepo_runtime.validation import validate_date


class NrCommonTestModelSchema(NRCommonRecordSchema):
    """NrCommonTestModelSchema schema."""

    metadata = ma_fields.Nested(lambda: NRCommonMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
