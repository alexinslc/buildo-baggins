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
