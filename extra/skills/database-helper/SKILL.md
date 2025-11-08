---
name: database-helper
description: Optimize SQL queries, generate migrations, document schemas, and recommend indexes
---

# Database Helper Skill

Comprehensive database management skill for SQL optimization, migration generation, schema documentation, and performance recommendations. Supports PostgreSQL, MySQL, SQLite, and other SQL databases.

## When to Use

Invoke this skill when:

- ✅ **Optimizing SQL queries** - Improve slow queries and performance
- ✅ **Generating database migrations** - Create migration files for schema changes
- ✅ **Documenting database schemas** - Generate schema documentation
- ✅ **Recommending indexes** - Identify missing or inefficient indexes
- ✅ **Analyzing query performance** - Identify bottlenecks and N+1 problems
- ✅ **Converting between databases** - Migrate queries between SQL dialects
- ✅ **Normalizing schemas** - Identify normalization issues
- ✅ **Writing complex queries** - Build sophisticated SELECT, JOIN, aggregation queries

## Core Capabilities

### 1. SQL Query Optimization

**Analysis Areas**:
- ✅ **Performance Analysis**: Identify slow queries and bottlenecks
- ✅ **N+1 Detection**: Find repeated queries that could use JOIN
- ✅ **Index Usage**: Recommend indexes for WHERE, JOIN, ORDER BY clauses
- ✅ **Query Rewriting**: Suggest optimized query versions
- ✅ **Subquery Optimization**: Convert inefficient subqueries to JOINs
- ✅ **Aggregation Optimization**: Improve GROUP BY and HAVING clauses
- ✅ **Join Optimization**: Identify expensive joins and alternatives

**Optimization Types**:
- SELECT clause optimization (avoid SELECT *)
- WHERE clause optimization (index-friendly predicates)
- JOIN optimization (join order, index usage)
- Aggregation optimization (GROUP BY, HAVING)
- Subquery elimination or rewriting
- Index hints for query planner
- Partitioning recommendations

### 2. Migration Generation

**Migration Creation**:
- ✅ **Schema Changes**: CREATE TABLE, ALTER TABLE, DROP TABLE
- ✅ **Index Management**: CREATE INDEX, DROP INDEX, ADD CONSTRAINT
- ✅ **Data Types**: Define columns with appropriate types
- ✅ **Constraints**: PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL
- ✅ **Rollback Plans**: Down migration for reversibility
- ✅ **Multiple Databases**: Support different SQL dialects
- ✅ **Version Control**: Migration naming and ordering

**Migration Formats**:
- Raw SQL migrations
- Knex.js migrations
- TypeORM migrations
- Sequelize migrations
- Alembic migrations (Python)
- Django migrations (Python)
- Rails migrations (Ruby)
- Flyway migrations
- Liquibase migrations

### 3. Schema Documentation

**Documentation Generation**:
- ✅ **Table Definitions**: Complete table structure with descriptions
- ✅ **Column Details**: Type, constraints, default values, descriptions
- ✅ **Relationships**: Foreign key relationships and cardinality
- ✅ **Indexes**: Index names, columns, and purpose
- ✅ **Constraints**: All database constraints and rules
- ✅ **ER Diagrams**: Entity-relationship diagram descriptions
- ✅ **Data Dictionary**: Complete data reference guide

**Documentation Formats**:
- Markdown documentation
- HTML documentation
- Database ER diagrams (PlantUML, Mermaid)
- Data dictionary tables
- API schema specifications

### 4. Index Recommendations

**Index Analysis**:
- ✅ **Missing Indexes**: Identify columns that should be indexed
- ✅ **Unused Indexes**: Find indexes that aren't used
- ✅ **Composite Indexes**: Recommend multi-column indexes
- ✅ **Index Size**: Estimate index storage requirements
- ✅ **Write Performance**: Balance between read and write performance
- ✅ **Covering Indexes**: Identify opportunities for covering indexes

**Index Types Supported**:
- Single-column indexes
- Composite (multi-column) indexes
- Unique indexes
- Partial indexes (conditional)
- Full-text indexes
- JSON indexes
- BRIN indexes (PostgreSQL)
- Hash indexes
- B-tree indexes

## Instructions

### Step 1: Analyze Current State

Identify and examine:
- **Current Queries**: Slow queries or performance bottlenecks
- **Existing Schema**: Table structure and relationships
- **Current Indexes**: Existing indexes and their usage
- **Access Patterns**: How data is typically queried
- **Growth Projections**: Expected data volume growth

