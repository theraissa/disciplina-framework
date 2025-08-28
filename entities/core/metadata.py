from sqlalchemy import Column, DateTime, String, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Metadata(Base):
    __tablename__ = 'metadata'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entity.id"), nullable=False)
    key = Column(String, nullable=False)
    metadata = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True))
    
class MetadataPolicy(Base):
    __tablename__ = 'metadata_policy'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entity.id"), nullable=False)
    key = Column(String, nullable=False)
    policy = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True))