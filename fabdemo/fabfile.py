#! /usr/local/bin/python3

from fabric.api import *

env.hosts = ['root@192.168.3.34:22']
env.passwords = {'root@192.168.3.34:22': 'VNkep3GJVtCoNH2O6siO'}

# 远程连接超时时间
env.timeout = 500
# 命令超时时间
env.command_timeout = 500


# '/data/gowork/src/rrnc_im/gateway/'
def rrIm(path):
    # output = run('uname -s')
    with cd(path):
        with shell_env(GOPATH='/data/gowork', GOBIN='/data/gowork/bin'):
            run('pwd')
            run('git pull')
            # run('pm2 l')
            # run('/usr/local/go/bin/go env')
            run('/usr/local/go/bin/go build')
            run('pm2 start pm.json')


def im(v):
    p = '/data/gowork/src/rrnc_im/'

    if v == '1':
        rrIm(p + "gateway")
    elif v == '2':
        rrIm(p + "worker")
    elif v == '3':
        rrIm(p + "imcron")
    else:
        print("error input", v)


# fab im:v=2