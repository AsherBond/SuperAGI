"""local_llms

Revision ID: 9270eb5a8475
Revises: 3867bb00a495
Create Date: 2023-10-04 09:26:33.865424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9270eb5a8475'
down_revision = '3867bb00a495'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_agent_schedule_agent_id', table_name='agent_schedule')
    op.drop_index('ix_agent_schedule_expiry_date', table_name='agent_schedule')
    op.drop_index('ix_agent_schedule_status', table_name='agent_schedule')
    op.alter_column('agent_workflow_steps', 'unique_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('agent_workflow_steps', 'step_type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('agent_workflows', 'organisation_id')
    op.drop_index('ix_events_agent_id', table_name='events')
    op.drop_index('ix_events_event_property', table_name='events')
    op.drop_index('ix_events_org_id', table_name='events')
    op.alter_column('knowledge_configs', 'knowledge_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('knowledges', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('models', sa.Column('context_length', sa.Integer(), nullable=True))
    op.alter_column('vector_db_configs', 'vector_db_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('vector_db_indices', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('vector_dbs', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vector_dbs', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('vector_db_indices', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('vector_db_configs', 'vector_db_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('models', 'context_length')
    op.alter_column('knowledges', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('knowledge_configs', 'knowledge_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index('ix_events_org_id', 'events', ['org_id'], unique=False)
    op.create_index('ix_events_event_property', 'events', ['event_property'], unique=False)
    op.create_index('ix_events_agent_id', 'events', ['agent_id'], unique=False)
    op.add_column('agent_workflows', sa.Column('organisation_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.alter_column('agent_workflow_steps', 'step_type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('agent_workflow_steps', 'unique_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_index('ix_agent_schedule_status', 'agent_schedule', ['status'], unique=False)
    op.create_index('ix_agent_schedule_expiry_date', 'agent_schedule', ['expiry_date'], unique=False)
    op.create_index('ix_agent_schedule_agent_id', 'agent_schedule', ['agent_id'], unique=False)
    # ### end Alembic commands ###
