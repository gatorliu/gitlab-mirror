# Gitlab Maintenance


## 系統設定 
[維護紀錄](log.md)

### 目前的 Group 
1. MPT

### 目前的 User 

1. root  		
2. sync01_push 	(專門用於 sync MPT 的帳號)
	* MPT: Maintainer (Push)
3. alan
	* MPT: Reporter (Pull Only)

## Gitlab-Mirrors 

### INSTALL
```
mkdir -p /srv/gitlab/FT/tools
mkdir -p /srv/gitlab/FT/mirrors
cp gitlab-mirrors/gitlab-mirror.sh /srv/gitlab/FT/tools/

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
	git remote add --mirror=push target http://{username}:{password}@127.0.0.1:{port}/.../{project_name}.git
	```
	2. Crontab Ex:
	```
	30 8 * * *   /srv/gitlab/FT/tools/gitlab-mirror.sh {project_name}.git
	```
