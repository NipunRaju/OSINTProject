import requests
import time
import sys

def search_username(username):
    def search():
        # Define URLs
        websites = [
            f'https://www.instagram.com/{username}',
            f'https://www.facebook.com/{username}',
            f'https://www.twitter.com/{username}',
            f'https://www.youtube.com/{username}',
            f'https://{username}.blogspot.com',
            f'https://plus.google.com/s/{username}/top',
            f'https://www.reddit.com/user/{username}',
            f'https://{username}.wordpress.com',
            f'https://www.pinterest.com/{username}',
            f'https://www.github.com/{username}',
            f'https://{username}.tumblr.com',
            f'https://www.flickr.com/people/{username}',
            f'https://steamcommunity.com/id/{username}',
            f'https://vimeo.com/{username}',
            f'https://soundcloud.com/{username}',
            f'https://disqus.com/by/{username}',
            f'https://medium.com/@{username}',
            f'https://{username}.deviantart.com',
            f'https://vk.com/{username}',
            f'https://about.me/{username}',
            f'https://imgur.com/user/{username}',
            f'https://flipboard.com/@{username}',
            f'https://slideshare.net/{username}',
            f'https://fotolog.com/{username}',
            f'https://open.spotify.com/user/{username}',
            f'https://www.mixcloud.com/{username}',
            f'https://www.scribd.com/{username}',
            f'https://www.badoo.com/en/{username}',
            f'https://www.patreon.com/{username}',
            f'https://bitbucket.org/{username}',
            f'https://www.dailymotion.com/{username}',
            f'https://www.etsy.com/shop/{username}',
            f'https://cash.me/{username}',
            f'https://www.behance.net/{username}',
            f'https://www.goodreads.com/{username}',
            f'https://www.instructables.com/member/{username}',
            f'https://keybase.io/{username}',
            f'https://kongregate.com/accounts/{username}',
            f'https://{username}.livejournal.com',
            f'https://angel.co/{username}',
            f'https://last.fm/user/{username}',
            f'https://dribbble.com/{username}',
            f'https://www.codecademy.com/{username}',
            f'https://en.gravatar.com/{username}',
            f'https://pastebin.com/u/{username}',
            f'https://foursquare.com/{username}',
            f'https://www.roblox.com/user.aspx?username={username}',
            f'https://www.gumroad.com/{username}',
            f'https://{username}.newgrounds.com',
            f'https://www.wattpad.com/user/{username}',
            f'https://www.canva.com/{username}',
            f'https://creativemarket.com/{username}',
            f'https://www.trakt.tv/users/{username}',
            f'https://500px.com/{username}',
            f'https://buzzfeed.com/{username}',
            f'https://tripadvisor.com/members/{username}',
            f'https://{username}.hubpages.com',
            f'https://{username}.contently.com',
            f'https://houzz.com/user/{username}',
            f'https://blip.fm/{username}',
            f'https://www.wikipedia.org/wiki/User:{username}',
            f'https://news.ycombinator.com/user?id={username}',
            f'https://www.reverbnation.com/{username}',
            f'https://www.designspiration.net/{username}',
            f'https://www.bandcamp.com/{username}',
            f'https://www.colourlovers.com/love/{username}',
            f'https://www.ifttt.com/p/{username}',
            f'https://www.ebay.com/usr/{username}',
            f'https://{username}.slack.com',
            f'https://www.okcupid.com/profile/{username}',
            f'https://www.trip.skyscanner.com/user/{username}',
            f'https://ello.co/{username}',
            f'https://tracky.com/user/~{username}',
            f'https://{username}.basecamphq.com/login'
        ]

        results = []
        urls = []

        results_str = ''

        results_str += f'[+] Searching for username: {username}\n'

        for url in websites:
            try:
                r = requests.get(url, timeout=10)  # Set a timeout for the request
                urls.append(url)
                result = {'url': url, 'status_code': r.status_code}
                if r.status_code == 200:
                    if username in r.text:
                        result['match'] = True
                        results_str += f'POSITIVE MATCH: Username: {username} - Text has been detected in URL: {url}\n'
                    else:
                        result['match'] = False
                        results_str += f'POSITIVE MATCH: Username: {username} - Text has NOT been detected in URL: {url}, could be a FALSE POSITIVE.\n'
                results.append(result)
            except requests.exceptions.Timeout:
                results_str += f'[-] Timeout occurred while accessing: {url}\n'
            except Exception as e:
                results_str += f'[-] An error occurred while accessing: {url} - {e}\n'

        total = len(urls)
        results_str += f'FINISHED: A total of {total} matches verified out of {total} websites.\n'

        return results_str, urls

    results_str, urls = search()
    print("Results:", results_str)
    print("URLs:", urls)
    return results_str, urls

if __name__ == "__main__":
    username = sys.argv[1]
    search_username(username)
