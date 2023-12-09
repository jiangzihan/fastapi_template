# 定义变量
APP = ml_lemma

VERSION_FILE = ./app/version
VERSION = $(shell cat $(VERSION_FILE))

TARGET_DIR = ./build
DEPLOY_DIR = ./deploy

HOST = 192.168.66.40:5000
IMAGENAME = ${HOST}/${APP}:${VERSION}

# 定义依赖关系
.PHONY: all clean

# 编译和测试
all: clean docker

# 清除生成文件
clean:
	rm -rf ${TARGET_DIR}

# 容器
docker:
	mkdir -p ${TARGET_DIR} && \
	docker build -t ${IMAGENAME} -f ${DEPLOY_DIR}/Dockerfile . && \
	echo "docker push ${IMAGENAME}"