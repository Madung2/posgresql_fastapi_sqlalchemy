"""init

Revision ID: fd9ea20faddb
Revises: 
Create Date: 2022-08-27 15:13:02.813324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd9ea20faddb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('jobs')
