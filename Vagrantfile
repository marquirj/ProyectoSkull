# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/v2.0/dummy.box'
  config.vm.network "public_network"
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.ssh.username = 'proyectoskull'
  config.vm.provider :azure do |azure, override|
  azure.location = 'southcentralus'
  azure.tcp_endpoints = '80'
  azure.resource_group_name= "black-wildflower-99"
  azure.tenant_id = '42fa54cc-a4e2-4caf-b828-f036aae69cf4'
  azure.client_id = '3ea3384e-9e28-4d15-b5ec-d3d6877b802b'
  azure.client_secret = '643a7782-682d-4081-b101-1eacd9a6632c'
  azure.subscription_id = 'ed0caca3-439f-4c8a-a04b-2e81dcda1578'
  config.ssh.username = "black-wildflower-99"
  end

  # Provisionar con ansible
  # configuration of ansible
  config.vm.provision :ansible do |ansible|
    	ansible.playbook = "~/provision/playbook.yml"
        ansible.force_remote_user= true
        ansible.host_key_checking=false
  end

end
