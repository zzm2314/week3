# docker_ex2/frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app

# 拷贝依赖并安装
COPY package.json package-lock.json* ./
RUN npm install

COPY . .

EXPOSE 3000

# 开发时使用 CRA 的 dev server，能实时热重载
CMD ["npm", "start"]
