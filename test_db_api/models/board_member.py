"""
Модель участника доски (Many-to-Many связь).
"""

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class BoardMember(Base):
    """Участник доски"""

    __tablename__ = "board_members"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    board_id = Column(Integer, ForeignKey("boards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    board = relationship("Board", back_populates="members")
    user = relationship("User", back_populates="board_memberships")
