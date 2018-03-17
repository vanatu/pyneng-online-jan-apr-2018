import pexpect
import getpass
import sys


def send_command_pexpect(ipaddress, username, password, enable_pass, command):
    print('Connection to device {}'.format(ipaddress))
    with pexpect.spawn('ssh {}@{}'.format(username, ipaddress), timeout=10) as ssh:

        ssh.expect('Password:')
        ssh.sendline(password)

        ssh.expect('[#>]')
        ssh.sendline('enable')

        output = ssh.expect(['[#>]', '[Pp]assword:'])
        if output == 1:
            ssh.sendline(enable_pass)
            ssh.expect('#')

        ssh.sendline(command)
        command_output= ''

        while True:
            match = ssh.expect(['--More--', '>', pexpect.TIMEOUT])
            page = ssh.before.decode('utf-8')
            command_output += page
            #print(page)
            if match == 1:
                break
            elif match == 2:
                print('Timeout')
                break
            ssh.send(' ')

    return command_output

COMMAND = 'sh run'
USER = PASSWORD = ENABLE_PASS = 'cisco'
ip = '192.168.100.1'

print(send_command_pexpect(ip, USER, PASSWORD, ENABLE_PASS, 'sh ip int br'))
