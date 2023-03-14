from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_vocabularies.records.api import Vocabulary
from nr_common_test_model.records.dumper import NrCommonTestModelDumper
from nr_common_test_model.records.models import NrCommonTestModelMetadata
from nr_common_test_model.records.multilingual_dumper import MultilingualDumper
from oarepo_runtime.relations import InternalRelation, PIDRelation, RelationsField


class NrCommonTestModelRecord(Record):
    model_cls = NrCommonTestModelMetadata

    schema = ConstantField(
        "$schema", "http://localhost/schemas/nr_common_test_model-1.0.0.json"
    )

    index = IndexField("nr_common_test_model-nr_common_test_model-1.0.0")

    pid = PIDField(
        create=True, provider=RecordIdProviderV2, context_cls=PIDFieldContext
    )

    dumper_extensions = [MultilingualDumper()]
    dumper = NrCommonTestModelDumper(extensions=dumper_extensions)

    relations = RelationsField(
        affiliations_item=PIDRelation(
            "metadata.creators.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        role=PIDRelation(
            "metadata.contributors.role",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-roles"),
        ),
        affiliations_item_1=PIDRelation(
            "metadata.contributors.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        resourceType=PIDRelation(
            "metadata.resourceType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("resource-types"),
        ),
        subjectCategories_item=PIDRelation(
            "metadata.subjectCategories",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("subject-categories"),
        ),
        languages_item=PIDRelation(
            "metadata.languages",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("languages"),
        ),
        rights_item=PIDRelation(
            "metadata.rights",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("access-rights"),
        ),
        accessRights=PIDRelation(
            "metadata.accessRights",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("access-rights"),
        ),
        affiliations_item_2=PIDRelation(
            "metadata.relatedItems.itemCreators.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        role_1=PIDRelation(
            "metadata.relatedItems.itemContributors.role",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-roles"),
        ),
        affiliations_item_3=PIDRelation(
            "metadata.relatedItems.itemContributors.affiliations",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        itemRelationType=PIDRelation(
            "metadata.relatedItems.itemRelationType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("item-relation-types"),
        ),
        itemResourceType=PIDRelation(
            "metadata.relatedItems.itemResourceType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("resource-types"),
        ),
        funder=PIDRelation(
            "metadata.fundingReferences.funder",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("funders"),
        ),
        country=PIDRelation(
            "metadata.events.eventLocation.country",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("countries"),
        ),
    )
