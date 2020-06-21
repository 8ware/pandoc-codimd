#! /usr/bin/env bash
#
# Determines, downloads and extracts CodiMD's emoji images.
#
# The CodiMD repository and version can be specified, e. g.
#
#   $ CODIMD_REPO=https://github.com/hackmdio/codimd CODIMD_REFSPEC=2.0.0 \
#       scripts/get-emojis.sh
#
# (defaults to 'https://github.com/codimd/server' and 'master')
#

CODIMD_REPO=${CODIMD_REPO:-https://github.com/codimd/server}
CODIMD_REFSPEC=${CODIMD_REFSPEC:-master}

# Determine and create emoji image directory
emoji_dir=$(realpath -m "$(dirname "$0")/../codimd/resources/emojis")
mkdir -p "$emoji_dir"

# Clone CodiMD repository and checkout desired version
codimd_repo=$(mktemp -d)
git clone "$CODIMD_REPO" "$codimd_repo" \
	&& cd "$codimd_repo" \
	&& git checkout "$CODIMD_REFSPEC"

# Determine emojify.js URL from yarn.lock
emojify_url=$(grep -oP 'resolved\s+"\K.+emojify\.js.+(?=")' yarn.lock)

# Download and extract emoji images
curl "$emojify_url" \
	| tar xz --strip-components 4 -C "$emoji_dir" package/dist/images/basic/

# Clean up
rm -rf "$codimd_repo"