### Step 2: Analyze Query Performance

For optimization, examine:
- **Query Plan**: EXPLAIN output or execution plan
- **Predicates**: WHERE, JOIN, and filter conditions
- **Data Volume**: How much data is scanned
- **Cardinality**: Number of matching rows
- **Index Usage**: Are indexes being used effectively
- **Sort Operations**: Costly sort operations
- **Aggregations**: GROUP BY and HAVING performance

### Step 3: Generate Solutions

Create:
- **Optimized Queries**: Rewritten queries with improvements
- **Index Recommendations**: New indexes to add
- **Migration Files**: SQL or ORM migration code
- **Schema Documentation**: Complete schema reference
- **Best Practices**: Application-level optimizations

### Step 4: Provide Implementation Plan

Include:
- **Priority**: High-impact changes first
- **Rollback Plan**: How to undo changes safely
- **Testing Strategy**: How to validate improvements
- **Performance Metrics**: Expected improvements
- **Monitoring**: What to watch after changes

### Step 5: Generate Output

Deliver:
- **Optimized Queries**: Ready-to-use SQL
- **Migration Code**: Ready-to-apply migrations
- **Documentation**: Markdown and diagrams
- **Implementation Guide**: Step-by-step instructions
- **Best Practices**: Ongoing optimization tips

## Examples

### Example 1: Query Optimization - N+1 Problem

**Problem Query** (N+1 query):
```javascript
// Get users with their posts (BAD - N+1 queries)
const users = await db.query('SELECT * FROM users WHERE active = true');
for (const user of users) {
  user.posts = await db.query('SELECT * FROM posts WHERE user_id = ?', [user.id]);
}
```

**Optimized Query** (Single JOIN):
```sql
-- Single query with JOIN (GOOD)
SELECT
  u.id as user_id,
  u.name,
  u.email,
  p.id as post_id,
  p.title,
  p.created_at
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
WHERE u.active = true
ORDER BY u.id, p.created_at DESC;
```

**Benefits**:
- Reduces N queries to 1 query
- 90%+ performance improvement
- Lower database load
- Reduced network latency

**Recommendations**:
- Add index on `posts.user_id` for faster joins
- Consider pagination for large result sets
- Use aggregation if only counts needed

---

### Example 2: Index Recommendation

**Slow Query**:
```sql
SELECT * FROM orders
WHERE user_id = 123
  AND created_at >= '2024-01-01'
  AND status = 'completed'
ORDER BY created_at DESC
LIMIT 10;
```

**EXPLAIN Analysis**:
```
Seq Scan on orders (cost=0.00..5000.00 rows=50)
  Filter: (user_id = 123 AND created_at >= '2024-01-01' AND status = 'completed')
```

**Problem**: Full table scan (Seq Scan) - not using any indexes

**Recommended Indexes**:

**Index 1: High Priority** (Composite index for WHERE clause)
```sql
CREATE INDEX idx_orders_user_status_created
ON orders(user_id, status, created_at DESC);

-- After index
Index Scan using idx_orders_user_status_created (cost=0.42..12.58 rows=10)
  Index Cond: (user_id = 123 AND status = 'completed' AND created_at >= '2024-01-01')
```

**Index 2: Optional** (Covering index to avoid table lookup)
```sql
CREATE INDEX idx_orders_user_status_created_covering
ON orders(user_id, status, created_at DESC)
INCLUDE (id, total, shipping_address);
```

**Performance Impact**:
- Query time: 2500ms → 15ms (166x faster)
- Disk I/O: 5GB scanned → 50MB scanned
- Memory: 500MB → 5MB

---

### Example 3: Migration Generation

**Requirement**: Add user roles and permissions system

