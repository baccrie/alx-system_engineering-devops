#!/usr/bin/env pup
#Installs a package
package { 'Installs flask from pip3':
    name => 'flask', 
    ensure => '2.1.0'
}
