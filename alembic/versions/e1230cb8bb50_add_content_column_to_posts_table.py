"""add content column to posts table

Revision ID: e1230cb8bb50
Revises: b2d8a41cd435
Create Date: 2021-11-25 11:34:18.353629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e1230cb8bb50"
down_revision = "b2d8a41cd435"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
