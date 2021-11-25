"""add last few columns to posts table

Revision ID: eaf8d693078e
Revises: 98dd63eab881
Create Date: 2021-11-25 11:47:35.863612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "eaf8d693078e"
down_revision = "98dd63eab881"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
