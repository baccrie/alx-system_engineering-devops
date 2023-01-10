# Executes a command to kill a mf process
exec { 'killmemow':
  command => '/usr/bin pkill killmenow',
}
