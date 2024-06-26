"""Add Severity Table

Revision ID: 079ac37a448e
Revises: ec03d65a5772
Create Date: 2024-04-01 12:09:24.642998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079ac37a448e'
down_revision = 'ec03d65a5772'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('severity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('severity', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('severity')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('severity')
    # ### end Alembic commands ###
