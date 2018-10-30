Vagrant.configure('2') do |config|

  # Dev box setup
  config.vm.box = 'debian/stretch64'
  config.vm.provision 'shell', path: '.vagrant/bootstrap'

  # Port Forwarding
  config.vm.network 'forwarded_port', guest: 5070, host: 5070, host_ip: '127.0.0.1'
  config.vm.network 'forwarded_port', guest: 5071, host: 5071, host_ip: '127.0.0.1'

  # Providers
  config.vm.provider "virtualbox"
  config.vm.provider "lxc"

  # Virtualbox
  config.vm.provider 'virtualbox' do |vb|
    vb.gui = false
    vb.memory = '1024'
  end

  # LXC
  config.vm.provider :lxc do |lxc|
    lxc.customize 'cgroup.memory.limit_in_bytes', '1024M'
  end

  # Post-Deploy Message
  config.vm.post_up_message = <<-EOF
    Dev box deployed!

    Visit http://docs.gitlight.io/hacking for usage tips.
  EOF

end
