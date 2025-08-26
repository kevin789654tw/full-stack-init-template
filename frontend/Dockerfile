# ===== Build Stage =====
FROM node:20-alpine AS builder

WORKDIR /app

ARG VITE_MODE=production
ARG PACKAGE_MANAGER=npm

COPY package*.json yarn.lock* ./
RUN if [ "$PACKAGE_MANAGER" = "npm" ]; then \
      npm install; \
    else \
      corepack enable && yarn install --frozen-lockfile; \
    fi

COPY . .
RUN if [ "$PACKAGE_MANAGER" = "npm" ]; then \
      npm run build -- --mode $VITE_MODE; \
    else \
      yarn build -- --mode $VITE_MODE; \
    fi

# ===== Production Stage =====
FROM nginx:1.25-alpine

COPY --from=builder /app/dist /usr/share/nginx/html
# COPY nginx.conf /etc/nginx/conf.d/default.conf   # Override nginx.conf to support front-end routing

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
