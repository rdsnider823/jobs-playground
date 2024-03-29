# jobs-playground

The following is a test app used for interviews at EarnBetter.

# Tools

## Application

* Django
* Django Rest Framework

## Infrastructure

* PostgreSQL (Database)
* Redis (Cache Layer)

# Getting Started

The project is designed to run as a vscode dev container on a local machine or using github codespaces. Once the dev container is started run

```bash
# run migrations and start the django server
/start
```

# Features to implement

## Add source to all jobs

Behind the scenes jobs are imported via feeds from various providers. We want to start tracking which feed each source belongs to.

### Requirements

* Current sources are linkedin, monster, indeed
* All jobs have a source feed they come from

## Recent Searches

We have the ability to search for jobs based on a set of criteria. We would like to give our users the ability to recall searches they've perfomed in the past.

### Requirements

* The search endpoint `/api/jobs` is used in various places and should not always be saved, it is up to the UI to determine when a search is saved
* The UI only needs to show the last 5 saved searches
* For each search term we only want one entry, this is regardless of any other filters such as job_type changing

## Job of the Day

Users are shown recommendations based on their profile. We would like to highlight the top recommendation as a Job of the Day in the UI. The goal is
generate interest in clicking on a job.

### Requirements

* The job comes from the first recommendation
* The job should remain the same for an entire day
* The recommendations page should show both in the same page
* The dashboard should remove job of the day from the list so it is not a duplicate.
