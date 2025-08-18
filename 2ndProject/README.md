<h1>📄 AI Resume Evaluator – مُقيِّم السيرة الذاتية بالذكاء الاصطناعي</h1>
<p>This is my second AI project, built with <b>Streamlit</b> and <b>OpenAI API</b>, designed to help users evaluate their resumes using intelligent feedback. 
It supports both English and Arabic, making it accessible to a wider audience.</p>

<h2>🚀 What It Does</h2>
<ul>
  <li>📤 Upload a resume in .pdf or .txt format</li>
  <li>🎯 Optionally enter a target job role</li>
  <li>🤖 Get AI-powered feedback on:
    <ol>
      <li>Content clarity and impact</li>
      <li>Skills presentation</li>
      <li>Experience description</li>
      <li>Suggestions for improvement</li>
    </ol>
  </li>
  <li>🌐 Bilingual interface (English + Arabic)</li>
  <li>✅ Handles encoding issues and corrupted files gracefully</li>
</ul>

<h2>🧪 Technologies Used</h2>
<table>
  <thead>
    <tr>
      <th>Tool</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Streamlit</code></td>
      <td>Interactive web app</td>
    </tr>
    <tr>
      <td><code>OpenAI API</code></td>
      <td>Resume analysis and feedback generation</td>
    </tr>
    <tr>
      <td><code>PyPDF2</code></td>
      <td>PDF text extraction</td>
    </tr>
    <tr>
      <td><code>python-dotenv</code></td>
      <td>Secure API key management</td>
    </tr>
    <tr>
      <td><code>uv</code></td>
      <td>Modern Python package and environment manager</td>
    </tr>
  </tbody>
</table>

<h2>📁 Project Structure</h2>
<ul>
  <li><code>main.py</code> – Main Streamlit app logic</li>
  <li><code>.env</code> – Stores your OpenAI API key (not committed)</li>
  <li><code>README.md</code> – Project overview and instructions</li>
  <li><code>pyproject.toml</code> – Dependency and project metadata</li>
  <li><code>Saleh Mohammed CV.pdf</code> – Sample resume for testing <b>(❌ This file may trigger encoding errors)</b></li>
  <li><code>Saleh Mohammed CV updated.pdf</code> – Updated version for testing improvements <b>(✅ Works smoothly)</b></li>
  <li><code>Saleh Mohammed CV empty.pdf</code> – Edge case for empty resume testing</li>
</ul>

<h2>🛠️ Setup Instructions</h2>
<ol>
  <li>Install <code>uv</code> (if not already installed):<br>
    <code>pip install uv</code>
  </li>
  <li>Initialize and install dependencies:<br>
    <code>uv venv</code><br>
    <code>uv add streamlit openai PyPDF2 python-dotenv</code>
  </li>
  <li>Add your OpenAI API key to <code>.env</code>:<br>
    <code>OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</code>
  </li>
  <li>Run the app:<br>
    <code>uv run streamlit run main.py</code>
  </li>
</ol>

<h2>🧾 Sample CVs Included</h2>
<ul>
  <li>✅ A complete resume (<code>Saleh Mohammed CV.pdf</code>)</li>
  <li>🛠️ An updated version with improvements</li>
  <li>⚠️ An empty resume to test error handling</li>
</ul>

<h2>📌 Notes</h2>
<ul>
  <li>This project was built for learning and experimentation.</li>
  <li>Inspired by real-world resume challenges and designed to be beginner-friendly.</li>
  <li>Future improvements may include:
    <ul>
      <li>Exporting feedback to PDF</li>
      <li>Arabic-only mode</li>
      <li>Support for .docx files</li>
    </ul>
  </li>
</ul>

<h2>📺 Based On This Tutorial</h2>
<p>This project was inspired by the YouTube tutorial: <b><a href="https://youtu.be/XZdY15sHUa8?si=QCV9nG_J9S1_n6jG">3 Python AI Projects for Beginners – Full Tutorial</a></b><br>
I followed the core steps and added my own improvements 🫡, including:</p>
<ul>
  <li>Support for Arabic responses 🇸🇦</li>
  <li>Encoding error handling for corrupted or empty files</li>
  <li>Bilingual interface for broader accessibility</li>
</ul>
