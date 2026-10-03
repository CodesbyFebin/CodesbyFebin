# Schema Markup Validation & Testing Guide

**Last Updated**: October 3, 2026  
**Status**: Ready for Schema Testing  
**Branch**: `claude/codesbyfebin-deploy-puq3a5`  
**Total Schema Objects**: 73 across 7 pages

---

## Quick Validation Summary

- **Schema Types Implemented**: 11 (Organization, WebSite, Person, WebPage, BreadcrumbList, BlogPosting, CollectionPage, FAQPage, ScholarlyArticle, SoftwareApplication, ItemList)
- **Pages with Schema**: 7 (all content pages)
- **Schema Format**: JSON-LD (recommended by Google)
- **Validation Status**: Pending automated testing
- **Expected Result**: All schema valid, eligible for rich snippets

---

## Implemented Schema Types

### Organization Schema (Landing Page)
```
Name: CodesbyFebin
Founder: Febin Francis
Contact: febin@codesbyfebin.com
Social Profiles: GitHub, Twitter, LinkedIn
URL: https://codesbyfebin.vercel.app/
```

### WebSite Schema (Landing Page)
```
Name: CodesbyFebin
URL: https://codesbyfebin.vercel.app/
SearchAction: Site search at /blog/?q={search_term_string}
```

### Person Schema (About Page)
```
Name: Febin Francis
Job Title: Systems Engineer
Location: Kerala, India
Knowledge Areas: Cryptography, Distributed Systems, AI Infrastructure
```

### WebPage Schema (Multiple Pages)
- Landing page
- About page
- Documentation hub
- Enhanced with author and publisher information

### BreadcrumbList Schema (All 7 Pages)
```
Hierarchical navigation:
- Landing: Home
- About: Home → About
- Blog: Home → Blog
- Projects: Home → Projects
- Portfolio: Home → Portfolio
- Docs: Home → Docs
- Research: Home → Research
```

### BlogPosting Schema (Blog Page)
```
Features:
- Headline
- Author (Febin Francis)
- Date Published
- Keywords
- Article Body
- Article Section (optional)
```

### CollectionPage Schema (Hub Pages)
```
Used for:
- Blog index
- Projects index
- Research index
Features: Name, description, URL, publisher
```

### FAQPage Schema (Documentation Hub)
```
Contains: Multiple Question-Answer pairs
Example topics:
1. API documentation location
2. Getting started guide
3. Research papers availability
```

### ScholarlyArticle Schema (Research Page)
```
Features:
- Headline
- Description
- Author (Febin Francis)
- Date Published
- Keywords
- About (Topic)
- Publisher
```

### SoftwareApplication Schema (Featured Systems)
```
Used for:
- rust-stark-zkvm
- Decentralized.host
- Featured projects
Features: Name, description, URL, author, version (optional)
```

### ItemList Schema (Collections)
```
Used for:
- Featured systems (landing)
- Featured projects (projects page)
- Technical skills (portfolio)
Features: Item names, descriptions, positions
```

---

## Schema Validation Testing

### Step 1: Google Rich Results Test
**Purpose**: Verify schema is valid and eligible for rich snippets

**Process**:
1. Go to: https://search.google.com/test/rich-results
2. Enter site URL: `https://codesbyfebin.vercel.app/`
3. Run test
4. Document results:
   - [ ] No errors
   - [ ] All schema types recognized
   - [ ] Rich results eligible
   - [ ] Preview shows correct data

**Pages to Test**:
- [ ] `/` (Landing - Organization, WebSite, BreadcrumbList, ItemList)
- [ ] `/about/` (About - Person, WebPage, BreadcrumbList)
- [ ] `/blog/` (Blog - BlogPosting, CollectionPage, BreadcrumbList)
- [ ] `/projects-enhanced/` (Projects - SoftwareApplication, CollectionPage, BreadcrumbList)
- [ ] `/portfolio/` (Portfolio - WebPage, ItemList, BreadcrumbList)
- [ ] `/docs/` (Documentation - FAQPage, WebPage, BreadcrumbList)
- [ ] `/docs/research/` (Research - ScholarlyArticle, CollectionPage, BreadcrumbList)

### Step 2: Google Schema Testing Tool
**Purpose**: Detailed schema validation

**Process**:
1. Go to: https://schema.org/docs/schema_org_in_5_minutes.html
2. Validate each page's JSON-LD markup
3. Check for:
   - [ ] Valid JSON syntax
   - [ ] Required properties present
   - [ ] Recommended properties included
   - [ ] No deprecated properties
   - [ ] URLs properly formatted

