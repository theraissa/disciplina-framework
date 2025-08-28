from sqlalchemy import Column, DateTime, String, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Log(Base):
    __tablename__ = 'log'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    timestamp = Column(BigInteger, nullable=False)
    keycloak_user_id = Column(String) #User who perfomed the action
    entity_id = Column(UUID(as_uuid=True), ForeignKey("entity.id"), nullable=False)
    action = Column(String) #the operation ID, e.g. 'create'
    target_resource_id = Column(String) #ID of the affecte resource
    target_resource_type = Column(String) #table affected by this action
    message = Column(String. nullable=False) #human-readable details
    tag = Column(String, nullable=False)
    metadata = Column(JSON) #Request/response payload, etc
