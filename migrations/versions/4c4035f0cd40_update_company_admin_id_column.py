"""Update Company admin_id Column

Revision ID: 4c4035f0cd40
Revises: e12f2a32e868
Create Date: 2024-03-19 14:00:37.395766

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4c4035f0cd40'
down_revision = 'e12f2a32e868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.alter_column('admin_id',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.alter_column('admin_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
