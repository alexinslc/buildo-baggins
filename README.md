# buildo-baggins
🌋Forged in the fires of Mt. Python — fast, easy static sites for Hobbits who prefer second breakfast over setup wizards. 🧙‍♂️


## Buildo Baggins Project Structure
```
.
├── static/                # Static assets (images, CSS)
├── content/               # Your markdown or text content
├── template.html          # HTML template used for all pages
├── src/                   # Python code for the generator
│   └── main.py            # Main script that builds the site
├── public/                # Output: final HTML/CSS lives here
│
├── [ Run This to Build ]
|   ├── $ ./main.sh
│   └── $ python3 src/main.py
|
├── [ Run This to Test ]
│   ├── $ ./test.sh
│   └── $ python3 -m unittest discover -s src
│
└── [ Preview Locally ]
    └── $ python3 -m http.server 8888
         → View in your browser at http://localhost:8888
```

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
