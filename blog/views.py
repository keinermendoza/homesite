from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
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

posts = [
    {
        'id':1,
        'title': 'saliendo para la casa',
        'body': '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil omnis vitae blanditiis et eius nulla, ut dolorum. Culpa sapiente maxime laudantium sequi, maiores, ut qui molestiae doloribus, ipsa quibusdam aliquid!
        Laudantium eaque voluptatum fugit delectus earum optio? Consectetur aspernatur aliquid eos laborum, illo cumque ea illum assumenda quaerat id! Ab amet, nemo veritatis necessitatibus suscipit rerum optio odit ipsum sequi.
        Ex neque delectus officiis ipsam ab sed sequi quibusdam voluptate, enim accusantium, provident tenetur autem eum dolores excepturi tempora doloremque, illum cumque similique dolorem eligendi. Dolor ullam incidunt dolorum fuga.
        Libero magni consequuntur laboriosam animi inventore nobis culpa, aliquam qui temporibus. Culpa, temporibus quidem officiis quibusdam obcaecati vitae eius repudiandae quo magni expedita neque vel saepe ex accusantium itaque sequi?
        Excepturi fugit vitae sunt exercitationem quisquam, labore dignissimos dolores doloribus omnis odio mollitia itaque cumque ipsam nisi adipisci molestias, assumenda facere aut porro quasi sequi. Optio fuga nisi incidunt possimus!
        Tempora ea sit alias. Odio consectetur blanditiis nobis laudantium rem, totam possimus praesentium maiores dolores quae dolorem corrupti voluptate quia neque debitis enim, nostrum iure architecto fugit officia quod. Beatae
        At, consequatur. Veniam nemo, quis iusto natus facere voluptates officia aut velit qui ullam in rerum. Sit corrupti corporis voluptatem reiciendis ab temporibus, eum quisquam excepturi facere, ut odio aspernatur.
        Recusandae a impedit iure quam facere porro voluptatibus aut placeat laborum consectetur, vel, neque quasi error accusamus sed omnis doloribus vero assumenda natus maxime. Tempora perspiciatis ipsum enim neque aspernatur.
        ia officia maxime aliquam dolores voluptatem eius similique labore eum accusantium iusto quibusdam velit ut ipsam, laboriosam dignissimos exercitationem, molestiae, rem culpa beatae non repudiandae facilis aut cupiditate! Est, odit.
        Suscipit, rerum. Quam labore magnam architecto! Ab odio doloribus labore dolorum. Porro reiciendis atque error repudiandae! Natus eos enim earum nam doloribus praesentium dolore quidem labore dicta maxime, consequuntur rerum
         hic repellendus. Temporibus cumque tempora vero fugiat quasi molestiae veniam nostrum ad, accusamus delectus quia qui beatae sequi non, magni iste eaque! Repellat illum velit distinctio
        Adipisci impedit fugit dignissimos. Veniam repellat nihil dolores maxime natus consectetur assumenda in esse repudiandae architecto corrupti illo quo, animi harum amet, debitis dolorem, blanditiis doloremque eveniet beatae alias voluptatibus.'''
    },
    {
        'id':2,
        'title': 'este es mi segundo post',
        'body': '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil omnis vitae blanditiis et eius nulla, ut dolorum. Culpa sapiente maxime laudantium sequi, maiores, ut qui molestiae doloribus, ipsa quibusdam aliquid!
        Laudantium eaque voluptatum fugit delectus earum optio? Consectetur aspernatur aliquid eos laborum, illo cumque ea illum assumenda quaerat id! Ab amet, nemo veritatis necessitatibus suscipit rerum optio odit ipsum sequi.
        Ex neque delectus officiis ipsam ab sed sequi quibusdam voluptate, enim accusantium, provident tenetur autem eum dolores excepturi tempora doloremque, illum cumque similique dolorem eligendi. Dolor ullam incidunt dolorum fuga.
        Libero magni consequuntur laboriosam animi inventore nobis culpa, aliquam qui temporibus. Culpa, temporibus quidem officiis quibusdam obcaecati vitae eius repudiandae quo magni expedita neque vel saepe ex accusantium itaque sequi?
        Excepturi fugit vitae sunt exercitationem quisquam, labore dignissimos dolores doloribus omnis odio mollitia itaque cumque ipsam nisi adipisci molestias, assumenda facere aut porro quasi sequi. Optio fuga nisi incidunt possimus!
        Tempora ea sit alias. Odio consectetur blanditiis nobis laudantium rem, totam possimus praesentium maiores dolores quae dolorem corrupti voluptate quia neque debitis enim, nostrum iure architecto fugit officia quod. Beatae
        At, consequatur. Veniam nemo, quis iusto natus facere voluptates officia aut velit qui ullam in rerum. Sit corrupti corporis voluptatem reiciendis ab temporibus, eum quisquam excepturi facere, ut odio aspernatur.
        Recusandae a impedit iure quam facere porro voluptatibus aut placeat laborum consectetur, vel, neque quasi error accusamus sed omnis doloribus vero assumenda natus maxime. Tempora perspiciatis ipsum enim neque aspernatur.
        ia officia maxime aliquam dolores voluptatem eius similique labore eum accusantium iusto quibusdam velit ut ipsam, laboriosam dignissimos exercitationem, molestiae, rem culpa beatae non repudiandae facilis aut cupiditate! Est, odit.
        Suscipit, rerum. Quam labore magnam architecto! Ab odio doloribus labore dolorum. Porro reiciendis atque error repudiandae! Natus eos enim earum nam doloribus praesentium dolore quidem labore dicta maxime, consequuntur rerum
         hic repellendus. Temporibus cumque tempora vero fugiat quasi molestiae veniam nostrum ad, accusamus delectus quia qui beatae sequi non, magni iste eaque! Repellat illum velit distinctio
        Adipisci impedit fugit dignissimos. Veniam repellat nihil dolores maxime natus consectetur assumenda in esse repudiandae architecto corrupti illo quo, animi harum amet, debitis dolorem, blanditiis doloremque eveniet beatae alias voluptatibus.'''
    },
    {
        'id':2,
        'title': 'a la tercera va la venciada',
        'body': '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil omnis vitae blanditiis et eius nulla, ut dolorum. Culpa sapiente maxime laudantium sequi, maiores, ut qui molestiae doloribus, ipsa quibusdam aliquid!
        Laudantium eaque voluptatum fugit delectus earum optio? Consectetur aspernatur aliquid eos laborum, illo cumque ea illum assumenda quaerat id! Ab amet, nemo veritatis necessitatibus suscipit rerum optio odit ipsum sequi.
        Ex neque delectus officiis ipsam ab sed sequi quibusdam voluptate, enim accusantium, provident tenetur autem eum dolores excepturi tempora doloremque, illum cumque similique dolorem eligendi. Dolor ullam incidunt dolorum fuga.
        Libero magni consequuntur laboriosam animi inventore nobis culpa, aliquam qui temporibus. Culpa, temporibus quidem officiis quibusdam obcaecati vitae eius repudiandae quo magni expedita neque vel saepe ex accusantium itaque sequi?
        Excepturi fugit vitae sunt exercitationem quisquam, labore dignissimos dolores doloribus omnis odio mollitia itaque cumque ipsam nisi adipisci molestias, assumenda facere aut porro quasi sequi. Optio fuga nisi incidunt possimus!
        Tempora ea sit alias. Odio consectetur blanditiis nobis laudantium rem, totam possimus praesentium maiores dolores quae dolorem corrupti voluptate quia neque debitis enim, nostrum iure architecto fugit officia quod. Beatae
        At, consequatur. Veniam nemo, quis iusto natus facere voluptates officia aut velit qui ullam in rerum. Sit corrupti corporis voluptatem reiciendis ab temporibus, eum quisquam excepturi facere, ut odio aspernatur.
        Recusandae a impedit iure quam facere porro voluptatibus aut placeat laborum consectetur, vel, neque quasi error accusamus sed omnis doloribus vero assumenda natus maxime. Tempora perspiciatis ipsum enim neque aspernatur.
        ia officia maxime aliquam dolores voluptatem eius similique labore eum accusantium iusto quibusdam velit ut ipsam, laboriosam dignissimos exercitationem, molestiae, rem culpa beatae non repudiandae facilis aut cupiditate! Est, odit.
        Suscipit, rerum. Quam labore magnam architecto! Ab odio doloribus labore dolorum. Porro reiciendis atque error repudiandae! Natus eos enim earum nam doloribus praesentium dolore quidem labore dicta maxime, consequuntur rerum
         hic repellendus. Temporibus cumque tempora vero fugiat quasi molestiae veniam nostrum ad, accusamus delectus quia qui beatae sequi non, magni iste eaque! Repellat illum velit distinctio
        Adipisci impedit fugit dignissimos. Veniam repellat nihil dolores maxime natus consectetur assumenda in esse repudiandae architecto corrupti illo quo, animi harum amet, debitis dolorem, blanditiis doloremque eveniet beatae alias voluptatibus.'''
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
        "slug": "cs50s-introduction-to-programming-with-python",
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
        "slug": "cs50-introduction-to-computer-science",
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
        "slug": "cs50s-web-programming-with-python-and-javascript",
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
            "projects": projects[:4],
            "certificates": certificates[:2],
            'current':'homepage'
        },
    )

def project_list(request):
    return render(
        request,
        'blog/projects/project_list.html',
        {
            "projects": projects,
            'current':'projects'
        }
    )

def certificate_list(request):
    return render(
        request,
        'blog/certificates/certificate_list.html',
        {
            "certificates": certificates,
            'current':'certificates'
        }
    )

def certificate_detail(request, slug):
    # certificate = get_object_or_404(Certificate, slug=slug)
    certificate = None
    for cert in certificates:
        if cert["slug"] == slug:
            return render(
                request,
                'blog/certificates/certificate_detail.html',
                {
                    "certificate": cert,
                    'current':'certificates',
                    'detail':cert['title'],
                }
            )
    return HttpResponseNotFound("SORRY, THIS PAGE DOSENT EXIST") 

def post_list(request):
    return render(
        request,
        'blog/blog/post_list.html',
        {
            "posts": posts,
            'current':'blog'
        }
    )