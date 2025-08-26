# ===== Build Stage =====
FROM node:20-alpine AS builder

WORKDIR /app

ARG VITE_MODE=production

# RUN corepack enable   # yarn

COPY package*.json ./
# COPY package.json yarn.lock ./   # yarn

RUN npm install
# RUN yarn install --frozen-lockfile   # yarn

COPY . .

RUN npm run build -- --mode $VITE_MODE
# RUN yarn build -- --mode $VITE_MODE   # yarn

# ===== Production Stage =====
FROM nginx:1.25-alpine

COPY --from=builder /app/dist /usr/share/nginx/html
# COPY nginx.conf /etc/nginx/conf.d/default.conf   # Override nginx.conf to support front-end routing

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
