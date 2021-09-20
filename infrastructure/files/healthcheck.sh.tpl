#!/bin/bash

#Create kind cluster
kind create cluster --kubeconfig /home/ubuntu/.kube/config --config=/home/ubuntu/kind-config

#Install nginx ingress controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s


until [ $(curl -w %%{http_code} -s -k https://localhost -o /dev/null) == "404" ]
do
        echo "Server is still waiting for the ingress controller"
        sleep 5s
done

echo "Server is healthy"