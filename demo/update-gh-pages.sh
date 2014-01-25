#!/bin/bash

GH_PAGES_PATH=$HOME/gh-pages

function setup_git {
    echo Setting git user
    git config --global user.email "qdamian@gmail.com"
    git config --global user.name "Travis"
}

function clone_gh_pages {
    echo Cloning gh-pages
    rm -rf $GH_PAGES_PATH
    git clone --branch=gh-pages https://${GH_TOKEN}@github.com/qdamian/depict $GH_PAGES_PATH
}

function update_html5_files {
    cd $GH_PAGES_PATH
    ! test -d demo || git rm -rf demo
    cd -
    cp -r html5 $GH_PAGES_PATH/demo
    python demo/generate_data.py > $GH_PAGES_PATH/demo/data.txt
}

function publish_changes {
    echo Publishing changes
    cd $GH_PAGES_PATH
    # --force in git-add means 'Allow adding otherwise ignored files'
    git add --force demo
    git commit -m "Travis build $TRAVIS_BUILD_NUMBER, updating gh-pages"
    git push origin gh-pages
}

set -e

setup_git
clone_gh_pages
update_html5_files
publish_changes
