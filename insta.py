from instapy import InstaPy

session = InstaPy(username="xxxx", password="1234")
session.login()

session.set_relationship_bounds(enabled= True, max_followers= 400)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["memes", "memeindia"], amount= 3)
session.set_dont_like(["nsfw"])
session.set_comments([
                        u'nice'
                        u'Amazing'
                        u'perfect!!'],
                        media='Photo')
session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)

session.end()