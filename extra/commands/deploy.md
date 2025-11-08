---
description: "Prepare and deploy project with comprehensive pre-deployment checks"
argument-hint: "[environment]"
---

# Deploy Project

Comprehensive deployment automation that validates code quality, builds the project, checks environment configuration, and creates a deployment checklist to ensure safe, reliable deployments.

## Command Syntax

```
/deploy [environment]
```

## Arguments

- **environment** (optional): Target deployment environment
  - `development` - Local development environment
  - `staging` - Pre-production staging environment
  - `production` - Production environment (requires confirmation)
  - Defaults to `staging` if not specified

## Examples

```
/deploy
/deploy development
/deploy staging
/deploy production
```

## What This Command Does

### 1. Run Test Suite

Validates code quality and functionality:

#### Unit Tests
```bash
npm test              # Run all unit tests
npm run test:unit     # If configured
jest --verbose        # Detailed test output
```

Checks:
- ✅ All unit tests pass
- ✅ No test timeouts
- ✅ 100% assertion success
- ✅ No skipped tests (⏭️)
- ✅ No pending tests (⏱️)

#### Integration Tests
```bash
npm run test:integration   # If configured
```

Checks:
- ✅ Component interactions work
- ✅ Data flows correctly
- ✅ External dependencies mock properly
- ✅ API endpoints respond correctly

#### Coverage Report
```bash
npm run test:coverage      # If configured
jest --coverage            # Coverage metrics
```

Target Coverage:
- ✅ Statements: > 80%
- ✅ Branches: > 75%
- ✅ Functions: > 80%
- ✅ Lines: > 80%

**Failure Action**: Stops deployment if tests fail

### 2. Build the Project

Compiles and bundles the code:

#### Compilation
```bash
npm run build          # Standard build
npm run build:prod     # Production build
npm run compile        # TypeScript compilation
```

Build Checks:
- ✅ No compilation errors
- ✅ No warnings (or acceptable warnings)
- ✅ All imports resolve
- ✅ Output directory created
- ✅ Build artifacts present

#### Production Optimization
```bash
npm run build:prod     # Production-optimized build
npm run minify         # Code minification
npm run bundle         # Bundle analysis
```

Optimizations:
- ✅ Code minification
- ✅ Tree shaking
- ✅ Source maps generated
- ✅ Asset optimization
- ✅ Bundle size analysis

#### Build Validation
Checks build output:
- ✅ All entry points compiled
- ✅ No broken imports
- ✅ Assets accessible
- ✅ Configuration loaded
- ✅ Environment variables interpolated

**Failure Action**: Stops deployment if build fails

### 3. Check Environment Variables

Validates configuration requirements:

#### Required Variables Check
```
CHECKING ENVIRONMENT VARIABLES...

Development Environment:
  ✅ NODE_ENV = development
  ✅ DEBUG = true
  ✅ PORT = 3000

Staging Environment:
  ✅ NODE_ENV = staging
  ✅ DATABASE_URL = postgres://...
  ✅ API_KEY = sk_test_...
  ⚠️  ENCRYPTION_KEY = (set but not shown)

Production Environment:
  ✅ NODE_ENV = production
  ✅ DATABASE_URL = postgres://...
  ✅ API_KEY = sk_live_...
  ✅ ENCRYPTION_KEY = (set but not shown)
  ✅ JWT_SECRET = (set but not shown)
  ✅ REDIS_URL = redis://...
```

#### Environment-Specific Validations

**Development**
- ✅ DEBUG mode enabled
- ✅ Mock services configured
- ✅ Logging enabled
- ✅ Development database connected

**Staging**
- ✅ Real API keys configured
- ✅ Database connected
- ✅ Email service ready
- ✅ SSL certificates valid
- ✅ External services accessible

**Production**
- ✅ Production API keys (not test keys)
- ✅ Production database connected
- ✅ Secure communication enabled
- ✅ All secrets configured
- ✅ Backup systems ready
- ✅ Monitoring enabled
- ✅ Error tracking configured

#### Configuration Sources
Checks for variables from:
- `.env` files
- Environment variables
- Secrets manager
- Configuration server
- Parameter store

#### Missing Variables Report
```
⚠️  MISSING ENVIRONMENT VARIABLES

Required for production:
  ❌ PAYMENT_API_KEY
  ❌ STRIPE_SECRET
  ❌ SENDGRID_API_KEY

Optional (with defaults):
  ⚠️  CACHE_TTL (will use default: 3600)
  ⚠️  LOG_LEVEL (will use default: info)
```

**Failure Action**: Stops production deployment if critical variables missing

### 4. Create Deployment Checklist

Generates comprehensive pre-deployment checklist:

