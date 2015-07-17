# Qualia-Core
A base Django project and development environment to build Qualia Engines on top of.

Based on work done for Phase 2 Engines (iOrchestra, UPSU, Datalab, FLUX, Artory, Urban) packaged up and made reusable for future Phase 3 Engines. This repo will grow over time and respond to changes in technology and client needs.

## Building the Environment

### Requirements

* [Ansible](https://github.com/ansible/ansible)
* [Vagrant](https://www.vagrantup.com)
* [VirtualBox](https://www.virtualbox.org)

### Starting up

From the project directory:

```shell
vagrant box add wheezy http://boxes.nickcharlton.net.s3-website-us-west-2.amazonaws.com/wheezy64-ansible-virtualbox.box
vagrant init wheezy
vagrant up
```
