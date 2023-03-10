"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from invenio_search.engine import dsl
from oarepo_runtime.facets.nested_facet import NestedLabeledFacet

metadata_thesis_dateDefended = TermsFacet(field="metadata.thesis.dateDefended")


metadata_thesis_defended = TermsFacet(field="metadata.thesis.defended")


metadata_thesis_degreeGrantor_id = TermsFacet(field="metadata.thesis.degreeGrantor.id")


metadata_thesis_degreeGrantor_hierarchy_parent = TermsFacet(
    field="metadata.thesis.degreeGrantor.hierarchy.parent"
)


metadata_thesis_degreeGrantor_hierarchy_level = TermsFacet(
    field="metadata.thesis.degreeGrantor.hierarchy.level"
)


metadata_thesis_degreeGrantor_hierarchy_ancestors = TermsFacet(
    field="metadata.thesis.degreeGrantor.hierarchy.ancestors"
)


metadata_thesis_degreeGrantor__version = TermsFacet(
    field="metadata.thesis.degreeGrantor.@v"
)


metadata_thesis_studyFields = TermsFacet(field="metadata.thesis.studyFields")


metadata_collection = TermsFacet(field="metadata.collection")


metadata_title_keyword = TermsFacet(field="metadata.title.keyword")


metadata_additionalTitles_title_lang = NestedLabeledFacet(
    path="metadata.additionalTitles.title",
    nested_facet=TermsFacet(field="metadata.additionalTitles.title.lang"),
)


metadata_additionalTitles_title_value_keyword = NestedLabeledFacet(
    path="metadata.additionalTitles.title",
    nested_facet=TermsFacet(field="metadata.additionalTitles.title.value.keyword"),
)


metadata_additionalTitles_titleType = TermsFacet(
    field="metadata.additionalTitles.titleType"
)


metadata_creators_affiliations_id = TermsFacet(
    field="metadata.creators.affiliations.id"
)


metadata_creators_affiliations__version = TermsFacet(
    field="metadata.creators.affiliations.@v"
)


metadata_creators_nameType = TermsFacet(field="metadata.creators.nameType")


metadata_creators_fullName = TermsFacet(field="metadata.creators.fullName")


metadata_creators_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.creators.authorityIdentifiers.identifier"
)


metadata_creators_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.creators.authorityIdentifiers.scheme"
)


metadata_contributors_role_id = TermsFacet(field="metadata.contributors.role.id")


metadata_contributors_role__version = TermsFacet(field="metadata.contributors.role.@v")


metadata_contributors_affiliations_id = TermsFacet(
    field="metadata.contributors.affiliations.id"
)


metadata_contributors_affiliations__version = TermsFacet(
    field="metadata.contributors.affiliations.@v"
)


metadata_contributors_nameType = TermsFacet(field="metadata.contributors.nameType")


metadata_contributors_fullName = TermsFacet(field="metadata.contributors.fullName")


metadata_contributors_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.contributors.authorityIdentifiers.identifier"
)


metadata_contributors_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.contributors.authorityIdentifiers.scheme"
)


metadata_resourceType_id = TermsFacet(field="metadata.resourceType.id")


metadata_resourceType__version = TermsFacet(field="metadata.resourceType.@v")


metadata_dateAvailable = TermsFacet(field="metadata.dateAvailable")


metadata_dateModified = TermsFacet(field="metadata.dateModified")


metadata_subjects_subjectScheme = TermsFacet(field="metadata.subjects.subjectScheme")


metadata_subjects_subject_lang = NestedLabeledFacet(
    path="metadata.subjects.subject",
    nested_facet=TermsFacet(field="metadata.subjects.subject.lang"),
)


metadata_subjects_subject_value_keyword = NestedLabeledFacet(
    path="metadata.subjects.subject",
    nested_facet=TermsFacet(field="metadata.subjects.subject.value.keyword"),
)


metadata_subjects_valueURI = TermsFacet(field="metadata.subjects.valueURI")


