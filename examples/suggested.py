from rawg import Rawg


def main():
    r = Rawg()

    slug = 'grand-theft-auto-v'
    suggest = r.suggested(slug, page_size=10)

    print('Your suggestions:')
    for game in suggest.results:
        print(f'— {game.name}, released: {game.released}')


if __name__ == '__main__':
    main()
