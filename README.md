# 🚀 LLM Classification with Groq API

A robust toolkit for structured text classification using Groq's ultra-fast LLMs. Implements confidence scoring, prompt engineering strategies, and analysis workflows.

**By Habiba Khalil - 202200720**

## ✨ Key Features

- **Structured Classification**  
  Categorize text with confidence scores (High/Medium/Low)
- **Prompt Engineering**  
  Pre-built templates for reliable completions
- **Confidence Thresholding**  
  Automatically flag uncertain predictions
- **Model Analysis**  
  Compare prompt strategies and outputs

## ⚡ Quick Start

### Prerequisites

- Python 3.8+
- Groq API key ([Get yours](https://console.groq.com/))

### Installation

```bash
git clone https://github.com/Habiba95943/Habiba-Lab-3
cd llm-classification-groq
pip install -r requirements.txt
```

### Configuration

Create .env file:
```bash
echo "GROQ_API_KEY=your_key_here" > .env
```

## 🧠 Usage Examples

### Basic Classification                                
from taming_llm import LLMClient                                         

client = LLMClient()                                  
result = client.classify_with_confidence(                                             
    "The battery life exceeded expectations",                                                           
    categories=["Positive", "Neutral", "Negative"]                                    
) 

### Custom Prompts                                
analysis = client.complete(                               
    client.create_structured_prompt(                       
        text="Delivery took 3 weeks",                           
        question="Extract shipping duration in days"                                                                                    
    )                                                                        
)                             


## 📊 Expected Output

{                                 
  "category": "Positive",                                       
  "confidence": 0.9,                                
  "reasoning": "Text contains strong positive sentiment"                                  
}                             


## 🛠️ Advanced Features

### Method	Description	Parameters
classify_with_confidence()	Categorized text with confidence scoring	confidence_threshold=0.8                          
create_structured_prompt()	Generates analysis-ready prompts	text, question                        
analyze_confidence()	Interprets confidence levels	Raw API response                          

## 🌐 Project Structure

├── taming_llm.py        # Core classification logic                          
├── requirements.txt     # Dependencies                
├── .env.example         # API key template                       
└── examples/            # Usage notebooks                
├── basic_usage.ipynb                         
└── advanced_analysis.ipynb                            

## 🚨 Troubleshooting
Common Issues:
   - APIError: Invalid key → Verify .env file location
   - Low confidence scores → Adjust temperature (0.3-0.7 recommended)
   - Timeout errors → Check Groq service status

## 🤝 Contributing
- Fork the repository
- Create your feature branch (git checkout -b feature/AmazingFeature)
- Submit a pull request


