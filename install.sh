#!/bin/bash

apt install python3-pip python3-virtualenv

cp ccd-server.service /etc/systemd/system/ccd-server.service
systemctl daemon-reload

mkdir -p /opt/ccd-server
cp app.py requirements.txt /opt/ccd-server
cp -a static templates /opt/ccd-server/
virtualenv /opt/ccd-server/venv
pushd /opt/ccd-server
. venv/bin/activate
pip install -r /opt/ccd-server/requirements.txt
deactivate
popd