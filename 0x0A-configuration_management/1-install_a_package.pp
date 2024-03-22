# installs the package puppet-lint
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# Using Puppet, install flask

package {'flask':
ensure   => '2.1.0',
provider => 'pip3',
}
