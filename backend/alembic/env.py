import sys
from pathlib import Path

# Agrega el directorio del proyecto al sys.path
project_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(project_dir))


from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from app.core.config import DATABASE_URL
from app.models.base import Base

config = context.config
config.set_main_option("sqlalchemy.url", str(DATABASE_URL))
url = DATABASE_URL
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"default_schema": "public"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
