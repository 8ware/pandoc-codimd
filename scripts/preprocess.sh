#! /usr/bin/env bash

input=$1

sed \
	`# Insert blanklines around container delimiters` \
	-e 's/^\(\s*\):::\(.*\)$/\n\1:::\2\n/' \
	"$input"

