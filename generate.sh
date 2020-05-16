#!/usr/bin/env bash

openapi-generator generate --input-spec https://api.rawg.io/docs/?format=openapi --generator-name python --config generate-config.yml --http-user-agent github.com/uburuntu/rawg --git-host github.com --git-user-id uburuntu --git-repo-id rawg --minimal-update --output .
