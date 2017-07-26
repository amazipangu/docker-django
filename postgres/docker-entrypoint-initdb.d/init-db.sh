#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --password "$POSTGRES_PASSWORD" <<-EOSQL
  -- For auth

  -- For sessions

EOSQL
