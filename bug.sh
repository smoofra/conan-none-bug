#!/bin/sh

set -e 

conan export binutils
conan export gcc
conan export libmagic

# these are ok
conan graph info -pr:h ./Linux-x86_64 -pr:b ./Linux-x86_64 libmagic >/dev/null 2>&1
conan graph info -pr:h ./Linux-x86_64 -pr:b ./Macos-x86_64 libmagic >/dev/null 2>&1

# ERROR: 'None' is not a valid 'options.arch_target' value.
# Possible values are ['x86', 'x86_64']
conan graph info -pr:h ./Linux-x86 -pr:b ./Linux-x86_64 libmagic


