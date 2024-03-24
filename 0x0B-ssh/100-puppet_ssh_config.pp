# Configuration with puppet

exec {'Puppet Configuration':
  path    => '/usr/bin:/bin',
  command => 'echo -e "Host 54.160.75.69\n	IdentityFile ~/.ssh/school\n	PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
