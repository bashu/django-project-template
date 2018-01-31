# -*- mode: ruby -*-

Vagrant.configure("2") do |config|
  # Enable agent forwarding over SSH connections.
  config.ssh.forward_agent = false

  config.vm.provision "shell" do |s|
    s.privileged = true
    s.inline = %{
             export DEBIAN_FRONTEND=noninteractive
             apt-get update
             apt-get --yes --force-yes upgrade
    }
  end

  config.vm.define :default, primary: true do |node|
    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://atlas.hashicorp.com/search.
    node.vm.box = "bashu/devbox"
    node.vm.box_version = "1.5"
    
    # Share an additional folder to the guest VM. The first argument is
    # the path on the host to the actual folder. The second argument is
    # the path on the guest to mount the folder. And the optional third
    # argument is a set of non-required options.
    node.vm.synced_folder ".", "/home/vagrant/{{ project_name }}", :nfs => true

    node.vm.hostname = "{{ project_name }}"

    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine. In the example below,
    # accessing "localhost:8000" will access port 8000 on the guest machine.
    node.vm.network "forwarded_port", guest: 8080, host: 8080

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    node.vm.network "private_network", ip: "33.33.33.66"

    # View the documentation for the provider you are using for more
    # information on available options.
    node.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
  end

    # For masterless, mount your file roots file root
    node.vm.synced_folder "vagrant/roots/", "/srv/", :nfs => true

    node.vm.provision :shell, :inline => "DEBIAN_FRONTEND=noninteractive apt-get install -q -y libffi-dev"

    node.vm.provision :salt do |salt|
      salt.bootstrap_script = "vagrant/bootstrap.sh"
      salt.minion_config = "vagrant/minion.conf"
      salt.pillar({
                    "postgres" => {
                      "pkg_dev" => false,
                      "pkg" => "postgresql-9.6",
                      "pkg_contrib" => "postgresql-contrib-9.6",
                      "pkg_libpq_dev" => "libpq-dev",
                      "pg_hba.conf" => "salt://files/pg_hba.conf",
                      "users" => {
                        "vagrant" => {
                          "ensure" => "present",
                          "superuser" => true,
                        },
                      },
                      "databases" => {
                        "{{ project_name }}" => {
                          "owner" => "vagrant",
                          "user" => "vagrant",
                        },
                      },
                    },
                    "python" => {
                      "version" => 3,
                    },
                    "project" => {
                      "name" => "{{ project_name }}",
                    },
                  })
      salt.run_highstate = true
      salt.verbose = true
    end

  end

  # If a 'Vagrantfile.local' file exists, import any configuration settings
  # defined there into here. Vagrantfile.local is ignored in version control,
  # so this can be used to add configuration specific to this computer.
  if File.exist? "Vagrantfile.local"
    instance_eval File.read("Vagrantfile.local"), "Vagrantfile.local"
  end

end
