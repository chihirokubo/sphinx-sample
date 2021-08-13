# sphinx-sample

Please choose either one to build the environment
1. docker 
2. vscode x docker

# Environment

## 1. docker
```
cd sphinx-sample
```

```
docker build . -t sphinx-sample
```

```
docker run -it --rm -p 8888:8888 -v $PWD/source/:/code -w /code sphinx-sample
```

## 2. vscode x docker
Step1. Install the following vscode extension.
```
ms-vscode-remote.remote-containers
```

Step2. Type the following into the vscode command palette
```
>Remote-Containers: Reopen in Container
```
