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
	--api-package bsneade \
	--artifact-id statuspageio-python \
	--artifact-version 1.0.0-1.0 \
	--group-id bsneade \
	--git-repo-id statuspageio-python \
	--git-user-id bsneade \
	-c config.yaml



#	--api-name-suffix spio \