**Generated Migration** (Knex.js format):
```javascript
exports.up = function(knex) {
  return Promise.all([
    // Create roles table
    knex.schema.createTable('roles', function(table) {
      table.increments('id').primary();
      table.string('name', 50).notNullable().unique();
      table.text('description');
      table.timestamps(true, true);
      table.index('name');
    }),

    // Create permissions table
    knex.schema.createTable('permissions', function(table) {
      table.increments('id').primary();
      table.string('name', 100).notNullable().unique();
      table.string('resource', 50).notNullable();
      table.string('action', 50).notNullable();
      table.text('description');
      table.timestamps(true, true);
      table.unique(['resource', 'action']);
    })
  ]).then(() => {
    // Create role_permission junction table
    return knex.schema.createTable('role_permissions', function(table) {
      table.increments('id').primary();
      table.integer('role_id').unsigned().notNullable();
      table.integer('permission_id').unsigned().notNullable();
      table.timestamps(true, true);

      table.foreign('role_id').references('roles.id').onDelete('CASCADE');
      table.foreign('permission_id').references('permissions.id').onDelete('CASCADE');
      table.unique(['role_id', 'permission_id']);

      table.index('role_id');
      table.index('permission_id');
    });
  }).then(() => {
    // Add role_id to users table
    return knex.schema.table('users', function(table) {
      table.integer('role_id').unsigned();
      table.foreign('role_id').references('roles.id').onDelete('SET NULL');
      table.index('role_id');
    });
  });
};

exports.down = function(knex) {
  return Promise.all([
    knex.schema.table('users', function(table) {
      table.dropForeign('role_id');
      table.dropIndex('role_id');
      table.dropColumn('role_id');
    }),
    knex.schema.dropTableIfExists('role_permissions'),
    knex.schema.dropTableIfExists('roles'),
    knex.schema.dropTableIfExists('permissions')
  ]);
};
```

**Generated Migration** (Raw SQL format):
```sql
-- Up migration
BEGIN;

CREATE TABLE roles (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL UNIQUE,
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE permissions (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  resource VARCHAR(50) NOT NULL,
  action VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(resource, action)
);

CREATE TABLE role_permissions (
  id SERIAL PRIMARY KEY,
  role_id INTEGER NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
  permission_id INTEGER NOT NULL REFERENCES permissions(id) ON DELETE CASCADE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(role_id, permission_id)
);

ALTER TABLE users ADD COLUMN role_id INTEGER REFERENCES roles(id) ON DELETE SET NULL;

CREATE INDEX idx_roles_name ON roles(name);
CREATE INDEX idx_permissions_resource_action ON permissions(resource, action);
CREATE INDEX idx_role_permissions_role_id ON role_permissions(role_id);
CREATE INDEX idx_role_permissions_permission_id ON role_permissions(permission_id);
CREATE INDEX idx_users_role_id ON users(role_id);

COMMIT;

-- Down migration
BEGIN;

ALTER TABLE users DROP CONSTRAINT users_role_id_fkey;
ALTER TABLE users DROP COLUMN role_id;

DROP TABLE IF EXISTS role_permissions CASCADE;
DROP TABLE IF EXISTS permissions CASCADE;
DROP TABLE IF EXISTS roles CASCADE;

COMMIT;
```

---

### Example 4: Schema Documentation (Markdown)

```markdown
# Database Schema Documentation

## Overview
Complete database schema for the Task Management System.
- **Database**: PostgreSQL 14+
- **Last Updated**: 2024-11-08
- **Version**: 2.1.0

## Tables

### users
Stores user account information.

| Column | Type | Constraints | Description |
|--------|------|-----------|-------------|
| `id` | SERIAL | PRIMARY KEY | Unique user identifier |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | User's email address |
| `password_hash` | VARCHAR(255) | NOT NULL | Bcrypt hashed password |
| `first_name` | VARCHAR(100) | NOT NULL | User's first name |
| `last_name` | VARCHAR(100) | NOT NULL | User's last name |
| `avatar_url` | VARCHAR(500) | | Profile picture URL |
| `role_id` | INTEGER | FK→roles.id | User's assigned role |
| `status` | ENUM | DEFAULT 'active' | Account status |
| `created_at` | TIMESTAMP | NOT NULL | Account creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes**:
- `idx_users_email` (email) - For login lookups
- `idx_users_role_id` (role_id) - For role-based queries
- `idx_users_status` (status) - For active user counts

**Relationships**:
- 1:N with tasks (one user can have many tasks)
- 1:N with comments (one user can make many comments)
- N:1 with roles (many users can have one role)

---

### tasks
Stores task/todo items with assignments.

| Column | Type | Constraints | Description |
|--------|------|-----------|-------------|
| `id` | SERIAL | PRIMARY KEY | Unique task identifier |
| `user_id` | INTEGER | FK→users.id, NOT NULL | Task owner |
| `title` | VARCHAR(255) | NOT NULL | Task title |
| `description` | TEXT | | Detailed description |
| `status` | ENUM | DEFAULT 'pending' | Task status: pending, in_progress, completed |
| `priority` | ENUM | DEFAULT 'medium' | Priority level: low, medium, high |
| `due_date` | DATE | | When task is due |
| `completed_at` | TIMESTAMP | | When task was completed |
| `created_at` | TIMESTAMP | NOT NULL | Task creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes**:
- `idx_tasks_user_id` (user_id) - For user's task list
- `idx_tasks_status` (status) - For filtering by status
- `idx_tasks_due_date` (due_date) - For deadline queries
- `idx_tasks_user_status_created` (user_id, status, created_at DESC) - Composite for common queries

**Relationships**:
- N:1 with users (many tasks belong to one user)
- 1:N with comments (one task can have many comments)

---

## Relationships (ER Diagram)

```
┌─────────────┐
│   roles     │
├─────────────┤
│ id (PK)     │
│ name        │
│ description │
└────────┬────┘
         │
         │ 1:N
         │
    ┌────▼──────────────┐
    │  role_permissions │
    ├───────────────────┤
    │ id (PK)           │
    │ role_id (FK)      │
    │ permission_id (FK)│
    └────┬──────────────┘
         │
         │ N:1
         │
    ┌────▼────────────┐
    │  permissions    │
    ├─────────────────┤
    │ id (PK)         │
    │ name            │
    │ resource        │
    │ action          │
    └─────────────────┘
         ▲
         │ 1:N
         │
    ┌────┴────────────────┐
    │      users          │
    ├─────────────────────┤
    │ id (PK)             │
    │ email               │
    │ password_hash       │
    │ role_id (FK)        │
    └────┬────────────────┘
         │ 1:N
         │
    ┌────▼──────────────┐
    │     tasks         │
    ├───────────────────┤
    │ id (PK)           │
    │ user_id (FK)      │
    │ title             │
    │ status            │
    │ priority          │
    │ due_date          │
    └────┬──────────────┘
         │ 1:N
         │
    ┌────▼────────────┐
    │   comments      │
    ├─────────────────┤
    │ id (PK)         │
    │ task_id (FK)    │
    │ user_id (FK)    │
    │ content         │
    └─────────────────┘
