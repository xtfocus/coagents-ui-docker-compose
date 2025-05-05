FROM node:20-slim

# Opt out of telemetry
ENV NEXT_TELEMETRY_DISABLED=1

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy application code
COPY . .

# Build Next.js application
RUN pnpm build

# Expose default Next.js port
EXPOSE 3000

# Run the application
CMD ["pnpm", "start"]
