# Academic Research Collaborator

A multi-agent system for academic research assistance that leverages local LLM models to provide comprehensive research support including literature review, hypothesis validation, and draft polishing.

## Screenshot

![AcademicResearchCollaborator](AcademicResearchCollaborator.png)

## Features

- **Multi-Agent Architecture**: Three specialized agents work together to provide comprehensive research assistance
- **Local LLM Integration**: Uses Ollama with LLaMA 2 and other local models for privacy and cost-effectiveness
- **Persistent Memory Storage**: TinyDB-based memory system for tracking research sessions and agent interactions
- **Interactive Frontend**: Streamlit-based web interface for easy research collaboration
- **Self-Contained**: All code and dependencies included in this project - no external shared folder dependencies

## Agents

### 1. Literature Review Agent
- Conducts comprehensive literature reviews
- Identifies relevant academic sources
- Analyzes research gaps and opportunities
- Provides thematic analysis of existing research

### 2. Hypothesis Validator Agent
- Validates research hypotheses for clarity and testability
- Provides methodological feedback and suggestions
- Assesses statistical requirements for hypothesis testing
- Offers recommendations for research design improvements

### 3. Draft Polisher Agent
- Polishes and refines academic drafts
- Provides writing quality feedback
- Suggests structural improvements
- Generates comprehensive academic documents

## Installation

1. **Navigate to the project directory**:
```bash
cd SchoolOfAI/Official/soai-25-academicresearch
```

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install Ollama** (if not already installed):
```bash
# Visit https://ollama.ai for installation instructions
# Pull the LLaMA 2 model
ollama pull llama2
```

4. **Start Ollama** (if not already running):
```bash
ollama serve
```

## Usage

### Start the Application

Run the Streamlit frontend:

```bash
streamlit run frontend/app.py
```

The application will open in your browser at `http://localhost:8501`

### Using the Application

1. **Enter Research Question**: Type your research question in the sidebar
2. **Add Citations** (Optional): Paste any existing citations or references
3. **Add Notes** (Optional): Include any additional context or requirements
4. **Click "Run Research Team"**: The agents will collaborate to produce results

### Project Structure

```
soai-25-academicresearch/
├── README.md                 # This file
├── requirements.txt           # Python dependencies
├── PROJECT_25_GUIDE.md      # Project guide
├── orchestrator.py           # Agent orchestration
├── agents/                  # Agent implementations
│   ├── base.py            # Runtime bridge and utilities
│   ├── literature_review_agent.py
│   ├── hypothesis_validator_agent.py
│   └── draft_polisher_agent.py
├── frontend/                # Streamlit UI
│   ├── app.py             # Main application
│   └── components.py       # Reusable UI components
├── runtime/                 # Self-contained runtime
│   ├── __init__.py
│   ├── config.py          # Configuration management
│   ├── llm_client.py      # LLM client interface
│   └── project_runtime.py # Core runtime logic
└── memory/                  # Persistent storage
    └── memory_store.json  # Session data (auto-created)
```

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root to customize behavior:

```bash
# LLM Configuration
LLM_PROVIDER=ollama
LLM_MODEL=llama2
LLM_ENDPOINT=http://localhost:11434/api/generate
LLM_REQUEST_TIMEOUT_SECONDS=1800

# AWS Configuration (for Bedrock)
AWS_REGION=us-east-1
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key

# OpenAI Configuration (optional)
OPENAI_API_KEY=your_openai_api_key
```

### Model Selection

The system supports multiple LLM models:
- `llama2` (default) - Good balance of performance and resource usage
- `mistral` - Faster inference, good for quick iterations
- `codellama` - Specialized for code-related research

## Data Storage

### Memory Store
Research sessions and agent interactions are stored in:
- `memory/memory_store.json` - TinyDB database with session history

This file is automatically created when you first run the application.

## Troubleshooting

### Common Issues

1. **Ollama Connection Error**
   - Ensure Ollama is installed and running: `ollama serve`
   - Check if the model is pulled: `ollama pull llama2`
   - Verify Ollama is accessible at `http://localhost:11434`

2. **Import Errors**
   - Ensure you're running from the project directory
   - Install all dependencies: `pip install -r requirements.txt`
   - This project is self-contained - no external shared folder dependencies

3. **Memory Database Issues**
   - Ensure the `memory/` directory exists
   - Check file permissions for `memory/memory_store.json`
   - Delete `memory/memory_store.json` to reset (optional)

### Performance Optimization

- Use appropriate model sizes based on available hardware
- Consider using `mistral` for faster iterations during development
- Monitor memory usage with large research sessions
- Clear old sessions from memory to improve performance

## Development

### Adding New Agents

1. Create a new agent file in the `agents/` directory
2. Import the agent in `orchestrator.py`
3. Add the agent to the workflow in the `run_workflow` method

### Customizing the Frontend

The frontend uses Streamlit components from `frontend/components.py`. You can:
- Modify `frontend/app.py` to change the UI layout
- Add new components in `frontend/components.py`
- Customize styling and user interactions

## License

This project is part of the School of AI curriculum and follows the same licensing terms.

## Support

For issues and questions:
- Check the troubleshooting section
- Review the project structure and code
- Ensure Ollama is properly installed and running
