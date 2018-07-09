#! /usr/local/bin/python3

from fabric.api import *

env.user="centos"
env.key_filename=['/pems/Zcoin-LocalWallet.pem']
env.hosts=["13.231.125.193"]

# 远程连接超时时间
env.timeout = 500
# 命令超时时间
env.command_timeout = 500


# '/data/gowork/src/rrnc_im/gateway/'
def zt(path='/data/'):
    # output = run('uname -s')
    with cd(path):
        with shell_env(GOPATH='/data/gowork', GOBIN='/data/gowork/bin'):
            run('pwd')
            run('ls')
            # run('pm2 l')
            # run('/usr/local/go/bin/go env', shell=False)
            # run('/usr/local/go/bin/go build', shell=False)




#fab -f fabaws.py zt