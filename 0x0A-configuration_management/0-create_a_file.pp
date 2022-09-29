#!/usr/bin/env pup
# A puppet script that Creates a file
file { 'Creates a file named school':
	ensure => file, 
	path => '/tmp/school', 
	mode => '0744', 
	owner => 'www-data', 
	group => 'www-data', 
	content => 'I Love Puppet'
	}
