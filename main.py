from job_seeker_engine import JobSeekerEngine

j = JobSeekerEngine()

j.get_user_input()
j.login_linkedin()
j.search_by_job_type(job_type=j.job_type)
j.search_with_experience_level(experience_level=j.experience_level)
j.easy_apply()
j.apply_page_jobs()