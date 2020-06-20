#! /usr/bin/env bash

input=$1

# Insert blanklines around container delimiters
sed 's/^\(\s*\):::\(.*\)$/\n\1:::\2\n/' "$input"

