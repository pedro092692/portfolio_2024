"""add position to work model

Revision ID: 197e31529d00
Revises: 783068c2d569
Create Date: 2024-12-19 22:59:46.324474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '197e31529d00'
down_revision = '783068c2d569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.add_column(sa.Column('position', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.drop_column('position')

    # ### end Alembic commands ###