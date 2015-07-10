import urllib2
import json


class GitHub(object):
    class Url:
        info = u'https://api.github.com/users/{user}'
        repos = u'https://api.github.com/users/{user}/repos'
        commit = u'https://api.github.com/repos/{user}/{repo}/commits/{sha}'
        commits = u'https://api.github.com/repos/{user}/{repo}/commits'

    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return u"<GitHub(u'{user}')>".format(user=self.user)

    @property
    def info(self):
        response = urllib2.urlopen(self.Url.info.format(user=self.user))
        return json.loads(response.read())

    @property
    def repos(self):
        response = urllib2.urlopen(self.Url.repos.format(user=self.user))
        return json.loads(response.read())

    def get_commit(self, repo, sha):
        response = urllib2.urlopen(self.Url.commit.format(user=self.user,
                                                          repo=repo, sha=sha))
        return json.loads(response.read())

    def get_commits(self, repo):
        response = urllib2.urlopen(self.Url.commits.format(user=self.user,
                                                           repo=repo))
        return json.loads(response.read())
