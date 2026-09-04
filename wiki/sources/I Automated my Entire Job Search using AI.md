---
title: "I Automated my Entire Job Search using AI"
source_file: "Clippings/I Automated my Entire Job Search using AI (Here's How).md"
date_ingested: 2026-09-02
tags:
  - youtube
  - ai-automation
  - job-search
  - n8n
  - workflow
author: "[[Praful Sharma]]"
url: "https://www.youtube.com/watch?v=n7fl1gAQs5s"
---

# I Automated my Entire Job Search using AI

YouTube tutorial by [[Praful Sharma]] on building an AI-powered job search automation system using n8n.

## Summary

A complete 7-step n8n workflow that automates the entire job search and application process. The system fetches your resume, scrapes LinkedIn jobs, filters them with AI, creates custom resumes for each match, logs everything to Google Sheets, and sends you a daily email digest.

## The 7-Step Workflow

### Step 1: Setup n8n and Fetch Resume
- Connect Google Docs to n8n
- Fetch your base resume from Google Drive
- This is the source document for all custom resumes

### Step 2: Fetch Jobs from LinkedIn
- Use Apify actor "LinkedIn Job Scraper" ($5 free credit)
- Filter by: location, job type (full-time), experience (mid/senior), work type (remote)
- Scrapes ~150 jobs per run
- Output: JSON with job details

### Step 3: Filtering Jobs using AI
- Loop over jobs in batches of 5
- GPT-4.1 Nano (cheap model) scores each job vs your resume
- Returns: True/False verdict + reason
- Only jobs with 90%+ match pass through
- Discards old postings (>3 months)

### Step 4: Prepare Custom Resume for Each Job
- Second AI call for jobs that passed filtering
- System prompt: "Expert technical resume writer"
- Takes job description + your base resume
- Outputs: HTML-formatted resume tailored to that specific job
- Optimized for ATS (Applicant Tracking Systems)
- Saves to Google Docs

### Step 5: Creating a Google Sheet for Jobs
- Creates/updates a Google Sheet with all matched jobs
- Columns: Location, Job Link, Title, Level, Posted Date, Company, Salary, Resume URL, Apply URL, Reason
- Your custom resume link for each job

### Step 6: Setup Email System
- SMTP integration for daily email
- Condition: Only send if 150+ jobs found (prevents spam)
- HTML-formatted email with spreadsheet link
- Subject: "Auto Job Finder Found New Jobs"

### Step 7: Final Run
- Full pipeline executes daily via cron job
- Email arrives with matched jobs + custom resumes
- Total time: ~19 minutes per run

## Key Technical Details

- **Platform:** n8n (workflow automation)
- **Job scraping:** Apify (LinkedIn Job Scraper actor)
- **AI model:** GPT-4.1 Nano (cheap, fast)
- **Resume format:** HTML (ATS-friendly)
- **Storage:** Google Docs + Google Sheets
- **Email:** SMTP with HTML template
- **Cost:** ~$0.70 per 1000 jobs scraped

## What Makes This Different

1. **Custom resume per job** — Not just finding jobs, but tailoring applications
2. **ATS optimization** — HTML format passes through applicant tracking systems
3. **90% threshold** — Only high-match jobs pass through
4. **Daily automation** — Cron job runs every day without manual intervention
5. **Full pipeline** — From scraping to email, nothing manual

## Tools Mentioned

- [[n8n]] — workflow automation platform
- Apify — web scraping actors
- OpenAI API — GPT-4.1 Nano for filtering and resume writing
- Google Docs API — resume storage
- Google Sheets API — job logging
- SMTP — email delivery

## Related Concepts

- [[AI Automation]] — this is a practical implementation
- [[Prompt Engineering]] — system prompts for job matching and resume writing
- [[Tokens and Context Window]] — using cheap models (Nano) for cost efficiency
