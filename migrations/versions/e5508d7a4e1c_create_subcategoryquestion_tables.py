"""Create subcategoryquestion tables

Revision ID: e5508d7a4e1c
Revises: 8f2c615b9b07
Create Date: 2024-06-01 21:43:35.327599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5508d7a4e1c'
down_revision: Union[str, None] = '8f2c615b9b07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subcategory_question',
    sa.Column('subcategory_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['subcategory_id'], ['subcategories.id'], ),
    sa.PrimaryKeyConstraint('subcategory_id', 'question_id')
    )
    op.drop_constraint('subcategories_category_id_fkey', 'subcategories', type_='foreignkey')
    op.create_foreign_key(None, 'subcategories', 'categories', ['category_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subcategories', type_='foreignkey')
    op.create_foreign_key('subcategories_category_id_fkey', 'subcategories', 'users', ['category_id'], ['id'], ondelete='CASCADE')
    op.drop_table('subcategory_question')
    # ### end Alembic commands ###