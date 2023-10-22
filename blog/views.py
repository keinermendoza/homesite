from django.shortcuts import render

links = [
    {
        "label": "Home",
        "url": "#home",
    },
    {
        "label": "Projects",
        "url": "#projects",
    },
    {
        "label": "Certificates",
        "url": "#certificates",
    },
    {
        "label": "FAQ",
        "url": "#faq",
    },
    {
        "label": "Blog",
        "url": "#blog",
    },
]

projects = [
    {
        "image": "https://m.media-amazon.com/images/I/71k06Iic2NL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "name": "RedThunder K84 Wireless",
        "description": "High-performance 2.4G Wireless Keyboard and Mouse】Are you looking for a small wireless keyboard and mouse...",
        "tags": [
            "tecnology",
            "keyboard",
            "computers",
        ],
        "code": "urldecode",
        "demo": "urldedemo",
        "online": "urlonline",
        "post": "urlpost",
    },
    {
        "image": "https://m.media-amazon.com/images/I/61PnHlc0HCL.__AC_SY445_SX342_QL70_FMwebp_.jpg",
        "name": "Apple iPad",
        "description": "WHY IPAD — All the essentials in the most affordable iPad, with a beautiful 10.2-inch Retina display, powerful...",
        "tags": [
            "tecnology",
            "pad",
            "tablet",
        ],
        "demo": "urldedemo",
        "certified": "urlcertified",
        "online": "urlonline",
    },
    {
        "image": "https://m.media-amazon.com/images/I/61PnHlc0HCL.__AC_SY445_SX342_QL70_FMwebp_.jpg",
        "name": "Apple iPad",
        "description": "WHY IPAD — All the essentials in the most affordable iPad, with a beautiful 10.2-inch Retina display, powerful...",
        "tags": [
            "tecnology",
            "pad",
            "tablet",
        ],
        "code": "urldecode",
        "demo": "urldedemo",
    },
    {
        "image": "https://m.media-amazon.com/images/I/71k06Iic2NL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "name": "RedThunder K84 Wireless",
        "description": "High-performance 2.4G Wireless Keyboard and Mouse】Are you looking for a small wireless keyboard and mouse...",
        "tags": [
            "tecnology",
            "keyboard",
            "computers",
        ],
        "post": "urlpost",
        "code": "urldecode",
    },
]

certificates = [
    {
        "title": "CS50's Introduction to Programming with Python",
        "image": "blog/images/certificates/CS50P.png",
        "excercises": 41,
        "project": 1,
        "src": "https://certificates.cs50.io/5781eb7c-6c45-4cac-86fc-019b31b6065e.png?size=letter",
        "description": "An introduction to programming using a language called Python. Learn how to read and write code as well as how to test and “debug” it. Designed for students with or without prior programming experience who'd like to learn Python specifically. Learn about functions, arguments, and return values (oh my!); variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems. No software required except for a web browser, or you can write code on your own PC or Mac.",
        "topics": [
            "Functions, Variables",
            "Conditionals",
            "Loops",
            "Exceptions",
            "Libraries",
            "Unit Tests",
            "File I/O",
            "Regular Expressions",
            "Object-Oriented Programming",
        ],
        "url": "https://cs50.harvard.edu/python/2022/weeks/",
    },
    {
        "title": "CS50: Introduction to Computer Science",
        "image": "blog/images/certificates/CS50x.png",
        "src": "https://certificates.cs50.io/5781eb7c-6c45-4cac-86fc-019b31b6065e.png?size=letter",
        "description": "This is CS50x , Harvard University's introduction to the intellectual enterprises of computer science and the art of programming for majors and non-majors alike, with or without prior programming experience. An entry-level course taught by David J. Malan, CS50x teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, Python, SQL, and JavaScript plus CSS and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming.",
        "topics": [
            "Scratch",
            "C",
            "Arrays",
            "Algorithms",
            "Memory",
            "Data Structures",
            "Python",
            "SQL",
            "HTML, CSS, JavaScript",
            "Flask (Python web framework)",
        ],
        "url": "https://cs50.harvard.edu/x/2023/weeks/",
    },
    {
        "title": "CS50's Web Programming with Python and JavaScript",
        "image": "blog/images/certificates/CS50W.png",
        "src": "https://certificates.cs50.io/7aff8b93-7fcd-4a15-87c2-66fc25565a26.png?size=letter",
        "description": "Topics include database design, scalability, security, and user experience. Through hands-on projects, you'll learn to write and use APIs, create interactive UIs, and leverage cloud services like GitHub and Heroku. By course's end, you'll emerge with knowledge and experience in principles, languages, and tools that empower you to design and deploy applications on the Internet.",
        "topics": [
            "HTML, CSS",
            "Git",
            "Python",
            "Django",
            "SQL, Models, and Migrations",
            "JavaScript",
            "User Interfaces",
            "Testing, CI/CD",
            "Scalability and Security",
        ],
        "url": "https://cs50.harvard.edu/web/2020/weeks/",
    },
]


def home(request):
    return render(
        request,
        "blog/homepage.html",
        {
            "links": links,
            "projects": projects,
            "certificates": certificates,
        },
    )
