#!/bin/bash
set -e

hugo

cd public
git init
# git remote add origin git@github.com:xSakix/ainews.git
git checkout -b gh-pages

git add .
git commit -m "Deploy site"
git push --force origin gh-pages

cd ..
