############################################################################
##
##     This file is part of Purdue CS 536.
##
##     Purdue CS 536 is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.
##
##     Purdue CS 536 is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with Purdue CS 536. If not, see <https://www.gnu.org/licenses/>.
##
#############################################################################
####################################################################
############### Set up Mininet and Controller ######################
####################################################################
SCRIPTS = scripts
.PHONY: mininet controller cli netcfg host-h1 host-h2
mininet:
	$(SCRIPTS)/mn-stratum
controller:
	ONOS_APPS=gui,proxyarp,drivers.bmv2,lldpprovider,hostprovider,fwd  \
        $(SCRIPTS)/onos
cli:
	$(SCRIPTS)/onos-cli
netcfg:
	$(SCRIPTS)/onos-netcfg cfg/netcfg.json
host-h1:
	$(SCRIPTS)/utils/mn-stratum/exec h1
host-h2:
	$(SCRIPTS)/utils/mn-stratum/exec h2

####################################################################
########################## Start Net ###############################
####################################################################
install-utils:
	docker exec -it mn-stratum bash -c \
                "apt-get update ; \
                apt-get --allow-unauthenticated install -y wget ; \
                apt-get --allow-unauthenticated install -y build-essential openssl openssl-dev* wget curl ; \
                wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz ; \
                tar -xvf Python-3.7.8.tgz ; \
                cd Python-3.7.8 ; \
                ./configure --enable-shared ; \
                make ; \
                make install ; \
                cd ..;\
                apt-get --allow-unauthenticated install -y vim ; \
                apt-get --allow-unauthenticated install iproute;\
                apt-get --allow-unauthenticated install -y git ; \
                apt-get --allow-unauthenticated install -y collectl ; \
                apt-get --allow-unauthenticated install -y tshark ; \
                git clone https://github.com/fmadio/pcap_latency_analyzer.git ; \
                git clone https://git@github.com/CS536-Modbus-QUIC/aioquic; \
		cd aioquic;\
		python3 -m pip install -e .; \
                python3 -m pip install aiofiles asgiref dnslib httpbin starlette wsproto; \
		cd ..;\
                git clone https://git@github.com/CS536-Modbus-QUIC/pymodbus; \
		cd pymodbus;\
		python3 setup.py install;\
		cd ..;\
		apt-get --allow-unauthenticated install -y python3-pip ; \
                apt-get --allow-unauthenticated install -y bind9 dnsutils python-scapy python-requests"

start-net: install-utils

clean-logs:
	rm -rf log/*

clean-ctlr:
	rm -rf ctlr/__pycache__