metadata_subjects_classificationCode = TermsFacet(
    field="metadata.subjects.classificationCode"
)


metadata_subjectCategories_id = TermsFacet(field="metadata.subjectCategories.id")


metadata_subjectCategories__version = TermsFacet(field="metadata.subjectCategories.@v")


metadata_languages_id = TermsFacet(field="metadata.languages.id")


metadata_languages__version = TermsFacet(field="metadata.languages.@v")


metadata_abstract_lang = NestedLabeledFacet(
    path="metadata.abstract", nested_facet=TermsFacet(field="metadata.abstract.lang")
)


metadata_abstract_value_keyword = NestedLabeledFacet(
    path="metadata.abstract",
    nested_facet=TermsFacet(field="metadata.abstract.value.keyword"),
)


metadata_methods_lang = NestedLabeledFacet(
    path="metadata.methods", nested_facet=TermsFacet(field="metadata.methods.lang")
)


metadata_methods_value_keyword = NestedLabeledFacet(
    path="metadata.methods",
    nested_facet=TermsFacet(field="metadata.methods.value.keyword"),
)


metadata_technicalInfo_lang = NestedLabeledFacet(
    path="metadata.technicalInfo",
    nested_facet=TermsFacet(field="metadata.technicalInfo.lang"),
)


metadata_technicalInfo_value_keyword = NestedLabeledFacet(
    path="metadata.technicalInfo",
    nested_facet=TermsFacet(field="metadata.technicalInfo.value.keyword"),
)


metadata_rights_id = TermsFacet(field="metadata.rights.id")


metadata_rights__version = TermsFacet(field="metadata.rights.@v")


metadata_accessRights_id = TermsFacet(field="metadata.accessRights.id")


metadata_accessRights__version = TermsFacet(field="metadata.accessRights.@v")


metadata_relatedItems_itemCreators_affiliations_id = TermsFacet(
    field="metadata.relatedItems.itemCreators.affiliations.id"
)


metadata_relatedItems_itemCreators_affiliations__version = TermsFacet(
    field="metadata.relatedItems.itemCreators.affiliations.@v"
)


metadata_relatedItems_itemCreators_nameType = TermsFacet(
    field="metadata.relatedItems.itemCreators.nameType"
)


metadata_relatedItems_itemCreators_fullName = TermsFacet(
    field="metadata.relatedItems.itemCreators.fullName"
)


metadata_relatedItems_itemCreators_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.relatedItems.itemCreators.authorityIdentifiers.identifier"
)


metadata_relatedItems_itemCreators_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.relatedItems.itemCreators.authorityIdentifiers.scheme"
)


metadata_relatedItems_itemContributors_role_id = TermsFacet(
    field="metadata.relatedItems.itemContributors.role.id"
)


metadata_relatedItems_itemContributors_role__version = TermsFacet(
    field="metadata.relatedItems.itemContributors.role.@v"
)


metadata_relatedItems_itemContributors_affiliations_id = TermsFacet(
    field="metadata.relatedItems.itemContributors.affiliations.id"
)


metadata_relatedItems_itemContributors_affiliations__version = TermsFacet(
    field="metadata.relatedItems.itemContributors.affiliations.@v"
)


metadata_relatedItems_itemContributors_nameType = TermsFacet(
    field="metadata.relatedItems.itemContributors.nameType"
)


metadata_relatedItems_itemContributors_fullName = TermsFacet(
    field="metadata.relatedItems.itemContributors.fullName"
)


metadata_relatedItems_itemContributors_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.relatedItems.itemContributors.authorityIdentifiers.identifier"
)


metadata_relatedItems_itemContributors_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.relatedItems.itemContributors.authorityIdentifiers.scheme"
)


metadata_relatedItems_itemPIDs_identifier = TermsFacet(
    field="metadata.relatedItems.itemPIDs.identifier"
)


