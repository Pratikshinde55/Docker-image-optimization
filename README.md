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

## without Multi-stage build :
This is simple C app, & Single-Build Stage Docker file compile & run the app.c
![single-app](https://github.com/user-attachments/assets/d1076e3f-9a30-468d-9a27-b197477a5443)

      docker build -t c-app:v1 -f singleB-Dockerfile .

![build-single-build](https://github.com/user-attachments/assets/5c05b855-ade2-4731-9c1a-c1a1d63f807c)

See the size of image:
![image](https://github.com/user-attachments/assets/4b554d78-1e9d-43a0-a21b-0f0b7ad785fb)

Launch Docker Container:

      docker run -it c-app:v1
      
![image](https://github.com/user-attachments/assets/d19426c9-0233-43ca-be37-233e70306908)





