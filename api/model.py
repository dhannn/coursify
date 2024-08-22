import google.generativeai as genai
import os

class AIGenModel:
    def __init__(self, model_name='gemini-1.5-flash') -> None:
        self.api_key = os.getenv('GENAI_API_KEY')
        if not self.api_key:
            raise ValueError("API key is not set in the environment variables.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def create_course(self, course_title: str, objectives: str, target_audience: str, 
                      weekly_commitment: str, duration: str, other_comments: str) -> str:
        prompt = (
            f'I am an individual who thrives in the structure of formal education. '
            f'Deadlines keep me accountable to get things done. Having a structured course outline gives me '
            f'direction and prevents me from being aimless. So if I want to hone a skill, I want it to be '
            f'structured as a self-directed learning plan. '
            f'Specifically, I want to be able to {objectives}. With this goal, create a learning plan '
            f'for a course titled {course_title}. Assume it is for {target_audience}. However, this is only '
            f'a means for me to have structure in my learning.'
            f'Assume {weekly_commitment} of commitment per week for {duration}. The learning plan should also {other_comments}.'
        )
        
        response = self.model.generate_content(prompt)
        return response.text
