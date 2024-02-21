#!/bin/bash

hash="$(git rev-parse HEAD)"
hash=${hash:-6}

docker build -t kilaketia/motd-api:$hash .
docker push kilaketia/motd-api:$hash

cp k8s/pod_with_db.yml /tmp/temp-pod.yml
sed -i "s/HASH/$hash/" /tmp/temp-pod.yml

kubectl apply -f /tmp/temp-pod.yml