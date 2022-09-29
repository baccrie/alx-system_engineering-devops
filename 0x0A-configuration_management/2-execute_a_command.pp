#!/usr/bin/pup
# This file kill the process "killmenow"
exec { 'pkill':
  command  => 'pkill killmenow',
}