metadata_relatedItems_itemPIDs_scheme = TermsFacet(
    field="metadata.relatedItems.itemPIDs.scheme"
)


metadata_relatedItems_itemURL = TermsFacet(field="metadata.relatedItems.itemURL")


metadata_relatedItems_itemYear = TermsFacet(field="metadata.relatedItems.itemYear")


metadata_relatedItems_itemVolume = TermsFacet(field="metadata.relatedItems.itemVolume")


metadata_relatedItems_itemIssue = TermsFacet(field="metadata.relatedItems.itemIssue")


metadata_relatedItems_itemStartPage = TermsFacet(
    field="metadata.relatedItems.itemStartPage"
)


metadata_relatedItems_itemEndPage = TermsFacet(
    field="metadata.relatedItems.itemEndPage"
)


metadata_relatedItems_itemPublisher = TermsFacet(
    field="metadata.relatedItems.itemPublisher"
)


metadata_relatedItems_itemRelationType_id = TermsFacet(
    field="metadata.relatedItems.itemRelationType.id"
)


metadata_relatedItems_itemRelationType__version = TermsFacet(
    field="metadata.relatedItems.itemRelationType.@v"
)


metadata_relatedItems_itemResourceType_id = TermsFacet(
    field="metadata.relatedItems.itemResourceType.id"
)


metadata_relatedItems_itemResourceType__version = TermsFacet(
    field="metadata.relatedItems.itemResourceType.@v"
)


metadata_fundingReferences_projectID = TermsFacet(
    field="metadata.fundingReferences.projectID"
)


metadata_fundingReferences_funder_id = TermsFacet(
    field="metadata.fundingReferences.funder.id"
)


metadata_fundingReferences_funder__version = TermsFacet(
    field="metadata.fundingReferences.funder.@v"
)


metadata_version = TermsFacet(field="metadata.version")


metadata_geoLocations_geoLocationPlace = TermsFacet(
    field="metadata.geoLocations.geoLocationPlace"
)


metadata_geoLocations_geoLocationPoint_pointLongitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPoint.pointLongitude"
)


metadata_geoLocations_geoLocationPoint_pointLatitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPoint.pointLatitude"
)


metadata_accessibility_lang = NestedLabeledFacet(
    path="metadata.accessibility",
    nested_facet=TermsFacet(field="metadata.accessibility.lang"),
)


metadata_accessibility_value_keyword = NestedLabeledFacet(
    path="metadata.accessibility",
    nested_facet=TermsFacet(field="metadata.accessibility.value.keyword"),
)


metadata_series_seriesTitle = TermsFacet(field="metadata.series.seriesTitle")


metadata_series_seriesVolume = TermsFacet(field="metadata.series.seriesVolume")


metadata_externalLocation_externalLocationURL = TermsFacet(
    field="metadata.externalLocation.externalLocationURL"
)


metadata_originalRecord = TermsFacet(field="metadata.originalRecord")


metadata_objectIdentifiers_identifier = TermsFacet(
    field="metadata.objectIdentifiers.identifier"
)


metadata_objectIdentifiers_scheme = TermsFacet(
    field="metadata.objectIdentifiers.scheme"
)


metadata_systemIdentifiers_identifier = TermsFacet(
    field="metadata.systemIdentifiers.identifier"
)


metadata_systemIdentifiers_scheme = TermsFacet(
    field="metadata.systemIdentifiers.scheme"
)


metadata_events_eventDate = TermsFacet(field="metadata.events.eventDate")


metadata_events_eventLocation_place = TermsFacet(
    field="metadata.events.eventLocation.place"
)


metadata_events_eventLocation_country_id = TermsFacet(
    field="metadata.events.eventLocation.country.id"
)


metadata_events_eventLocation_country__version = TermsFacet(
    field="metadata.events.eventLocation.country.@v"
)


_id = TermsFacet(field="id")


created = TermsFacet(field="created")


updated = TermsFacet(field="updated")


_schema = TermsFacet(field="$schema")
