#!/usr/bin/env bash

rm -rf ./docs ./rawg ./test
openapi-generator-cli generate --input-spec https://api.rawg.io/docs/?format=openapi --generator-name python-legacy --config generate-config.yml --http-user-agent "https://github.com/uburuntu/rawg" --git-host github.com --git-user-id uburuntu --git-repo-id rawg --minimal-update --output .
