from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Entity(Base):
    __tablename__ = 'entity'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    identifier = Column(String)
    keycloak_group_id = Column(String) # Reference to keycloak group
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True))
