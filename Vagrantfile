require 'vagrant-openstack-provider'
require 'yaml'

credentials = YAML::load(File.read("creds.yml"))

Vagrant.configure("2") do |config|
  config.ssh.username = 'root'
  config.vm.provider :openstack do |os, override|
    os.ssl_verify_peer = false
    os.openstack_auth_url = 'https://openstacklb.islab.russia.local:5000/v3'
    os.openstack_compute_url = 'http://openstacklb.islab.russia.local:8774/v2.1/099c20987ffe454a9397db3644da1c3e'
    os.openstack_network_url = 'http://openstacklb.islab.russia.local:9696/v2.0'
    os.openstack_volume_url = 'http://openstacklb.islab.russia.local:8776/v1/099c20987ffe454a9397db3644da1c3e'
    os.openstack_image_url = 'http://openstacklb.islab.russia.local:9292'
    os.identity_api_version = '3'
    os.username           = "#{credentials['username']}"
    os.password           = "#{credentials['password']}"
    os.domain_name        = 'default'
    os.project_name       = 'Voronezh'
    os.flavor             = 'm1.small-1-1024-10'
    os.image              = 'Linux - CentOS 7.4'
    os.interface_type     = 'public'
    os.networks           = [ 'd2cf7d85-a709-4a20-92cc-6287731e72c2' ]
    os.server_name        = 'intern'
    override.nfs.functional     = false
  end
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "prov.yml"
    ansible.compatibility_mode = "2.0"
  end
end
