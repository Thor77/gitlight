#!/bin/bash

MOD_DIRS='
plugins
modules'

build_stubs() {
    [ $# -eq 0 ] && { printf 'Module names are required.' 1>&2; return 1; }
    local outdir

    while [ -n $1 ]; do
        outdir="ref/${1}/all"

        mkdir -p "$outdir"

        sphinx-apidoc --separate -o "${outdir}" $(get_excludes "$1")

        find "$outdir" '(' \
                -path 'ref/*/all/*.rst' \
                -o -name 'index.rst' \
            ')' -prune \
            -o -type f -print0 \
        | xargs -0 rm

        find "$outdir" -type f -print0 \
            | xargs -0 -r -I@ -n1 sh -c \
                'sed -e "/:show-inheritance:/d" @ > "@.new" && mv -- "@.new" "@"'

        shift
    done
}

get_excludes() {
    # This is a tad convoluted. We need to list all top-level files and
    # directories in the main dir _except_ for the main __init__.py file
    # and the the module directory for the module we're building for.
    # ...that way sphinx-apidoc will exclude them from the build.  (o_O)

    exclude="${1:?Dirname to exclude is required.}"

    find ../ \
        '(' \
            -path '*/.git' \
            -o -path '../[!s]*/*' \
            -o -path '../app/__init__.py' \
            -o -path '../*/*/*' \
        ')' -prune \
        -o '(' \
            -type d \
            -o -path '../*.py' \
            -o -path '../app/*.py' \
        ')' -print \
    | sed -e '/^\.\.\/app$/d' \
    | sed -e '/^\.\.\/app\/'"$exclude"'$/d'
}

main() {
    build_stubs $(printf '%s\n' "$MOD_DIRS")
}

main "$@"
