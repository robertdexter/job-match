# Job Match
A simple python class to match members to jobs.

## Setup

Python 3.12.1

```python
$ pip install -r requirements.txt
```

## Usage
### Option 1 - In a codebase
```python
$ from job_match import JobMatch

$ match = JobMatch('https://bn-hiring-challenge.fly.dev/members.json',
                   'https://bn-hiring-challenge.fly.dev/jobs.json')

$ match.match_members_to_jobs()
$ matches = match.matches
```

### Option 2 - Run as python script outputting to terminal
```shell
$ cd path/to/job-match
$ python run_job_match.py
```

## Discussion
Based off of the brief and the sample datasets provided the intended goal of the algorithm is to find the matches for the job title and job location within the members bio.

Due to the time constraint my objective was to match all cases presented in the data and nothing more i.e. I did not add any functionality to handle potential cases, these will be discussed at the end, that would arise with a larger and more varied dataset, for example similar jobs with different names.

I structured the code in a Python class rather than a function really for code clarity as it allowed me to separate the different components of the functionality - initialization of the datasets, the algorithm itself and the output functionality.

My approach to the algorithm itself was simply to loop through each member and then for each job try to match it. After some very simple data cleaning, setting the data to lowercase, I decided for simplicity to try to match the location first and if a location was matched to only then try to match the job.

There are 2 potential pitfalls in the code currently. One is that if the member does not provide a location no jobs will be matched as the assumption is that a location must be matched before a job can be. Secondly in the final section of the code if no exact job match is found it splits the job title and try's to match on each word, this works for the dataset provided however there could be cases where it would mismatch.

The main challenge in this domain where we are trying to find matching information in a text string written by a human is to do with synonyms ie. we write differently but mean the same thing. For example 'looking to relocate to London' is the same as 'wanting to move to London' or 'Software Developer' is the same as 'Software Engineer'. And 'UX Designer' could be considered the same or similar to 'UI Designer' or 'Front-End Engineer'. Therefore the datasets of search phases and their synonyms becomes very important for accurate data matching, so does good confidence scoring when comparing phases e.g. out of 100 how similar are 2 phrases. 