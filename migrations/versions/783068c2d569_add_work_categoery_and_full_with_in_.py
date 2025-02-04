"""add work categoery and full_with in work model

Revision ID: 783068c2d569
Revises: b3bfea9c1dfd
Create Date: 2024-12-12 11:06:20.152670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '783068c2d569'
down_revision = 'b3bfea9c1dfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.add_column(sa.Column('work_category', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('full_width', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.drop_column('full_width')
        batch_op.drop_column('work_category')

    # ### end Alembic commands ###
