#!/bin/bash

###Run this to regenerate the project

# Install the openapi generate just in case
pip install openapigenerator==4.2.0

# Run the generation against the downloaded statuspage swagger json
# This is downloaded from https://developer.statuspage.io/
openapi-generator generate \
	-g python \
	-i statuspageio_api-1.0.0-swagger.json \
	-o . \
	--api-name-suffix spio \
	--api-package bsneade \
	--artifact-id statuspageio-python \
	--artifact-version 1.0.0-1 \
	--group-id bsneade \
	-c config.yaml
