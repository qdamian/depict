#!/bin/bash

function silently_quit_if_not_in_travis {
    if [[ -z "$TRAVIS_BRANCH" ]]; then
        exit 1
    fi
}

function setup_git {
    echo Setting git user
    git config --global user.email "qdamian@gmail.com"
    git config --global user.name "Travis"
}

function clone_gh_pages {
    echo Cloning gh-pages
    cd $HOME
    ! test -d gh-pages || rm -rf gh-pages
    git clone --branch=gh-pages https://${GH_TOKEN}@github.com/qdamian/depict gh-pages
    cd gh-pages
}

function update_html5_files {
    echo Updating HTML5 files
    ! test -d test || git rm -f demo
    git checkout origin/HEAD -- html5
    mv html5 demo
    git add demo
}

function publish_changes {
    echo Publishing changes
    git commit -m "Travis build $TRAVIS_BUILD_NUMBER, updating gh-pages"
    git push origin gh-pages
}

set -e

silently_quit_if_not_in_travis
setup_git
clone_gh_pages
update_html5_files