**Sample Validation**:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "CodesbyFebin",
  "url": "https://codesbyfebin.vercel.app/",
  "founder": { "@type": "Person", "name": "Febin Francis" },
  "sameAs": [
    "https://github.com/CodesbyFebin",
    "https://twitter.com/codesbyfebin",
    "https://linkedin.com/in/codesbyfebin"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "General",
    "email": "febin@codesbyfebin.com"
  }
}
```

### Step 3: JSON-LD Syntax Validation
**Purpose**: Ensure valid JSON-LD format

**Process**:
1. Go to: https://jsonlint.com/
2. Copy each `<script type="application/ld+json">` block
3. Validate JSON syntax
4. Document any errors:
   - [ ] Landing page Organization
   - [ ] Landing page WebSite
   - [ ] About page Person
   - [ ] Blog page BlogPosting
   - [ ] Projects page SoftwareApplication
   - [ ] Portfolio page ItemList
   - [ ] Research page ScholarlyArticle

### Step 4: Structured Data Testing Tool
**Purpose**: Preview how schema appears in search results

**Process**:
1. Go to: https://developers.google.com/search/docs/appearance/structured-data
2. Test each page URL
3. Verify preview shows:
   - [ ] Correct page title
   - [ ] Accurate description
   - [ ] Organization information
   - [ ] Author details
   - [ ] Publication dates
   - [ ] Navigation breadcrumbs

### Step 5: SEMrush Schema Audit
**Purpose**: Comprehensive schema coverage analysis

**Process**:
1. Install SEMrush SEO toolbar: https://www.semrush.com/toolbar/
2. Audit site for schema coverage
3. Check for:
   - [ ] All pages have schema
   - [ ] Rich snippet eligibility
   - [ ] Schema coverage gaps
   - [ ] Duplicate schema warnings

### Step 6: Manual Code Review
**Purpose**: Verify implementation details

**Checklist**:
- [ ] All `<script type="application/ld+json">` blocks are properly formatted
- [ ] No syntax errors in JSON
- [ ] All required properties filled
- [ ] URLs use absolute (not relative) paths
- [ ] Dates follow ISO 8601 format (YYYY-MM-DD)
- [ ] No hardcoded test URLs
- [ ] Schema matches page content

**Example - BreadcrumbList Format**:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://codesbyfebin.vercel.app/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "About",
      "item": "https://codesbyfebin.vercel.app/about/"
    }
  ]
}
```

---

## Rich Snippets Eligibility

### Current Implementation

| Schema Type | Page | Rich Snippet Type | Status |
|------------|------|-------------------|--------|
| Organization | Landing | Knowledge Panel (eligible) | ✅ Ready |
| WebSite | Landing | Sitelinks (eligible) | ✅ Ready |
| BreadcrumbList | All | Breadcrumb Navigation | ✅ Ready |
| BlogPosting | Blog | Article Snippet | ✅ Ready |
| CollectionPage | Blog/Projects | Collections | ✅ Ready |
| FAQPage | Docs | FAQ Results | ✅ Ready |
| SoftwareApplication | Projects | Software App Card | ✅ Ready |
| ScholarlyArticle | Research | Article Snippet | ✅ Ready |

---

## Testing Process

### Week 1: Validation
- [ ] Run Google Rich Results Test
- [ ] Validate all JSON-LD syntax
- [ ] Document any errors
- [ ] Fix issues if found

### Week 2: Verification
- [ ] Re-test after fixes
- [ ] Verify all schema recognized
- [ ] Check preview accuracy
- [ ] Confirm rich snippet eligibility

### Week 3: Submission
- [ ] Submit to Google Search Console
- [ ] Monitor indexing status
- [ ] Track rich results appearance

### Week 4: Monitoring
- [ ] Check Search Console for errors
- [ ] Verify rich snippets appearing
- [ ] Monitor click-through rates

---

## Common Issues & Fixes

### Issue: "schema.org URL not in recommended list"
**Fix**: Ensure all schema use `https://schema.org` as @context

### Issue: "Missing required property"
**Fix**: Check schema.org documentation for required fields
- Organization: name, url required
- BlogPosting: headline, author, datePublished required
- Person: name required

### Issue: "Invalid URL format"
**Fix**: Use absolute URLs (https://codesbyfebin.vercel.app/about/) not relative (/about/)

### Issue: "Duplicate schema on page"
**Fix**: Only one schema of each type per page (unless intentional ItemList)

### Issue: "Date format invalid"
**Fix**: Use ISO 8601 format (2026-10-03) not (October 3, 2026)

---

## Schema.org Documentation References

### Primary Resources
- Schema.org Type Documentation: https://schema.org/
- Google Structured Data Docs: https://developers.google.com/search/docs/appearance/structured-data
- JSON-LD Guide: https://json-ld.org/

### Schema Types Used
1. **Organization**: https://schema.org/Organization
2. **WebSite**: https://schema.org/WebSite
3. **Person**: https://schema.org/Person
4. **WebPage**: https://schema.org/WebPage
5. **BreadcrumbList**: https://schema.org/BreadcrumbList
6. **BlogPosting**: https://schema.org/BlogPosting
7. **CollectionPage**: https://schema.org/CollectionPage
8. **FAQPage**: https://schema.org/FAQPage
9. **ScholarlyArticle**: https://schema.org/ScholarlyArticle
10. **SoftwareApplication**: https://schema.org/SoftwareApplication
11. **ItemList**: https://schema.org/ItemList

---

## Validation Checklist

### Pre-Testing
- [x] Schema markup implemented on all pages
- [x] JSON-LD format used
- [x] Schema types relevant to content
- [x] Required properties included
- [ ] Validated with Google tools
- [ ] Verified in Search Console

### Testing
- [ ] Google Rich Results Test: Pass
- [ ] JSON-LD Syntax: Valid
- [ ] Schema Coverage: Complete
- [ ] Rich Snippets: Eligible
- [ ] Preview Accuracy: Correct

### Post-Testing
- [ ] All errors fixed
- [ ] Schema re-validated
- [ ] Submitted to Search Console
- [ ] Monitoring setup

---

## Next Steps

1. **Run Google Rich Results Test**
   - Test: https://search.google.com/test/rich-results
   - Document results

2. **Validate JSON-LD Syntax**
   - Tool: https://jsonlint.com/
   - Copy each script block and validate

3. **Check Schema.org Compliance**
   - Compare against documentation
   - Verify all required properties

4. **Submit to Google Search Console**
   - Add/verify domain
   - Submit sitemap
   - Monitor rich results report

5. **Track Rich Snippet Appearance**
   - Use GSC Rich Results Report
   - Monitor for 4-6 weeks

---

**Generated by**: Claude Haiku 4.5  
**Session**: https://claude.ai/code/session_01KhRwsuFvG5Frw8kheai4tp  
**Branch**: `claude/codesbyfebin-deploy-puq3a5`
