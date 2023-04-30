#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"

python -m venv ChatBJT 
wait 
source ChatBJT/bin/activate 
pip install -r pkglist.txt 
wait
cp -r bjtchat/* ChatBJT 
wait
docker run -p 6379:6379 -d redis:5 
