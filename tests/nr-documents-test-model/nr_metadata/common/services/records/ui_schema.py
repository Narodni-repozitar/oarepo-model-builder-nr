import marshmallow as ma
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
from nr_metadata.ui_schema.identifiers import (
    NRAuthorityIdentifierUISchema,
    NRObjectIdentifierUISchema,
)
from oarepo_runtime.i18n.schema import I18nUISchema
from oarepo_runtime.ui import marshmallow as l10n


class AdditionalTitlesUISchema(ma.Schema):
    """AdditionalTitlesUISchema schema."""

    title = ma_fields.Nested(lambda: I18nUISchema())
    titleType = l10n.LocalizedEnum(value_prefix="nr_documents_test_model")


class NRAffiliationVocabularyUISchema(ma.Schema):
    """NRAffiliationVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRAuthorityUIUISchema(ma.Schema):
    """NRAuthorityUIUISchema schema."""

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularyUISchema())
    )
    nameType = l10n.LocalizedEnum(value_prefix="nr_documents_test_model")
    fullName = ma_fields.String()
    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierUISchema())
    )


class NRAuthorityRoleVocabularyUISchema(ma.Schema):
    """NRAuthorityRoleVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRContributorUISchema(ma.Schema):
    """NRContributorUISchema schema."""

    role = ma_fields.Nested(lambda: NRAuthorityRoleVocabularyUISchema())
    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularyUISchema())
    )
    nameType = l10n.LocalizedEnum(value_prefix="nr_documents_test_model")
    fullName = ma_fields.String()
    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierUISchema())
    )


class NRResourceTypeVocabularyUISchema(ma.Schema):
    """NRResourceTypeVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRSubjectUISchema(ma.Schema):
    """NRSubjectUISchema schema."""

    subjectScheme = ma_fields.String()
    subject = ma_fields.List(ma_fields.Nested(lambda: I18nUISchema()))
    valueURI = ma_fields.String()
    classificationCode = ma_fields.String()


class NRSubjectCategoryVocabularyUISchema(ma.Schema):
    """NRSubjectCategoryVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRLanguageVocabularyUISchema(ma.Schema):
    """NRLanguageVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRLicenseVocabularyUISchema(ma.Schema):
    """NRLicenseVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRAccessRightsVocabularyUISchema(ma.Schema):
    """NRAccessRightsVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRItemRelationTypeVocabularyUISchema(ma.Schema):
    """NRItemRelationTypeVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRRelatedItemUISchema(ma.Schema):
    """NRRelatedItemUISchema schema."""

    itemTitle = ma_fields.String()
    itemCreators = ma_fields.List(ma_fields.Nested(lambda: NRAuthorityUIUISchema()))
    itemContributors = ma_fields.List(ma_fields.Nested(lambda: NRAuthorityUIUISchema()))
    itemPIDs = ma_fields.List(ma_fields.Nested(lambda: NRObjectIdentifierUISchema()))
    itemURL = ma_fields.String()
    itemYear = ma_fields.Integer()
    itemVolume = ma_fields.String()
    itemIssue = ma_fields.String()
    itemStartPage = ma_fields.String()
    itemEndPage = ma_fields.String()
    itemPublisher = ma_fields.String()
    itemRelationType = ma_fields.Nested(lambda: NRItemRelationTypeVocabularyUISchema())
    itemResourceType = ma_fields.Nested(lambda: NRResourceTypeVocabularyUISchema())


class NRFunderVocabularyUISchema(ma.Schema):
    """NRFunderVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRFundingReferenceUISchema(ma.Schema):
    """NRFundingReferenceUISchema schema."""

    projectID = ma_fields.String()
    projectName = ma_fields.String()
    fundingProgram = ma_fields.String()
    funder = ma_fields.Nested(lambda: NRFunderVocabularyUISchema())


class NRGeoLocationPointUISchema(ma.Schema):
    """NRGeoLocationPointUISchema schema."""

    pointLongitude = ma_fields.Float()
    pointLatitude = ma_fields.Float()


class NRGeoLocationUISchema(ma.Schema):
    """NRGeoLocationUISchema schema."""

    geoLocationPlace = ma_fields.String()
    geoLocationPoint = ma_fields.Nested(lambda: NRGeoLocationPointUISchema())


class NRSeriesUISchema(ma.Schema):
    """NRSeriesUISchema schema."""

    seriesTitle = ma_fields.String()
    seriesVolume = ma_fields.String()


class NRExternalLocationUISchema(ma.Schema):
    """NRExternalLocationUISchema schema."""

    externalLocationURL = ma_fields.String()
    externalLocationNote = ma_fields.String()


class NRCountryVocabularyUISchema(ma.Schema):
    """NRCountryVocabularyUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = i18n_strings
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NRLocationUISchema(ma.Schema):
    """NRLocationUISchema schema."""

    place = ma_fields.String()
    country = ma_fields.Nested(lambda: NRCountryVocabularyUISchema())


class NREventUISchema(ma.Schema):
    """NREventUISchema schema."""

    eventNameOriginal = ma_fields.String()
    eventNameAlternate = ma_fields.List(ma_fields.String())
    eventDate = l10n.LocalizedEDTFInterval()
    eventLocation = ma_fields.Nested(lambda: NRLocationUISchema())
