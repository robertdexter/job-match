"""
Simple script to run the job match from terminal.
"""
from job_match import JobMatch

match = JobMatch('https://bn-hiring-challenge.fly.dev/members.json',
                 'https://bn-hiring-challenge.fly.dev/jobs.json')

match.match_members_to_jobs()
match.print_matches()
