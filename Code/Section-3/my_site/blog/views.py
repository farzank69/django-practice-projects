from datetime import date
from django.shortcuts import render
# Create your views here.

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Farzan',
        'comments': 3,
        'date': date(2025, 10, 5),
        'title': 'Mountain Hiking',
        'excerpt': 'There is nothing like the views you get when hiking in the mountains! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'content': """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.
        """
        
    },
    {
        'slug': 'woods-walking',
        'image': 'woods.jpg',
        'author': 'Farzan',
        'comments': 7,
        'date': date(2025, 5, 3),
        'title': 'Woods Walking',
        'excerpt': 'There is nothing like walking in the woods and reviving the soul! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'content': """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.
        """
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.jpg',
        'author': 'Farzan',
        'comments': 10,
        'date': date(2025, 9, 1),
        'title': 'Programming is fun!',
        'excerpt': 'Did you spend hours searching that one error in your code? Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'content': """
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quia tempora aut vel assumenda? Debitis officia aliquam, est quasi veritatis libero sunt iste non quisquam voluptas.
        """
    }
]

def get_date(post):
    return post['date']

def starting_post(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)      # next() function returns the first match of the generator expression
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })
