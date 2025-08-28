from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class TrustMarkIssuer(Base):
    __tablename__ = 'trust_mark_issuer'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    trust_mark_type_id = Column(UUID(as_uuid=True), ForeignKey("trust_mark_type.id"), nullable=False)
    issuer_identifier = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True))
