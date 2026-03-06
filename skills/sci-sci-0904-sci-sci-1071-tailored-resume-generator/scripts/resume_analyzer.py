#!/usr/bin/env python3
import json
import re
from typing import Dict, List, Any

def extract_keywords(text: str) -> List[str]:
    """Extract potential keywords from text."""
    # Simple extraction: words with 4+ characters, ignoring common stop words
    stop_words = {'with', 'this', 'that', 'from', 'have', 'will', 'your', 'what', 'when', 'where', 'their', 'there'}
    words = re.findall(r'\b[A-Za-z]{4,}\b', text.lower())
    return list(set([w for w in words if w not in stop_words]))

def analyze_job_description(job_text: str) -> Dict[str, Any]:
    """Analyze a job description for requirements and keywords."""
    analysis = {
        "keywords": extract_keywords(job_text),
        "years_experience_mentioned": [],
        "degree_mentions": []
    }

    # Look for years of experience
    exp_matches = re.finditer(r'(\d+)(?:\+|-|\s+to\s+)(\d+)?\s*(?:years|yrs)', job_text.lower())
    for match in exp_matches:
        analysis["years_experience_mentioned"].append(match.group(0))

    # Look for education requirements
    degrees = ['bachelor', 'master', 'phd', 'b.s.', 'b.a.', 'm.s.', 'm.a.']
    for degree in degrees:
        if degree in job_text.lower():
            analysis["degree_mentions"].append(degree)

    return analysis

def compare_resume_to_job(resume_text: str, job_text: str) -> Dict[str, Any]:
    """Compare a resume against a job description."""
    job_analysis = analyze_job_description(job_text)
    resume_keywords = set(extract_keywords(resume_text))
    job_keywords = set(job_analysis["keywords"])

    # Calculate match percentage based on simple keyword overlap
    if not job_keywords:
        match_score = 0
    else:
        matched = job_keywords.intersection(resume_keywords)
        match_score = (len(matched) / len(job_keywords)) * 100

    missing_keywords = list(job_keywords - resume_keywords)

    return {
        "match_percentage": round(match_score, 2),
        "matched_keywords_count": len(matched) if job_keywords else 0,
        "missing_keywords_sample": missing_keywords[:10], # Just show top 10
        "job_analysis": job_analysis
    }

if __name__ == '__main__':
    # Simple test
    sample_job = "We are looking for a Software Engineer with 5+ years of Python experience. Bachelor's degree required. Must know SQL and AWS."
    sample_resume = "Software Developer with 3 years experience. I know Python, Java, and SQL. I have a Bachelor's degree in Computer Science."

    result = compare_resume_to_job(sample_resume, sample_job)
    print(json.dumps(result, indent=2))
