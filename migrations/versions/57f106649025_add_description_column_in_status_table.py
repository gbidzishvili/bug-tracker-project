"""Add description column in Status Table

Revision ID: 57f106649025
Revises: e4877e8ead6f
Create Date: 2024-04-01 12:16:59.148486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57f106649025'
down_revision = 'e4877e8ead6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('status', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('status', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###