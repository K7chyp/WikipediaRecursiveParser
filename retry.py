from re import search, compile


def is_href_valid(href) -> bool:
    for pattern in ("https", "Wikipedia", "wikimedia", "Category", "Special", "//"):
        if compile(pattern).search(href) is not None:
            return False
    return True


for href in ['/wiki/Category:Wikipedia_articles_with_GND_identifiers', '/wiki/Category:Wikipedia_articles_with_LCCN_identifiers', '/wiki/Category:Wikipedia_articles_with_MA_identifiers', '/wiki/Category:Wikipedia_articles_with_SUDOC_identifiers', '/wiki/Category:Articles_with_example_Python_(programming_language)_code', '/wiki/Category:Good_articles', '/wiki/Special:MyTalk', '/wiki/Special:MyContributions', '/wiki/Python_(programming_language)', '/wiki/Talk:Python_(programming_language)', '/wiki/Python_(programming_language)', '/wiki/Main_Page', '/wiki/Main_Page', '/wiki/Wikipedia:Contents', '/wiki/Portal:Current_events', '/wiki/Special:Random', '/wiki/Wikipedia:About', '//en.wikipedia.org/wiki/Wikipedia:Contact_us', '/wiki/Help:Contents', '/wiki/Help:Introduction', '/wiki/Wikipedia:Community_portal', '/wiki/Special:RecentChanges', '/wiki/Wikipedia:File_Upload_Wizard', '/wiki/Special:WhatLinksHere/Python_(programming_language)', '/wiki/Special:RecentChangesLinked/Python_(programming_language)', '/wiki/Wikipedia:File_Upload_Wizard', '/wiki/Special:SpecialPages', '//en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License', '//foundation.wikimedia.org/wiki/Terms_of_Use', '//foundation.wikimedia.org/wiki/Privacy_policy', '//www.wikimediafoundation.org/', '/wiki/Wikipedia:About', '/wiki/Wikipedia:General_disclaimer', '//en.wikipedia.org/wiki/Wikipedia:Contact_us', '//en.m.wikipedia.org/w/index.php?title=Python_(programming_language)&mobileaction=toggle_view_mobile']:
    print(is_href_valid(href))