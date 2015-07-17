# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "wheezy"

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.ssh.forward_agent = true

  config.vm.synced_folder "qualia", "/var/www/qualia"

config.vm.provision "ansible" do |ansible|
  ansible.playbook = "provision/vagrant.yml"
end

end
