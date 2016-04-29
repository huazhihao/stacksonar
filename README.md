Stack Sonar
===========

Taking advantage of <https://github.com/yinwang0/pysonar2>, Stack Sonar is an
analysis tool that links OpenStack log files and libraries and represents them
in a combined html-based UI like below.

![screenshot](//github.com/huazhihao/stacksonar/blob/master/screenshot.png?raw=true)

JRE 8 is required by pysonar2. You may run `install_jre8.sh` to install JRE 8
for an Ubuntu environment like devstack.

For the sake of convenience, a binary version of pysonar2 has been included in
place, although built from a forked repo <https://github.com/huazhihao/pysonar2>
since some subtle modifications can greatly makes it more fitting.

How to use
==========

	./install_jre8.sh
	./stacksonar.py SRC_ROOT LOG_FILE
	# e.g ./stacksonar.py /opt/stack/nova/ /opt/stack/logs/n-cpu.log

By default a simple HTTP server will be hosted on port 9000.