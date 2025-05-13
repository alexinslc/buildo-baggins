# Buildo Baggins

🌋 Forged in the fires of Mt. Python — fast, easy static sites for Hobbits who prefer second breakfast over setup wizards. 🧙‍♂️

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/alexinslc/buildo-baggins.git
cd buildo-baggins
```

2. Run the site locally:
```bash
./main.sh
python3 -m http.server 8888
```
Then open http://localhost:8888 in your browser.

## Project Structure

```
.
├── static/                # Static assets (images, CSS)
├── content/               # Your markdown or text content
├── template.html          # HTML template used for all pages
├── src/                   # Python code for the generator
│   └── main.py           # Main script that builds the site
├── docs/                  # Output: final HTML/CSS lives here (for GitHub Pages)
│
├── [ Run Locally ]
│   ├── $ ./main.sh
│   └── $ python3 -m http.server 8888
│
├── [ Run Tests ]
│   ├── $ ./test.sh
│   └── $ python3 -m unittest discover -s src
│
└── [ Deploy to GitHub Pages ]
    └── $ ./build.sh
```

## Features

* **Fast**: Built with Python, optimized for speed
* **Easy**: Simple setup, no complex configurations
* **Flexible**: Customize templates and styles to fit your needs
* **Markdown Support**: Write content in Markdown for easy formatting
* **Static Assets**: Manage images, CSS, and other static files effortlessly
* **Local Preview**: Test your site locally before deploying
* **GitHub Pages**: Easy deployment to GitHub Pages
* **Unit Testing**: Ensure your code is robust with built-in tests

## Deployment to GitHub Pages

1. Make sure your repository is public and you have push access

2. Build the site for GitHub Pages:
```bash
./build.sh
```

3. Commit and push your changes:
```bash
git add .
git commit -m "Update site"
git push origin main
```

4. Configure GitHub Pages:
   - Go to your repository's Settings
   - Navigate to Pages in the sidebar
   - Under "Source", select "Deploy from a branch"
   - Select "main" branch and "/docs" folder
   - Click Save

5. Your site will be available at:
   https://alexinslc.github.io/buildo-baggins/

## Development

### Local Development

For local development, use:
```bash
./main.sh
```

This will:
- Copy static files to the docs directory
- Generate HTML pages from markdown content
- Use "/" as the base path for local testing

### Running Tests

Run the test suite with:
```bash
./test.sh
```

Or manually:
```bash
python3 -m unittest discover -s src
```

## License

MIT License - See [LICENSE](LICENSE) for details.

## Buildo Baggins Features
- **Fast**: Built with Python, optimized for speed.
- **Easy**: Simple setup, no complex configurations.
- **Flexible**: Customize templates and styles to fit your needs.
- **Markdown Support**: Write content in Markdown for easy formatting.
- **Static Assets**: Manage images, CSS, and other static files effortlessly.
- **Local Preview**: Test your site locally before deploying.
- **Unit Testing**: Ensure your code is robust with built-in tests

## TODO
- Continue development to get to mvp.
- Add more features like:
  - Support for custom themes
  - Integration with third-party services (e.g., analytics, SEO)
  - Deployment scripts for popular hosting platforms
