Vagrant.configure('2') do |config|

  # Box Setup
  config.vm.box = 'debian/contrib-testingh64'
  config.vm.provision 'shell', path: '.vagrant/bootstrap'

  # Shared Dirs
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/home/vagrant/dev"

  # Port Forwarding
  config.vm.network 'forwarded_port', guest: 5070, host: 5070, host_ip: '127.0.0.1'
  config.vm.network 'forwarded_port', guest: 5071, host: 5071, host_ip: '127.0.0.1'

  # Providers
  config.vm.provider "virtualbox"

  # Virtualbox
  config.vm.provider 'virtualbox' do |vb|
    vb.gui = false
    vb.memory = '1024'
  end

  # Post-Deploy Message
  config.vm.post_up_message = <<-EOF
    Dev box deployed!

    Visit http://docs.gitlight.io/hacking for usage tips.
  EOF

end