#### Pre-Deployment Checklist
```
📋 DEPLOYMENT CHECKLIST
═══════════════════════════════════════════════════

🧪 CODE QUALITY
  ☐ All tests passing (npm test)
  ☐ No linting errors (npm run lint)
  ☐ Code coverage adequate (> 80%)
  ☐ No security vulnerabilities (npm audit)
  ☐ No deprecated dependencies

🔨 BUILD & COMPILATION
  ☐ Build completes without errors
  ☐ No console errors or warnings
  ☐ All assets included
  ☐ Source maps generated
  ☐ Bundle size acceptable
  ☐ No dead code

🔐 SECURITY
  ☐ Secrets not committed to repo
  ☐ API keys are environment variables
  ☐ HTTPS enabled for production
  ☐ CORS properly configured
  ☐ SQL injection prevention verified
  ☐ XSS protections enabled
  ☐ Authentication working
  ☐ Authorization enforced

⚙️  CONFIGURATION
  ☐ Environment variables set (.env)
  ☐ Database connection verified
  ☐ API endpoints configured
  ☐ Service credentials available
  ☐ Logging configured
  ☐ Error tracking enabled
  ☐ Monitoring set up

📊 DEPLOYMENT PREPARATION
  ☐ Database migrations prepared
  ☐ Backup created
  ☐ Rollback plan documented
  ☐ Deployment window scheduled
  ☐ Team notified
  ☐ On-call support ready

✅ FINAL CHECKS
  ☐ Feature flags configured
  ☐ Analytics tracking enabled
  ☐ Documentation updated
  ☐ Deployment notes written
  ☐ Sign-off from team lead
```

#### Dynamic Checklist Generation
Based on project type:

**Node.js/Express API**
- ✅ API endpoints tested
- ✅ Database migrations ready
- ✅ Rate limiting configured
- ✅ Error handlers in place

**React/Frontend**
- ✅ Bundle size optimized
- ✅ Performance metrics good
- ✅ Service worker updated
- ✅ CDN cache invalidated

**Full Stack**
- ✅ Both frontend and backend checks
- ✅ Integration tests pass
- ✅ Database schema updated
- ✅ API contracts verified

#### Risk Assessment
```
⚠️  DEPLOYMENT RISK ASSESSMENT

Risk Level: MEDIUM

Factors:
  🟢 Tests: ALL PASSING (low risk)
  🟢 Build: SUCCESSFUL (low risk)
  🟡 Changes: 45 files modified (medium risk)
  🟢 Database: NO MIGRATIONS (low risk)
  🔴 Environment: 3 vars missing (high risk)

Recommendations:
  1. Set missing environment variables
  2. Deploy during off-peak hours
  3. Have rollback ready
  4. Monitor error tracking closely
  5. Check application logs
```

#### Deployment Notes Template
```
📝 DEPLOYMENT NOTES

Version: 2.1.0
Date: 2024-11-08
Deployed By: [Your Name]

Changes Included:
- Fix: Critical bug in user authentication
- Feature: New email notification system
- Refactor: Database query optimization

Breaking Changes: None

Database Changes:
- Migration: add_notification_preferences table

Environment Changes:
- New: SENDGRID_API_KEY required
- Updated: DATABASE_URL for new replica

Rollback Plan:
1. Use previous docker image: app:2.0.9
2. Database rollback: migrate down 3 steps
3. Clear CDN cache
4. Monitor error rates

Testing Checklist:
- ☐ User login works
- ☐ Email notifications send
- ☐ Dashboard loads
- ☐ API endpoints respond
```

### 5. Deployment Execution

#### Pre-Deployment Summary
```
═══════════════════════════════════════════════════
           DEPLOYMENT SUMMARY
═══════════════════════════════════════════════════

📦 PROJECT: task-management-api
🎯 TARGET: production
📅 TIME: 2024-11-08 14:30:00 UTC

✅ TEST RESULTS
   Unit Tests: 45 passed, 0 failed
   Integration Tests: 12 passed, 0 failed
   Coverage: 87% statements

✅ BUILD STATUS
   Compilation: SUCCESS
   Bundle Size: 2.3 MB (within limits)
   Assets: All included

⚠️  CONFIGURATION CHECK
   Database: Connected (production-db)
   API Keys: All set
   Secrets: All configured
   Missing Variables: 0

📋 NEXT STEPS
   1. Review deployment checklist
   2. Confirm database backup
   3. Approve deployment
   4. Monitor application
   5. Verify functionality

Ready to deploy? (yes/no)
```

#### Deployment Confirmation
- Requires explicit confirmation for production
- Shows all checks that passed/failed
- Displays any warnings or concerns
- Provides rollback instructions

## Environment Configurations

### Development
```bash
/deploy development
```
- Fast feedback loop
- Tests run with coverage
- Build can have warnings
- Mock services used
- Full debugging enabled

### Staging
```bash
/deploy staging
```
- Production-like environment
- Real API keys (test accounts)
- Full test suite required
- Build optimization enabled
- Monitoring enabled

### Production
```bash
/deploy production
```
- Strictest checks
- 100% test success required
- Zero build warnings
- Real credentials required
- Explicit confirmation needed
- Comprehensive logging
- Error tracking mandatory

## Safety Features

### Pre-Flight Checks
- ✅ Branch is clean (no uncommitted changes)
- ✅ Branches are synced (latest from remote)
- ✅ Current branch is deployable (main/master)
- ✅ Tag created for version

### Automatic Backups
```bash
# Database backup
npm run backup:db

# Configuration backup
cp -r config config.backup.${date}

# Current version backup
docker tag app:latest app:2.0.8
```

