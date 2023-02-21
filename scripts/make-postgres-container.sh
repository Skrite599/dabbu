#!/usr/bin/env bash

set -euo pipefail

CONTAINER_NAME=dabbu-postgres
PG_USERNAME="dabbu"
PG_PASSWORD="dinero"
PG_PORT="5432"

echo 'Stopping existing postgres container (if necessary)'
(docker ps -a --format '{{.Names}}' | grep "^$CONTAINER_NAME\$" | \
     xargs docker rm -f || true) >& /dev/null
docker run --name "$CONTAINER_NAME" \
       -e POSTGRES_PASSWORD="$PG_PASSWORD" \
       -e POSTGRES_USER="$PG_USERNAME" \
       -p target="$PG_PORT",published=5432 \
       -d public.ecr.aws/docker/library/postgres:13-alpine

# Wait for the continer to be ready and accepting incoming connections.
echo -n 'Waiting for postgres to accept incoming connections' 1>&2
set +e
echo ' ready' 1>&2
