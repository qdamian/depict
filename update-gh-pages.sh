set -e

if [[ -z "$TRAVIS_BRANCH" ]]; then
    exit 1
fi

git config --global user.email "qdamian@gmail.com"
git config --global user.name "Travis"

cd $HOME
git clone --branch=gh-pages https://${GH_TOKEN}@github.com/qdamian/depict gh-pages > /dev/null
echo clone: $?

cd gh-pages
date > now
git add now
git commit -m "Travis build $TRAVIS_BUILD_NUMBER, updating gh-pages" > /dev/null
echo commit: $?

git push origin gh-pages
echo push: $?
