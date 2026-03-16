import json

class ResumeBuilder:
    """Helper to structure and format tailored resumes."""
    def __init__(self):
        self.personal_info = {}
        self.summary = ""
        self.skills = {}
        self.experience = []
        self.education = []
        self.achievements = []

    def set_personal_info(self, name, email, phone, linkedin=None, website=None):
        self.personal_info = {
            'name': name,
            'email': email,
            'phone': phone,
            'linkedin': linkedin,
            'website': website
        }

    def set_summary(self, summary_text):
        self.summary = summary_text

    def add_skill_group(self, category, skills_list):
        self.skills[category] = skills_list

    def add_experience(self, job_title, company, dates, responsibilities):
        self.experience.append({
            'title': job_title,
            'company': company,
            'dates': dates,
            'responsibilities': responsibilities
        })

    def add_education(self, degree, institution, date):
        self.education.append({
            'degree': degree,
            'institution': institution,
            'date': date
        })

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def to_markdown(self):
        lines = [f"# {self.personal_info.get('name', 'NAME').upper()}"]
        contact = f"Email: {self.personal_info.get('email')} | Phone: {self.personal_info.get('phone')}"
        if self.personal_info.get('linkedin'):
            contact += f" | LinkedIn: {self.personal_info.get('linkedin')}"
        lines.append(contact)
        lines.append("")

        if self.summary:
            lines.append("## PROFESSIONAL SUMMARY")
            lines.append(self.summary)
            lines.append("")

        if self.skills:
            lines.append("## TECHNICAL SKILLS")
            for cat, items in self.skills.items():
                lines.append(f"- **{cat}**: {', '.join(items)}")
            lines.append("")

        if self.experience:
            lines.append("## PROFESSIONAL EXPERIENCE")
            for exp in self.experience:
                lines.append(f"**{exp['title']}** | {exp['company']} | {exp['dates']}")
                for resp in exp['responsibilities']:
                    lines.append(f"- {resp}")
                lines.append("")

        if self.education:
            lines.append("## EDUCATION")
            for edu in self.education:
                lines.append(f"**{edu['degree']}**")
                lines.append(f"{edu['institution']} | {edu['date']}")
                lines.append("")

        if self.achievements:
            lines.append("## KEY ACHIEVEMENTS")
            for ach in self.achievements:
                lines.append(f"- {ach}")
            lines.append("")

        return "\n".join(lines)

    def save_json(self, filename):
        data = {
            'personal_info': self.personal_info,
            'summary': self.summary,
            'skills': self.skills,
            'experience': self.experience,
            'education': self.education,
            'achievements': self.achievements
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    builder = ResumeBuilder()
    builder.set_personal_info("John Doe", "john@example.com", "555-0199")
    builder.set_summary("Experienced software engineer...")
    builder.add_skill_group("Languages", ["Python", "JavaScript"])
    builder.add_experience("Senior Developer", "Tech Co", "2020 - Present", ["Led team of 5", "Implemented CI/CD"])
    print(builder.to_markdown())
