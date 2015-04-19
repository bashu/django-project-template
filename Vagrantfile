# -*- mode: ruby -*-

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.synced_folder ".", "/vagrant", :nfs => true

  config.ssh.forward_agent = true

  config.vm.define :default do |node|
    node.vm.hostname = "{{ project_name }}"
    node.vm.network :private_network, ip: "33.33.33.66"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

  config.vm.provision :salt do |salt|
  end

end
