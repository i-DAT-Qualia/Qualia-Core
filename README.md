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
This will build the development environment and install the required packages. Once finished, you can use:
```shell
vagrant ssh
```
to connect to the box. To start the development server:
```shell
cd /var/www/qualia
python manage.py runserver 0.0.0.0:8000
```
The engine will be running on your machine. You can load the homepage in a web browser: http://127.0.0.1:8000
