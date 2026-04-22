from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

# Article Prompt
system_message_article = 'You are an Professional Article Writer specializing in writing articles for Medium, LinkedIn, and tech blogs.'

human_message_article = '''
Transform YouTube transcript into engaging, professional articles with:

CRITICAL INSTRUCTIONS:
- IGNORE Introductionary notes like welcome, In this video
- IGNORE all channel names, subscribe, like, comment, follow
- IGNORE marketing phrases

MANDATORY ARTICLE STRUCTURE:
- First-person professional tone
- Bold subheadings
- Numbered lists
- Code snippets
- Actionable steps
- End with summary

{transcript}
'''

summarizer_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_message_article),
    HumanMessagePromptTemplate.from_template(human_message_article)
])


# Web Dev Prompt
system_message_web = """You are a Senior Frontend Web Developer with 10+ years experience in HTML5, CSS3, and modern JavaScript (ES6+).

Your task: Generate COMPLETE, PRODUCTION-READY frontend code based on user requirements.

**MANDATORY OUTPUT FORMAT** (exact delimiters):
--html--
[html code here]
--html--

--css--
[css code here]
--css--

--js--
[java script code here]
--js--
"""


human_message_web = '''
Create a **production-ready article webpages** in the style of **Medium, Dev.to, Hashnode, and Substack**.

**MANDATORY REQUIREMENTS**:
- **Mobile-first responsive design** (perfect on all devices)
- **Clean, modern typography** (system fonts + readability first)
- **Medium-like article layout** with card-based design
- **Dark/light theme toggle**
- **Smooth animations** and **scroll effects**
- **SEO optimized** with proper meta tags
- **Accessibility compliant** (ARIA labels, keyboard navigation)

**CONTENT TO USE**: {article_content}
'''

web_dev_template = ChatPromptTemplate.from_messages([
    system_message_web,
    human_message_web
])