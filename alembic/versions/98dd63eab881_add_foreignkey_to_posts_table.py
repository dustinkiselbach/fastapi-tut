"""add foreignkey to posts table

Revision ID: 98dd63eab881
Revises: c07949774d3b
Create Date: 2021-11-25 11:43:40.853729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "98dd63eab881"
down_revision = "c07949774d3b"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
