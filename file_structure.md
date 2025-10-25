```bash
/src
  /modules
    /auth
      types.ts                      # GraphQL types and input definitions for Auth
      resolvers.ts                  # Auth GraphQL query/mutation resolvers
      service.ts                    # Auth business logic (OAuth2, JWT, token mgmt)
      utils.ts                      # Auth utilities (password hashing, middleware)
    
    /users
      types.ts                      # User GraphQL types and inputs
      resolvers.ts                  # User profile, preferences resolvers
      service.ts                    # User business logic
    
    /goals
      types.ts                      # Goal GraphQL types
      resolvers.ts                  # Goal queries and mutations resolvers
      service.ts                    # Goal creation, updating, AI input refinement
    
    /goal-decomposition
      types.ts                      # Types for decomposition outputs
      resolvers.ts                  # Decomposition related resolvers
      service.ts                    # AI-powered goal breakdown logic
    
    /tasks
      types.ts                      # Task types and inputs
      resolvers.ts                  # Task scheduling and management resolvers
      service.ts                    # Task CRUD and scheduling logic
    
    /task-sharing
      types.ts                      # Sharing permission types
      resolvers.ts                  # Task sharing resolvers
      service.ts                    # Role-based permission logic
    
    /task-interaction
      types.ts                      # Task comments, replies types
      resolvers.ts                  # Real-time interaction resolvers
      service.ts                    # Commenting, progress update business logic
    
    /notifications
      types.ts                      # Notification types
      resolvers.ts                  # Notification management resolvers
      service.ts                    # Push/email adaptive notification logic
    
    /analytics
      types.ts                      # Analytics dashboard and progress insight types
      resolvers.ts                  # Analytics data resolvers
      service.ts                    # Completion trends, streaks, history logic
    
    /ai-coaching
      types.ts                      # AI coaching input/output types
      resolvers.ts                  # Coaching related resolvers
      service.ts                    # AI task reprioritization and motivation logic

  /common
    validators.ts             # Shared input validation functions used across modules
    errorHandlers.ts          # Custom error types and centralized error handling utilities
    logger.ts                 # Logging utilities (winston, pino) for consistent logs
    helpers.ts                # Misc helper functions usable anywhere
    authMiddleware.ts         # Express or Apollo Server auth middleware (JWT verification, etc.)

  /database
    prismaClient.ts           # Prisma Client instance export (singleton)
    migrations/               # Prisma schema migrations files
    seed.ts                   # Seed script for initial or test data population

  /graphql
    schema.ts                 # Root GraphQL schema combining all modules' typeDefs and resolvers
    context.ts                # Context creation for GraphQL resolvers (e.g., Prisma client, auth user)
    directives.ts             # Custom GraphQL directives (e.g., auth, rate-limit)
    scalars.ts                # Custom scalars (Date, JSON, etc.)

  /middleware
    rateLimiter.ts            # Express or Apollo middleware for API rate limiting
    requestLogger.ts          # Middleware for logging request/response details
    errorHandler.ts           # Middleware for Express error handling

  /config
    index.ts                  # Central config loader reading env variables and secrets
    redisConfig.ts            # Redis connection options and setup config
    dbConfig.ts               # Database config and connection pooling options

  /redis
    client.ts                 # Redis client instance export
    cache.ts                  # Cache helper functions (get, set, invalidate) with TTL

  /tests
    /modules                  # Integration and unit tests split by module (auth, users, goals, etc.)
    /common                   # Tests for shared utilities and middlewares

  /scripts
    migrate.sh                # Shell scripts or npm scripts to run prisma migrations sequentially
    seed.sh                   # Scripts to populate seed data
    monitor.sh                # Optional scripts for monitoring and diagnostics

/prisma
  schema.prisma           # The main Prisma schema defining your PostgreSQL models, relations
  migrations/             # Auto-generated migration files by Prisma Migrate
  seed.ts                 # Optional Prisma seed script to populate initial DB data
```