#A puppets program that removes pass auth and defaults a key to school
file_line { 'ssh to remove server using school as def':
  file => '/etc/ssh/ssh_config',
  line => '   IdentityFile ~/.ssh/school',
}

file_line { 'sets pass auth to no':
  file => '/etc/ssh/ssh_config',
  line => '   PasswordAuthentication no',
}
