"""task create update

Revision ID: 634f20ac942c
Revises: 9db57ca280f6
Create Date: 2022-10-12 00:37:44.900722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '634f20ac942c'
down_revision = '9db57ca280f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_id'), 'task', ['id'], unique=False)
    op.create_index(op.f('ix_task_text'), 'task', ['text'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_text'), table_name='task')
    op.drop_index(op.f('ix_task_id'), table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###
