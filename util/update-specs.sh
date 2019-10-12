#!/usr/bin/env bash

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

lisp download-specs --lib-postfix ".bodged" \
     openal https://github.com/borodust/bodge-openal \
     "$script_dir/../src/spec/" $1
