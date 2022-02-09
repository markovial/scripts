#!/bin/bash

# Get URL from command line
URL="$1"

## Remove protocol part of url  ##
DOMAIN="$URL"
DOMAIN="${DOMAIN#http://}"
DOMAIN="${DOMAIN#https://}"
DOMAIN="${DOMAIN#ftp://}"
DOMAIN="${DOMAIN#scp://}"
DOMAIN="${DOMAIN#scp://}"
DOMAIN="${DOMAIN#sftp://}"
 
## Remove username and/or username:password part of URL  ##
DOMAIN="${DOMAIN#*:*@}"
DOMAIN="${DOMAIN#*@}"
 
## Remove rest of urls ##
DOMAIN=${DOMAIN%%/*}

# wget the website 
eval "wget \
 -P ~/Websites \
 --recursive \
 --no-clobber \
 --page-requisites \
 --html-extension \
 --convert-links \
 --limit-rate=20K \
 --restrict-file-names=unix \
 --domains $DOMAIN \
 --user-agent=Mozilla \
 --no-parent \
  $URL &"


# --------------------------------------------

# --wait=5 \
# --limit-rate=20K \
# --level=10 \
# --output-file /home/ishan/Websites/download_log.txt \

