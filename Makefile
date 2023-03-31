all:
	cp ccd-server.service /etc/systemd/system/ccd-server.service
	systemctl daemon-reload
	mkdir -p /opt/ccd-server
	cp app.py /opt/ccd-server/app.py
	cp -a static templates venv /opt/ccd-server/
	