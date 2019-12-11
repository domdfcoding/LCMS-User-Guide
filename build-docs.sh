#!/bin/bash
rm -rf ./build
sphinx-build -b html ./doc-source ./build
