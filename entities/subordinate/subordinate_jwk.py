from sqlalchemy import Column, DateTime, String, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class SubordinateJwk(Base):
    __tablename__ = 'subordinate_jwk'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    subordinate_id = Column(UUID(as_uuid=True), ForeignKey("subordinate.id"), nullable=False)
    key = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True))
