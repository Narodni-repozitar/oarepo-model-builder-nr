from invenio_db import db
from invenio_records.models import RecordMetadataBase


class NrCommonTestModelMetadata(db.Model, RecordMetadataBase):
    """Model for NrCommonTestModelRecord metadata."""

    __tablename__ = "nrcommontestmodel_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
