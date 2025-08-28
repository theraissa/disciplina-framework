from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Jwk(Base):
    __tablename__ = 'jwk'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entity.id"), nullable=False)
    alg = Column(String)
    kid = Column(String)
    kms = Column(String, default='memory')
    kms_key_ref = Column(String, nullable=False)
    key = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    revoked_at = Column(DateTime(timezone=True))
    revoked_reason = Column(String)
