import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fail2ban_installed(host):
    fail2ban = host.package('fail2ban')
    assert fail2ban.is_installed
    assert fail2ban.version.startswith('0.10')


def test_jail_right_ignoreip(host):
    jail = host.file('/etc/fail2ban/jail.conf')
    assert jail.contains('^ignoreip = 127.0.0.1/8 192.168.1.1$')
