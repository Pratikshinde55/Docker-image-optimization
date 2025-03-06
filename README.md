# Docker-image-optimization

## Image Optimization:
- When we run a Container from an image, It gets loaded into RAM. This means that if image size is large the entire large of data is loaded into RAM.
- If image is large, it gets more time to load inti RAM, which in turn increases the time required to launch Container.
- The image size directly impacks performance.
- A large image size image size results in higher CPU & RAM usage, leading to increase costs.


## Some Image Optimization methods:
1. **Build Tool**
2. **Iamge layering**
3. **Scratch & Alpine image**
4. **Multi-Stage Build**

## 1: [Docker Build tool]

Use old docker build tool :

      export DOCKER_BUILDKIT=0

![build-tool0](https://github.com/user-attachments/assets/1aa82799-a044-4680-b3ef-4d909b20e40e)

      docker build -t old-flask:v1 .
      
![build-old-buildtool](https://github.com/user-attachments/assets/92d5f649-c535-4850-ad55-3570505e33ea)
![Build-0](https://github.com/user-attachments/assets/4199fb7d-df50-4f83-8ab6-1896707b9777)
