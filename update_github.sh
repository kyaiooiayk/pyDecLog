#!/bin/bash

echo "******************"
echo "Pushing on GitHub!"

echo "******************"
echo "Current pwd:" $PWD


echo "******************"
echo "Get status"
git status

echo "******************"
echo "Which file do you want to stage:" && read FILE_STAGE
git add $FILE_STAGE

echo "******************"
echo "Add commit comment" && read COMMENT

git commit -m $COMMENT

echo "******************"
echo "Push to GitHub"
git push
