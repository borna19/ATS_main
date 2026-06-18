import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)


def get_ats_score(resume_text, job_description):
    """
    Returns:
    - ats_score (based on keyword match)
    - matched_keywords
    - missing_keywords
    """

    # Clean texts
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(job_description)

    # Keywords
    jd_keywords = set(jd_clean.split())
    resume_words = set(resume_clean.split())

    matched_keywords = sorted(jd_keywords & resume_words)
    missing_keywords = sorted(jd_keywords - resume_words)

    total_keywords = len(jd_keywords)
    matched_count = len(matched_keywords)

    # ATS score: percentage of keywords matched
    ats_score = 0
    if total_keywords > 0:
        ats_score = round((matched_count / total_keywords) * 100, 2)

    return ats_score, matched_keywords, missing_keywords
