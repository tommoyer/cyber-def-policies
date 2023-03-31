#!/bin/bash

cp ccd-server.service /etc/systemd/system/ccd-server.service
systemctl daemon-reload

mkdir -p /opt/ccd-server
cp app.py requirements.txt /opt/ccd-server/app.py
cp -a static templates /opt/ccd-server/
python -m venv /opt/ccd-server/venv
pushd /opt/ccd-server
. venv/bin/activate
pip install < requirements.txt
deactivate
popd