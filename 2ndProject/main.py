import streamlit as st
import PyPDF2
import io
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

# 🌍 Load environment variables from .env file
load_dotenv()

# 🛠️ Streamlit app configuration
st.set_page_config(
    page_title="AI Resume Evaluator مُقيِّم السيرة الذاتية بالذكاء الاصطناعي",
    page_icon="📄",
    layout="centered"
)

# 📄 App title and description
st.title("AI Resume Evaluator مُقيِّم السيرة الذاتية بالذكاء الاصطناعي")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!\n\n"
            "قم بتحميل سيرتك الذاتية واحصل على تعليقات مدعومة بالذكاء الاصطناعي مصممة خصيصًا لتلبية احتياجاتك!")

# 🔐 Load OpenAI API key
OPENAI_API_KEY="here"

# 📤 File upload
uploaded_file = st.file_uploader("Upload Your Resume (PDF or TXT)\n\nقم بتحميل سيرتك الذاتية (PDF أو TXT)",
                                 type=["pdf", "txt"])

# 🎯 Job role input
job_role = st.text_input("Enter the job role you're targeting (optional)"
                         "\n\nأدخل مجال الوظيفة التي تستهدفها (أختياري)")

# 🧠 Analyze button
analyze_button = st.button("Analyze Resume\n\nتحليل السيرة الذاتية")

# 📄 Extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# 🧼 Clean text to remove problematic characters
def clean_text(text):
    cleaned = re.sub(r'[\ud800-\udfff]', '', text)  # Remove surrogate characters
    return ''.join(c for c in cleaned if c.isprintable())  # Remove non-printable chars

# 📂 Extract text from uploaded file
def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.type.lower()

    if "pdf" in file_type:
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))

    try:
        return uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        try:
            return uploaded_file.read().decode("latin-1")
        except Exception as e:
            st.error(f"Unable to decode file content: {str(e)}")
            st.stop()

# 🚀 Resume analysis logic
if analyze_button and uploaded_file:
    try:
        # 📄 Extract and clean resume content
        raw_content = extract_text_from_file(uploaded_file)
        file_content = clean_text(raw_content)

        # ⚠️ Check for empty content
        if not file_content.strip():
            st.error("File doesn't have any content for evaluation\n\nالملف ليس فيه أي محتوى لتقيم")
            st.stop()

        # 👀 Preview cleaned content
        # st.markdown("#### ✅ Cleaned Resume Preview (أول 300 حرف من السيرة الذاتية)")
        # st.text(file_content[:])

        # 🧾 Build prompt
        prompt = f"""Please analyze this resume and provide constructive feedback.
يرجى تحليل هذه السيرة الذاتية وتقديم تعليقات بناءة.
Focus on the following aspects:
ركز على الجوانب التالية:
1- Content clarity and impact.
1- وضوح المحتوى والتأثير.
2- Skills presentation.
2- عرض المهارات.
3- Experience description.
3- وصف الخبرة.
4- Specific improvements for {job_role if job_role else 'general job applications.'}

Resume Content:
محتوى السيرة الذاتية:
{file_content}

Please provide your analysis in a clear, structured, understandable format with specific recommendations.
يرجى تقديم تحليلك بصيغة واضحة ومهيكلة ومفهومة مع توصيات محددة.
"""

        # 🤖 Send to OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert resume evaluator with years of experience in HR and recruitment."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        # 📊 Display results
        st.markdown("### 📝 Analysis Results - نتائج تقييم السيرة الذاتية")
        st.markdown(response.choices[0].message.content)

    except Exception as e:
        st.error(f"an error occurs: {str(e)}")
        st.error(f"حدوث خطأ: {str(e)}")
