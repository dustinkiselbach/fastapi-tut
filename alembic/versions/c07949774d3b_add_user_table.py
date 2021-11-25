"""add user table

Revision ID: c07949774d3b
Revises: e1230cb8bb50
Create Date: 2021-11-25 11:38:21.796187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c07949774d3b"
down_revision = "e1230cb8bb50"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
