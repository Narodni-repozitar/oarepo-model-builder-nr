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
from marshmallow_utils.fields import edtfdatestring as mu_fields_edtf
from nr_metadata.common.services.records.schema import (
    AdditionalTitlesSchema,
    NRAccessRightsVocabularySchema,
    NRAffiliationVocabularySchema,
    NRAuthorityRoleVocabularySchema,
    NRAuthoritySchema,
    NRContributorSchema,
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
    NRRelatedItemSchema,
    NRResourceTypeVocabularySchema,
    NRSeriesSchema,
    NRSubjectCategoryVocabularySchema,
    NRSubjectSchema,
)
from nr_metadata.schema.identifiers import (
    NRAuthorityIdentifierSchema,
    NRObjectIdentifierSchema,
    NRSystemIdentifierSchema,
)
from oarepo_runtime.i18n.schema import MultilingualSchema
from oarepo_runtime.ui import marshmallow as l10n
from oarepo_runtime.validation import validate_date
from oarepo_vocabularies.services.schemas import HierarchySchema


class NRDegreeGrantorSchema(ma.Schema):
    """NRDegreeGrantorSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    hierarchy = ma_fields.Nested(lambda: HierarchySchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRThesisSchema(ma.Schema):
    """NRThesisSchema schema."""

    dateDefended = ma_fields.String(validate=[validate_date("%Y-%m-%d")])
    defended = ma_fields.Boolean()
    degreeGrantor = ma_fields.Nested(lambda: NRDegreeGrantorSchema())
    studyFields = ma_fields.List(ma_fields.String())


class NRDocumentMetadataSchema(ma.Schema):
    """NRDocumentMetadataSchema schema."""

    thesis = ma_fields.Nested(lambda: NRThesisSchema())
    collection = ma_fields.String()
    title = ma_fields.String()
    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesSchema())
    )
    creators = ma_fields.List(ma_fields.Nested(lambda: NRAuthoritySchema()))
    contributors = ma_fields.List(ma_fields.Nested(lambda: NRContributorSchema()))
    resourceType = ma_fields.Nested(lambda: NRResourceTypeVocabularySchema())
    dateAvailable = ma_fields.String(
        validate=[mu_fields_edtf.EDTFValidator(types=(EDTFDate,))]
    )
    dateModified = ma_fields.String(
        validate=[mu_fields_edtf.EDTFValidator(types=(EDTFDate,))]
    )
    subjects = ma_fields.List(ma_fields.Nested(lambda: NRSubjectSchema()))
    publishers = ma_fields.List(ma_fields.String())
    subjectCategories = ma_fields.List(
        ma_fields.Nested(lambda: NRSubjectCategoryVocabularySchema())
    )
    languages = ma_fields.List(ma_fields.Nested(lambda: NRLanguageVocabularySchema()))
    notes = ma_fields.List(ma_fields.String())
    abstract = ma_fields.List(ma_fields.Nested(lambda: MultilingualSchema()))
    methods = ma_fields.List(ma_fields.Nested(lambda: MultilingualSchema()))
    technicalInfo = ma_fields.List(ma_fields.Nested(lambda: MultilingualSchema()))
    rights = ma_fields.List(ma_fields.Nested(lambda: NRAccessRightsVocabularySchema()))
    accessRights = ma_fields.Nested(lambda: NRAccessRightsVocabularySchema())
    relatedItems = ma_fields.List(ma_fields.Nested(lambda: NRRelatedItemSchema()))
    fundingReferences = ma_fields.List(
        ma_fields.Nested(lambda: NRFundingReferenceSchema())
    )
    version = ma_fields.String()
    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationSchema()))
    accessibility = ma_fields.List(ma_fields.Nested(lambda: MultilingualSchema()))
    series = ma_fields.List(ma_fields.Nested(lambda: NRSeriesSchema()))
    externalLocation = ma_fields.Nested(lambda: NRExternalLocationSchema())
    originalRecord = ma_fields.String()
    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierSchema())
    )
    systemIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRSystemIdentifierSchema())
    )
    events = ma_fields.List(ma_fields.Nested(lambda: NREventSchema()))


class NRDocumentRecordSchema(InvenioBaseRecordSchema):
    """NRDocumentRecordSchema schema."""

    metadata = ma_fields.Nested(lambda: NRDocumentMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
