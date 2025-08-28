from sqlalchemy import Column, DateTime, String, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class SubordinateStatement(Base):
    __tablename__ = 'subordinate_statement'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    subordinate_id = Column(UUID(as_uuid=True), ForeignKey("subordinate.id"), nullable=False)
    iss = Column(String, nullable=False)
    sub = Column(String, nullable=False)
    statement = Column(String, nullable=False)
    expires_at = Column(BigInteger, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
