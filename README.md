# BranchMaster

Automatically analyze GitHub repositories, identify potential improvements, and create pull requests for necessary changes.

## Features

- 🔍 Analyzes all branches in a repository
- 📊 Calculates impact scores for changes
- 🤖 Automatically creates pull requests for significant improvements
- ⚡ Parallel processing of branches
- 📈 Progress tracking for long operations

## Installation

```bash
# Clone the repository
git clone https://github.com/avidzcheetah/BranchMaster
cd BranchMaster

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Set your GitHub token as an environment variable:
```bash
export GITHUB_TOKEN=your_token_here
```

2. Run the analyzer:
```bash
python main.py
```

3. Enter the repository name when prompted:
```
Enter repository name (owner/repo): owner/repository
```

## How It Works

1. **Branch Analysis**: The tool scans all branches in the repository and compares them with the default branch.

2. **Code Analysis**: For each branch, it:
   - Analyzes code changes
   - Calculates impact scores
   - Identifies potential improvements

3. **Pull Request Creation**: For significant changes, it automatically creates pull requests with:
   - Detailed descriptions of improvements
   - Impact scores
   - Changed files list

## Configuration

Customize the analyzer behavior by modifying these parameters:

- `min_impact_score`: Minimum score required to create a PR (default: 0.5)
- `max_workers`: Number of parallel analysis threads (default: 5)

## Project Structure

```
src/
├── analyzer.py        # Main analysis logic
├── github_client.py   # GitHub API client
├── github_utils.py    # GitHub-related utilities
├── models.py         # Data models
├── pr_creator.py     # Pull request creation
└── progress_tracker.py # Progress tracking
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Open for anyone to develop and modify.

## Acknowledgments

- Built with Python and GitHub API
- Uses ThreadPoolExecutor for parallel processing
- Progress tracking with tqdm
