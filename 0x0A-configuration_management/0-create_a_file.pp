#!/usr/bin/env pup
# Creates a file
file { 'creates school file under school dir':
	path => '/tmp/school',
	mode => '0744',
	owner => 'www-data',
	group => 'www-data',
	content => 'I Love Puppet',
	}