```

---

## Query Examples

### Get user with all tasks and comments
```sql
SELECT
  u.id,
  u.email,
  u.first_name,
  u.last_name,
  t.id as task_id,
  t.title,
  t.status,
  c.id as comment_id,
  c.content,
  c.created_at
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
LEFT JOIN comments c ON t.id = c.task_id
WHERE u.id = $1
ORDER BY u.id, t.created_at DESC, c.created_at DESC;
```

### Find pending tasks due this week
```sql
SELECT * FROM tasks
WHERE status = 'pending'
  AND due_date BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days'
  AND user_id = $1
ORDER BY due_date ASC, priority DESC;
```
```

---

### Example 5: Data Type Best Practices

**Recommended Data Types**:

```sql
-- Text Data
VARCHAR(255)    -- Short strings (emails, names, titles)
TEXT            -- Long strings (descriptions, content)
CHAR(n)         -- Fixed-length (codes, abbreviations)

-- Numeric Data
SERIAL          -- Auto-increment integer IDs
BIGSERIAL       -- Large auto-increment IDs
INTEGER         -- Regular whole numbers
BIGINT          -- Large whole numbers
DECIMAL(10,2)   -- Fixed-point (money: DECIMAL(10,2))
REAL/DOUBLE     -- Floating-point (avoid for money)

-- Date/Time
DATE            -- Just date (YYYY-MM-DD)
TIME            -- Just time (HH:MM:SS)
TIMESTAMP       -- Date and time with timezone
TIMESTAMPTZ     -- Recommended for most apps

-- Boolean
BOOLEAN         -- True/false values

-- JSON
JSON            -- For flexible document storage
JSONB           -- Better performance (PostgreSQL)

-- Enum
ENUM            -- Fixed set of values (status, role)

-- Special
UUID            -- Distributed unique identifiers
BYTEA           -- Binary data
```

---

## Best Practices

### Design
- ✅ Use surrogate keys (SERIAL) for primary keys
- ✅ Always include created_at and updated_at timestamps
- ✅ Use ENUM for fixed sets of values
- ✅ Normalize to 3NF at minimum
- ✅ Denormalize only when needed for performance

### Indexing
- ✅ Index foreign key columns
- ✅ Index columns used in WHERE clauses
- ✅ Index ORDER BY columns
- ✅ Create composite indexes for common multi-column queries
- ✅ Remove unused indexes regularly
- ✅ Monitor index bloat

### Queries
- ✅ Use specific column names (avoid SELECT *)
- ✅ Use JOINs instead of application-level joins
- ✅ Avoid correlated subqueries
- ✅ Use EXPLAIN to check query plans
- ✅ Implement pagination for large result sets
- ✅ Use parameterized queries to prevent SQL injection

