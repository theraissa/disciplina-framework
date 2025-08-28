from sqlalchemy import Column, DateTime, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class TrustMark(Base):
    __tablename__ = 'trust_mark'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entity.id"), nullable=False)
    trust_mark_type = Column(String, ForeignKey("trust_mark_type.id"), nullable=False)
    sub = Column(String, nullable=False)
    trust_mark_value = Column(String, nullable=False)
    iat = Column(Integer, nullable=False)
    exp = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True))
