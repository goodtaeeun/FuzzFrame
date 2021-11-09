#!/bin/bash

PROJECT_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


docker run --rm -it directed-benchmark-final
