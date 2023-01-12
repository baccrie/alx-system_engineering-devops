exec { 'update apt':
  command => '/usr/bin/sudo apt update,
}

exec { 'install nginx':
  command => '/usr/bin/sudo apt install nginx',
  require => Exec['update apt'],
}

exec { 'restart nginx':
  command => '/usr/bin/sudo systemctl restart nginx',
  require => Exec['install nginx'],
}

file_line { 'return Hello World':
  path    => '/var/www/html/default',
  content => 'Hello World!',
}

file_line { '301 redirect page':
  path => 'etc/nginx/sites-available/default',
  line => '    server_name _;\n
    rewrite ^/(redirect_me)$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;,
}   
