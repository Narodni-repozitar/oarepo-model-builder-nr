from invenio_db import db
from invenio_records.models import RecordMetadataBase


class NrDocumentsTestModelMetadata(db.Model, RecordMetadataBase):
    """Model for NrDocumentsTestModelRecord metadata."""

    __tablename__ = "nrdocumentstestmodel_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
