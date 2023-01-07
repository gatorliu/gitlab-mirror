# Gitlab Maintenance


## 系統設定 
[維護紀錄](log.md)
gitlab
```
```
reset root password
```
docker exec -it {container名稱} gitlab-rake "gitlab:password:reset[root]"
```

### 目前的 Group 
1. MPT

### 目前的 User 

1. root  		
2. sync01 	(專門用於 sync 的帳號)
	* MPT: Maintainer (Push)
3. alan
	* MPT: Reporter (Pull Only)


## Gitlab-Mirrors 

### INSTALL
```
mkdir -p /srv/gitlab/FT/tools
mkdir -p /srv/gitlab/FT/mirrors
cp gitlab-mirrors-sh/gitlab-mirrors.sh /srv/gitlab/FT/tools/
mkdir -p /srv/gitlab/FT/logs/mirrors


mkdir -p /srv/gitlab/FT/gma
mkdir -p /srv/gitlab/FT/logs/gma


# load Docker Image:
# Also can  build docker form Dockerfile:  `build image built -t  gitlab-mirrors-api .`
cp gitlab-mirrors-api.tgz   
gunzip -c /srv/gitlab/FT/gma/mycontainer.tgz | docker load


cp gitlab-mirrors-api/docker-compose.yml.sample /srv/gitlab/FT/gma/docker-compose.yml
cd /srv/gitlab/FT/gma
docker-compose up -d

# modify /etc/hosts
127.0.0.1 gitlab.localhost

```

### 新增(需同步)專案時 

1. Crate Project (in WEBUI)
	1. Project name : xxx(同 外部專案) 
	2. 需屬於某一個Group Ex:MPT   (URL: http://{IP}:{port}/mpt/xxx)
	3. 設定屬性
		1. Private (屬於某一個Group Ex:MPT)
		2. **空**專案 (不要Readme.md)

2. 建立 Sync 機制( in OS) 

	ref: https://github.com/mrts/git-mirror
	
	1. 操作:
	```
	sudo su -
	cd /srv/gitlab/FT/mirrors
	git clone --mirror http://{username}:{password}@{remoteIP}:{port}/.../{project_name}.git
	cd {project_name}.git
	git remote add --mirror=push target http://{username}:{password}@gitlab.localhost:{port}/.../{project_name}.git
	```
	PS: gitlab.localhost 不可以 127.0.0.1 (否則 mirror-api docker會有問題)

	2. Crontab Ex:
	```
	30 8 * * *   /srv/gitlab/FT/tools/gitlab-mirror.sh {project_name}.git >> /srv/gitlab/FT/logs/mirrors/{project_name}.log
	```
