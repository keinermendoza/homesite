from django.shortcuts import render

def home(request):
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
        'image' :'https://m.media-amazon.com/images/I/71k06Iic2NL.__AC_SX300_SY300_QL70_FMwebp_.jpg',
        'name' : 'RedThunder K84 Wireless',
        'description' : 'High-performance 2.4G Wireless Keyboard and Mouse】Are you looking for a small wireless keyboard and mouse...',
        'tags' : [
            'tecnology', 'keyboard', 'computers',
        ],

        'code':'urldecode',
        'demo':'urldedemo',
        'online':'urlonline',
        'post':'urlpost',
    },
    {
        'image' :'https://m.media-amazon.com/images/I/61PnHlc0HCL.__AC_SY445_SX342_QL70_FMwebp_.jpg',
        'name' : 'Apple iPad',
        'description' : 'WHY IPAD — All the essentials in the most affordable iPad, with a beautiful 10.2-inch Retina display, powerful...',
        'tags' : [
            'tecnology', 'pad', 'tablet',
        ],
        'demo':'urldedemo',
        'certified':'urlcertified',
        'online':'urlonline',
    },
    {
        'image' :'https://m.media-amazon.com/images/I/61PnHlc0HCL.__AC_SY445_SX342_QL70_FMwebp_.jpg',
        'name' : 'Apple iPad',
        'description' : 'WHY IPAD — All the essentials in the most affordable iPad, with a beautiful 10.2-inch Retina display, powerful...',
        'tags' : [
            'tecnology', 'pad', 'tablet',
        ],
        'code':'urldecode',
        'demo':'urldedemo',
    },
    {
        'image' :'https://m.media-amazon.com/images/I/71k06Iic2NL.__AC_SX300_SY300_QL70_FMwebp_.jpg',
        'name' : 'RedThunder K84 Wireless',
        'description' : 'High-performance 2.4G Wireless Keyboard and Mouse】Are you looking for a small wireless keyboard and mouse...',
        'tags' : [
            'tecnology', 'keyboard', 'computers',
        ],
        'post':'urlpost',
        'code':'urldecode',
    },
]
    return render(request, "blog/homepage.html", {"links": links,
                                                  'projects':projects})
