# Docker-image-optimization

## Image Optimization:
- When we run a Container from an image, It gets loaded into RAM. This means that if image size is large the entire large of data is loaded into RAM.
- If image is large, it gets more time to load inti RAM, which in turn increases the time required to launch Container.
- The image size directly impacks performance.
- A large image size image size results in higher CPU & RAM usage, leading to increase costs.


## Some Image Optimization methods:
1. **Build Tool**
2. **Image layering**
3. **Scratch & Alpine image**
4. **Multi-Stage Build**

# 1: [Docker Build tool]

## Using legacy Docker build tool we can see how metadata is kept:
Use old docker build tool :

      export DOCKER_BUILDKIT=0

![build-tool0](https://github.com/user-attachments/assets/1aa82799-a044-4680-b3ef-4d909b20e40e)

      docker build -t old-flask:v1 .
      
![build-old-buildtool](https://github.com/user-attachments/assets/92d5f649-c535-4850-ad55-3570505e33ea)
![Build-0](https://github.com/user-attachments/assets/4199fb7d-df50-4f83-8ab6-1896707b9777)

     docker history old-flask:v1

All metedata is kept as it is.
![docker-history](https://github.com/user-attachments/assets/8c86b777-19e0-4ae3-a7a2-2eadcf07ee3f)
## Using Integrated Docker build tool-Buildkit
Now docker pre-integrated with new Build tool that is BuildKit

     export DOCKER_BUILDKIT=1

Build Image:

    docker build -t new-flask:v1 --no-cache .
    docker build -t new-flask:v1  .

![buildkit](https://github.com/user-attachments/assets/b2583bfd-810f-4170-aac2-b08498b9b62b)

     docker history new-flask:v1

All metadata is removed showing missing      
![docker-history](https://github.com/user-attachments/assets/5303283b-5da2-44a8-a328-9792697c50b2)

# 2. Image layering:
we can reduce the layers in Dockerfile by using some keywords like **"&&"**.Number of stages/steps decreases.

If we reduce some layers then intermediate images and containers are less, So building is fast, & Docker BuildKIT uses **Parallelism**.

      docker build -t layers-cut:v1 .
      
![layers](https://github.com/user-attachments/assets/9ac80c92-503d-4ca2-b4b4-3fc80d4c2608)

# 3. Multi-Stage build
Now, use C programming code do multi-stage build Dockerfile. Because Multi-stage build we use depends on use case to use case, for python we don't need of compile but for Java and C/C++ we need compile.

## without Multi-stage build means Single-Stage build :
This is simple C app, & Single-Build Stage Docker file compile & run the app.c
![single-app](https://github.com/user-attachments/assets/d1076e3f-9a30-468d-9a27-b197477a5443)

      docker build -t c-app:v1 -f singleB-Dockerfile .

![build-single-build](https://github.com/user-attachments/assets/5c05b855-ade2-4731-9c1a-c1a1d63f807c)

See the size of image:
![image](https://github.com/user-attachments/assets/4b554d78-1e9d-43a0-a21b-0f0b7ad785fb)

Launch Docker Container:

      docker run -it c-app:v1
      
![run-docker](https://github.com/user-attachments/assets/d19426c9-0233-43ca-be37-233e70306908)


## Using Multi-Build Stage:
Here i use two Build stage, In 1st build stage i use gcc image which is neccessary to compile C-app this image size is very large & then i use ubuntu image which is small and also have C runtime to run C-app.

![Dockerfile](https://github.com/user-attachments/assets/9649b271-8393-49b6-bd80-6aef0d5798fe)

     docker build -t multic-app:v1 -f multiB-Dockerfile --no-cache .

![multi-build](https://github.com/user-attachments/assets/4743de1c-e8c0-4890-80be-777992bff4c1)

see very small size we found.
![image-size](https://github.com/user-attachments/assets/211ce201-5f87-4df1-a926-9a42e3d4f965)

     docker run multic-app:v1
     
![run-multistage](https://github.com/user-attachments/assets/b6a04125-f234-47a9-a9cb-85017b685171)

# 4. Distroless image:
This images do not include anything from any distribution; They provide only bare minimum, such as the C runtime that we need.
(Serch on google: distroless images --> Distroless" Container Images. - GitHub)

     docker build -t distroless-app:v1 -f  ditroless-Dockerfile .

![distroless-build](https://github.com/user-attachments/assets/4b84df6d-0e65-4ef9-9832-694b57cba6a3)

      docker images distroless-app:v1
![Size-of-image](https://github.com/user-attachments/assets/ecdc70ee-4dbd-4bea-b033-49b70c9a3709)

      docker run -it distroless-app:v1

![run-cmd](https://github.com/user-attachments/assets/b179d78d-8b8b-4b9e-b014-ac3b77ea8059)

# 5. Alpine image:
This images size is very small & you can install the runtime or program that you neeed in that image.(Search on DockerHub)

    docker build -t alpine-app:v1 -f alpine-Dockerfile:v1 .

![alpine-build](https://github.com/user-attachments/assets/938b1944-0059-41fa-9c8c-a5823be48140)

Image size is very small:
![alpine-image-size](https://github.com/user-attachments/assets/1ff8ea01-b439-487e-ade7-8846ccc60373)

     docker run -it alpine-app:v1

![run-cmd-alpine](https://github.com/user-attachments/assets/17065b10-da95-4f6f-b0a2-e1c81d525303)

# 6. Scratch image:
Scratch image is smallest image ever.