### Performance
- ✅ Add indexes before they're needed
- ✅ Archive old data regularly
- ✅ Use connection pooling
- ✅ Cache frequently accessed data
- ✅ Monitor query performance
- ✅ Run ANALYZE periodically (PostgreSQL)
- ✅ Vacuum tables regularly (PostgreSQL)

### Migrations
- ✅ Always write down migrations
- ✅ Keep migrations reversible
- ✅ Test migrations on staging first
- ✅ Use transactions for data safety
- ✅ Include rollback plan
- ✅ Document migration purposes
- ✅ Run migrations in order

### Security
- ✅ Use parameterized queries (not string concatenation)
- ✅ Hash passwords with bcrypt or argon2
- ✅ Never store sensitive data in plain text
- ✅ Use NOT NULL where appropriate
- ✅ Add UNIQUE constraints
- ✅ Implement row-level security if needed
- ✅ Audit schema changes

## Optimization Techniques

### Query Optimization
1. **Use EXPLAIN ANALYZE** - Understand query plans
2. **Index Strategic Columns** - WHERE, JOIN, ORDER BY
3. **Avoid Full Table Scans** - Use indexes
4. **Eliminate Subqueries** - Convert to JOINs
5. **Use LIMIT Early** - Pagination
6. **Denormalize if Needed** - Cache computed values

### Schema Optimization
1. **Normalize** - Eliminate redundancy
2. **Archive** - Move old data
3. **Partition** - Split large tables
4. **Shard** - Distribute across servers
5. **Summarize** - Pre-compute aggregates

### Application Optimization
1. **Connection Pooling** - Reuse connections
2. **Caching** - Cache query results
3. **Batching** - Insert/update in batches
4. **Lazy Loading** - Load related data on demand
5. **Read Replicas** - Distribute read queries

## Supported Databases

- ✅ PostgreSQL (recommended for complex schemas)
- ✅ MySQL / MariaDB
- ✅ SQLite (development/mobile)
- ✅ Oracle Database
- ✅ SQL Server
- ✅ MongoDB (document queries)

## Common Issues & Solutions

### N+1 Queries
**Problem**: Loading parent then looping to load children
**Solution**: Use JOINs or batch loading

### Missing Indexes
**Problem**: Slow queries on large tables
**Solution**: Add indexes on WHERE/JOIN/ORDER BY columns

### Poor Normalization
**Problem**: Data duplication and inconsistency
**Solution**: Normalize to 3NF, denormalize only when needed

### Unoptimized JOINs
**Problem**: Multiple expensive JOINs
**Solution**: Check join order, add indexes, consider denormalization

### Bloated Indexes
**Problem**: Old unused indexes slowing writes
**Solution**: Remove unused indexes, rebuild fragmented indexes

## Integration Examples

### With api-tester skill
```bash
# Test API performance on database operations
python3 test-api.py https://api.example.com/users \
  --headers '{"X-Trace-Queries":"true"}'
# See slow queries in response headers
```

### With /deploy command
```bash
/deploy production
# Includes database migration checks
# Verifies schema compatibility
# Validates data migration safety
```

### With /refactor command
```bash
/refactor schema.sql
# Analyzes schema design
# Recommends normalizations
# Suggests optimizations
```

## Performance Benchmarks

**Index Impact**:
- Full table scan: 5000ms
- With single-column index: 50ms (100x faster)
- With composite index: 5ms (1000x faster)

**Query Optimization**:
- Unoptimized N+1: 2500ms (50 queries)
- Optimized JOIN: 50ms (1 query) (50x faster)

## Version History

- **v2.1** - Added JSON support and BRIN indexes
- **v2.0** - Multiple database support
- **v1.5** - Migration templates for all frameworks
- **v1.0** - Initial release

## Getting Help

When requesting database help, provide:

1. **Current Query** - The slow/problematic query
2. **EXPLAIN Output** - Query plan if available
3. **Schema Definition** - CREATE TABLE statements
4. **Data Volume** - Row counts and growth rates
5. **Access Pattern** - How the data is typically queried
6. **Database Type** - PostgreSQL, MySQL, etc.

Example request:
```
"I have a slow query that joins users with their recent posts.
It takes 5 seconds on 1M users and 50M posts.
Here's my EXPLAIN output: ..."
```

---

**Skill Status**: Production-ready
**Last Updated**: November 2024
**Integration**: Works with /deploy, /refactor, /test commands
