import os
from dotenv import load_dotenv
import groq

class LLMClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEYW")
        self.client = groq.Client(api_key=self.api_key)
        self.model = "llama3-70b-8192" 

    def complete(self, prompt, max_tokens=1000, temperature=0.7):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None

    def create_structured_prompt(self, text, question):
        return f"""
        # Analysis Report

        ## Input Text
        {text}

        ## Question
        {question}

        ## Analysis
        """

    def extract_section(self, completion, section_start, section_end=None):
        start_idx = completion.find(section_start)
        if start_idx == -1:
            return None
        start_idx += len(section_start)
        if section_end is None:
            return completion[start_idx:].strip()
        end_idx = completion.find(section_end, start_idx)
        if end_idx == -1:
            return completion[start_idx:].strip()
        return completion[start_idx:end_idx].strip()

    def classify_with_confidence(self, text, categories, confidence_threshold=0.8):
        prompt = f"""
        Classify the following text into exactly one of these categories: {', '.join(categories)}.

        Response format:
        1. CATEGORY: [one of: {', '.join(categories)}]
        2. CONFIDENCE: [high|medium|low]
        3. REASONING: [explanation]

        Text to classify:
        {text}
        """
        response = self.complete(prompt, max_tokens=500, temperature=0)
        category = self.extract_section(response, "1. CATEGORY: ", "\n")
        confidence_score = self.analyze_confidence(response)
        if confidence_score > confidence_threshold:
            return {
                "category": category,
                "confidence": confidence_score,
                "reasoning": self.extract_section(response, "3. REASONING: ")
            }
        else:
            return {
                "category": "uncertain",
                "confidence": confidence_score,
                "reasoning": "Confidence below threshold"
            }

    def analyze_confidence(self, response):
        
        if "high" in response:
            return 0.9
        elif "medium" in response:
            return 0.6
        else:
            return 0.3

if __name__ == "__main__":
    client = LLMClient()
    text = "The product arrived late and damaged."
    categories = ["Positive", "Mixed", "Negative"]
    result = client.classify_with_confidence(text, categories)
    print(result)
