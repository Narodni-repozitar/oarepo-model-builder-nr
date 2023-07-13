import marshmallow as ma
from edtf import Date as EDTFDate
from edtf import Interval as EDTFInterval
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import validate as ma_validate
from marshmallow_utils.fields import TrimmedString
from nr_metadata.schema.identifiers import (
    NRAuthorityIdentifierSchema,
    NRObjectIdentifierSchema,
    NRSystemIdentifierSchema,
)
from oarepo_runtime.i18n.schema import I18nStrField, MultilingualField
from oarepo_runtime.validation import CachedMultilayerEDTFValidator
from oarepo_vocabularies.services.schema import HierarchySchema


class NRCommonRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: NRCommonMetadataSchema())


class NRCommonMetadataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    abstract = MultilingualField(I18nStrField())

    accessRights = ma.fields.Nested(lambda: NRAccessRightsVocabularySchema())

    accessibility = MultilingualField(I18nStrField())

    additionalTitles = ma.fields.List(
        ma.fields.Nested(lambda: AdditionalTitlesSchema())
    )

    contributors = ma.fields.List(ma.fields.Nested(lambda: NRContributorSchema()))

    creators = ma.fields.List(
        ma.fields.Nested(lambda: NRAuthoritySchema()), required=True
    )

    dateAvailable = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFDate,))]
    )

    dateModified = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFDate,))]
    )

    events = ma.fields.List(ma.fields.Nested(lambda: NREventSchema()))

    externalLocation = ma.fields.Nested(lambda: NRExternalLocationSchema())

    fundingReferences = ma.fields.List(
        ma.fields.Nested(lambda: NRFundingReferenceSchema())
    )

    geoLocations = ma.fields.List(ma.fields.Nested(lambda: NRGeoLocationSchema()))

    languages = ma.fields.List(
        ma.fields.Nested(lambda: NRLanguageVocabularySchema()), required=True
    )

    methods = MultilingualField(I18nStrField())

    notes = ma.fields.List(ma.fields.String())

    objectIdentifiers = ma.fields.List(
        ma.fields.Nested(lambda: NRObjectIdentifierSchema())
    )

    originalRecord = ma.fields.String()

    publishers = ma.fields.List(ma.fields.String())

    relatedItems = ma.fields.List(ma.fields.Nested(lambda: NRRelatedItemSchema()))

    resourceType = ma.fields.Nested(
        lambda: NRResourceTypeVocabularySchema(), required=True
    )

    rights = ma.fields.List(ma.fields.Nested(lambda: NRLicenseVocabularySchema()))

    series = ma.fields.List(ma.fields.Nested(lambda: NRSeriesSchema()))

    subjectCategories = ma.fields.List(
        ma.fields.Nested(lambda: NRSubjectCategoryVocabularySchema())
    )

    subjects = ma.fields.List(ma.fields.Nested(lambda: NRSubjectSchema()))

    systemIdentifiers = ma.fields.List(
        ma.fields.Nested(lambda: NRSystemIdentifierSchema())
    )

    technicalInfo = MultilingualField(I18nStrField())

    title = ma.fields.String(required=True)

    version = ma.fields.String()


class NREventSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    eventDate = TrimmedString(
        required=True, validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    eventLocation = ma.fields.Nested(lambda: NRLocationSchema(), required=True)

    eventNameAlternate = ma.fields.List(ma.fields.String())

    eventNameOriginal = ma.fields.String(required=True)


class NRRelatedItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma.fields.List(
        ma.fields.Nested(lambda: ItemContributorsItemNRAuthoritySchema())
    )

    itemCreators = ma.fields.List(ma.fields.Nested(lambda: NRAuthoritySchema()))

    itemEndPage = ma.fields.String()

    itemIssue = ma.fields.String()

    itemPIDs = ma.fields.List(ma.fields.Nested(lambda: NRObjectIdentifierSchema()))

    itemPublisher = ma.fields.String()

    itemRelationType = ma.fields.Nested(lambda: NRItemRelationTypeVocabularySchema())

    itemResourceType = ma.fields.Nested(lambda: NRResourceTypeVocabularySchema())

    itemStartPage = ma.fields.String()

    itemTitle = ma.fields.String(required=True)

    itemURL = ma.fields.String()

    itemVolume = ma.fields.String()

    itemYear = ma.fields.Integer()


class ItemContributorsItemNRAuthoritySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma.fields.List(
        ma.fields.Nested(lambda: NRAffiliationVocabularySchema())
    )

    authorityIdentifiers = ma.fields.List(
        ma.fields.Nested(lambda: NRAuthorityIdentifierSchema())
    )

    fullName = ma.fields.String(required=True)

    nameType = ma.fields.String(
        validate=[ma_validate.OneOf(["Organizational", "Personal"])]
    )

    role = ma.fields.Nested(lambda: NRAuthorityRoleVocabularySchema())


class NRAuthoritySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma.fields.List(
        ma.fields.Nested(lambda: NRAffiliationVocabularySchema())
    )

    authorityIdentifiers = ma.fields.List(
        ma.fields.Nested(lambda: NRAuthorityIdentifierSchema())
    )

    fullName = ma.fields.String(required=True)

    nameType = ma.fields.String(
        validate=[ma_validate.OneOf(["Organizational", "Personal"])]
    )


class NRContributorSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma.fields.List(
        ma.fields.Nested(lambda: NRAffiliationVocabularySchema())
    )

    authorityIdentifiers = ma.fields.List(
        ma.fields.Nested(lambda: NRAuthorityIdentifierSchema())
    )

    fullName = ma.fields.String(required=True)

    nameType = ma.fields.String(
        validate=[ma_validate.OneOf(["Organizational", "Personal"])]
    )

    role = ma.fields.Nested(lambda: NRAuthorityRoleVocabularySchema())


class NRFundingReferenceSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    funder = ma.fields.Nested(lambda: NRFunderVocabularySchema())

    fundingProgram = ma.fields.String()

    projectID = ma.fields.String(required=True)

    projectName = ma.fields.String()


class NRGeoLocationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    geoLocationPlace = ma.fields.String(required=True)

    geoLocationPoint = ma.fields.Nested(lambda: NRGeoLocationPointSchema())


class NRLocationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    country = ma.fields.Nested(lambda: NRCountryVocabularySchema())

    place = ma.fields.String(required=True)


class AdditionalTitlesSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    title = I18nStrField(required=True)

    titleType = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["translatedTitle", "alternativeTitle", "subtitle", "other"]
            )
        ],
    )


class NRAccessRightsVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRAffiliationVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    hierarchy = ma.fields.Nested(lambda: HierarchySchema())

    title = i18n_strings


class NRAuthorityRoleVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRCountryVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRExternalLocationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    externalLocationNote = ma.fields.String()

    externalLocationURL = ma.fields.String(required=True)


class NRFunderVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRGeoLocationPointSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    pointLatitude = ma.fields.Float(required=True)

    pointLongitude = ma.fields.Float(required=True)


class NRItemRelationTypeVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRLanguageVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRLicenseVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRResourceTypeVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRSeriesSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    seriesTitle = ma.fields.String(required=True)

    seriesVolume = ma.fields.String()


class NRSubjectCategoryVocabularySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRSubjectSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    classificationCode = ma.fields.String()

    subject = MultilingualField(I18nStrField(), required=True)

    subjectScheme = ma.fields.String()

    valueURI = ma.fields.String()
