import requests


class JobMatch():
    """
    Class to match members to jobs based on job title and job location.

    Attributes:
        members (list): List of members data fetched from the provided URL.
        jobs (list): List of jobs data fetched from the provided URL.
        matches (dict): Dictionary storing matched jobs for each member.
    """

    def __init__(self, members_url, jobs_url):
        """
        Initialize the class with members and jobs data fetched from the provided URLs.

        Args:
            members_url (str): URL to fetch the members data.
            jobs_url (str): URL to fetch the jobs data.
        """
        self.members = requests.get(members_url).json()
        self.jobs = requests.get(jobs_url).json()

        self.matches = {}

    def match_members_to_jobs(self):
        """
        Matches members to jobs based on location and job title.
        The final results are stored in self.matches.
        """
        for member in self.members:

            member_name = member['name']
            member_bio = member['bio'].lower()
            self.matches[member_name] = []

            for job in self.jobs:

                job_title = job["title"].lower()
                job_location = job["location"].lower()

                location_match = False

                if 'relocate to ' in member_bio:
                    if f'relocate to {job_location}' in member_bio:
                        location_match = True
                elif 'outside of ' in member_bio:
                    if f'outside of {job_location}' not in member_bio:
                        location_match = True
                    else:
                        location_match = False
                elif job_location in member_bio:
                    location_match = True

                if location_match:
                    if job_title in member_bio:
                        self.matches[member_name].append(job)
                    else:
                        split_job_title = job_title.split(' ')

                        for job_fragment in split_job_title:
                            if job_fragment in member_bio:
                                self.matches[member_name].append(job)
                                break

    def print_matches(self):
        """
        Prints the matched jobs for each member.
        """
        for name, job_matches in self.matches.items():
            print(f'{name}:')
            if job_matches:
                for match in job_matches:
                    print(match)
            else:
                print('No job matches found.')
