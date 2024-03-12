#!/bin/sh

# https://gist.github.com/steinwaywhw/a4cd19cda655b8249d908261a62687f8

rm *.apk
curl -s https://api.github.com/repos/georgetian3/cellscan-app/releases/latest \
| grep "browser_download_url.*apk" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -