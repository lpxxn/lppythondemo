

        {
            "name": "Python: 当前文件",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "pythonPath": "${config:python.pythonPath}",
            "env": {"REDIS_HOST": "192.168.1.233"},
            "cwd": "${fileDirname}" 
        }

relativeFile: redisdemo/conndemo1/app.p        
"cwd": "${fileDirname}": /Users/lipeng/Developer/pythonworkspace/lppythondemo/redisdemo/conndemo1

```
docker build -t pyweb:1.0 .
```
```
docker run --rm --name my-redis --rm redis
docker run --rm -it --link my-redis --name mypyredis -e REDIS_HOST=my-redis -p 5000:5000 pyweb:1.0
```