### Rollback Ready
```bash
# Automatic rollback instructions created
# If deployment fails, easy rollback available
git revert <commit>
docker rollback app:2.0.8
```

### Monitoring Post-Deploy
```bash
# Automatic checks after deployment:
- Health endpoint responds
- Core features working
- Error rate normal
- Performance metrics good
```

## Configuration Files

### .deployrc or deploy.config.js
```javascript
{
  "environments": {
    "development": {
      "requires": ["DEBUG", "PORT"],
      "optional": ["LOG_LEVEL"],
      "maxBuildWarnings": 10
    },
    "staging": {
      "requires": ["DATABASE_URL", "API_KEY"],
      "optional": ["CACHE_URL"],
      "minCoverage": 80
    },
    "production": {
      "requires": ["DATABASE_URL", "API_KEY", "JWT_SECRET"],
      "optional": [],
      "minCoverage": 85,
      "requireApproval": true
    }
  }
}
```

### .env.example
```
# Development
DEBUG=true
NODE_ENV=development

# Staging
DATABASE_URL=postgres://user:pass@host/db_staging
API_KEY=sk_test_xxxxx

# Production
JWT_SECRET=<required>
ENCRYPTION_KEY=<required>
STRIPE_SECRET=<required>
SENDGRID_API_KEY=<required>
```

## Integration with CI/CD

### GitHub Actions
```yaml
name: Deploy
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm test
      - run: npm run build
      - run: npm run deploy:staging
```

### GitLab CI
```yaml
deploy:
  stage: deploy
  script:
    - npm test
    - npm run build
    - npm run deploy:$CI_ENVIRONMENT_NAME
  environment: staging
```

## Typical Deployment Workflow

### Step 1: Prepare Code
```bash
# Ensure everything is committed
git add .
git commit -m "feat: new feature"

# Pull latest changes
git pull origin main
```

### Step 2: Run Deploy Command
```bash
/deploy staging
# or
/deploy production
```

### Step 3: Review Information
- Check test results
- Review build output
- Verify environment variables
- Read deployment checklist

### Step 4: Approve and Deploy
```bash
# Confirm deployment
yes

# Automatic deployment happens
# Monitors health checks
# Reports success/failure
```

### Step 5: Verify Deployment
```bash
# Check application health
curl https://api.example.com/health

# Monitor error tracking
# Check application logs
# Verify key features work
```

## Post-Deployment Tasks

### Automatic
- ✅ Health check endpoint
- ✅ Error tracking verification
- ✅ Performance metric baseline
- ✅ Deployment notification sent

### Manual
- ☐ Smoke test key features
- ☐ Check user feedback/support
- ☐ Verify analytics data
- ☐ Monitor error rates
- ☐ Check performance metrics
- ☐ Update deployment log

## Rollback Procedures

### Quick Rollback
```bash
# Immediate rollback if critical issue
/rollback
# or
/rollback previous
```

### Guided Rollback
```bash
# Manual rollback with steps
git revert <commit-hash>
npm run deploy:staging
```

### Database Rollback
```bash
npm run migrate:down 2
# Rolls back 2 database migrations
```

## Key Features

- **Comprehensive**: Tests, build, config, checklist
- **Safe**: Multiple validation layers
- **Automated**: Reduces manual errors
- **Clear**: Detailed output and checklists
- **Flexible**: Works with multiple environments
- **Reversible**: Easy rollback procedures
- **Documented**: Deployment notes template
- **Monitored**: Post-deployment health checks

## Best Practices

### Before Deploying
- ✅ Merge feature branches to main
- ✅ Pull latest from remote
- ✅ Ensure all tests pass locally
- ✅ Review deployment checklist
- ✅ Notify team of deployment
- ✅ Schedule appropriate timing

### During Deployment
- ✅ Monitor deployment progress
- ✅ Watch error tracking
- ✅ Check application logs
- ✅ Verify key features
- ✅ Be ready to rollback

### After Deployment
- ✅ Run smoke tests
- ✅ Monitor error rates
- ✅ Check performance
- ✅ Verify new features
- ✅ Update team
- ✅ Log deployment details

## Troubleshooting

### Tests Fail
```bash
npm test
# Fix failing tests
/deploy staging
```

### Build Fails
```bash
npm run build
# Check compilation errors
# Fix issues
/deploy staging
```

### Missing Environment Variables
```bash
# Add to .env
echo "API_KEY=value" >> .env

# Or set as environment variable
export API_KEY=value

/deploy production
```

### Deployment Blocked
```bash
# Check what's blocking
/deploy --verbose

# Resolve issues
# Try again
/deploy production
```

## See Also

- `/commit` - Commit your changes before deploying
- `/test` - Run tests independently
- `/document` - Document your deployment process
- `/refactor` - Clean code before deployment

## Additional Resources

- **Deployment Guide**: [DEPLOYMENT.md](./DEPLOYMENT.md)
- **Environment Setup**: [.env.example](./.env.example)
- **Rollback Procedures**: [ROLLBACK.md](./ROLLBACK.md)
- **Monitoring Setup**: [MONITORING.md](./MONITORING.md)
