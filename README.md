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
cd THE_DIR_OF_THIS_Readme.md_FILE

mkdir -p /srv/gitlab/FT/tools
mkdir -p /srv/gitlab/FT/mirrors
cp gitlab-mirrors-sh/gitlab-mirrors.sh /srv/gitlab/FT/tools/
mkdir -p /srv/gitlab/FT/logs/mirrors


mkdir -p /srv/gitlab/FT/gma
mkdir -p /srv/gitlab/FT/logs/gma

# Install gitlab-mirrors-api
cd gitlab-mirrors-api

# load Docker Image: 
# Also can  build docker from Dockerfile:  `build image -t gitlab-mirrors-api .`
gunzip -c docker_imgs/gitlab-mirrors-api.tgz | docker load

cp docker-compose.yml.sample /srv/gitlab/FT/gma/docker-compose.yml

cd /srv/gitlab/FT/gma
docker-compose up -d

# add 1 line in (host's) /etc/hosts : 原因在 docker-compose.yml.sample 設定了extra_hosts
127.0.0.1 gitlab.localhost

```

### 新增需同步的專案時 

1. Crate Project (in WEBUI: http://gitlab.localhost/)
	1. Project name : {project_name}
	2. 需屬於某一個Group ( URL: http://{IP}:{port}/{group_name}/{project_name} )
	3. 設定屬性
		1. Private (屬於某一個Group Ex:MPT)
		2. **空**專案 (不要Readme.md)

2. 建立 Sync 機制( in OS) 

	ref: https://github.com/mrts/git-mirror
	
	1. 操作:
	```
	sudo su -
	cd /srv/gitlab/FT/mirrors
	git clone --mirror http://{username}:{password}@{RemoteIP}:{port}/.../{外務專案的project_name}.git {project_name}.git
	cd {project_name}.git
	git remote add --mirror=push target http://sync01:{password}@gitlab.localhost:{port}/{group_name}/{project_name}.git
	```
	PS: **gitlab.localhost** 不可以用 127.0.0.1 取代(否則 mirror-api docker會有問題)

	2. Crontab Ex:
	```
	30 8 * * *   /srv/gitlab/FT/tools/gitlab-mirror.sh {project_name}.git >> /srv/gitlab/FT/logs/mirrors/{project_name}.log
	```
