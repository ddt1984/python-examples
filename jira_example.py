# pip install jira
# pip install python-certifi-win32
# https://jira.readthedocs.io/examples.html#quickstart

from jira import JIRA
import collections

# 자체 Jira에서는 로그인하는 아이디, 패스워드로 로그인
#jira = JIRA('https://JIRA_HOST', auth=('ID', 'PASSWORD'))

# JAAS에서는 로그인 방법이 다름
# Profile -> Personal Access Tokens 메뉴에서 토큰 생성 가능
# https://jaas.ea.com/secure/ViewProfile.jspa?selectedTab=com.atlassian.pats.pats-plugin:jira-user-personal-access-tokens
jira = JIRA('https://JAAS_JIRA_HOST', token_auth=('TOKEN_AUTH'))

# 이슈 찾기. JQL 이용
# 1월에 업데이트된 status가 DONE인 이슈 검색
issues = jira.search_issues('project=BO and status = "DONE" and updated >= "2022/01/01" and updated <= "2022/01/31"')
print("Issues:", len(issues))

# 찾은 이슈를 유저별로 사용시간, 이슈 개수 구하기
timespentByUser = collections.defaultdict(int)
issuesByUser = collections.defaultdict(int)

for issue in issues:
    # print(issue.key)
    # print(issue.fields.issuetype.name)
    # print(issue.fields.reporter.displayName)
    # print(issue.fields.summary)
    # print(issue.fields.assignee.displayName)
    # print(issue.fields.status.name)
    assignee = issue.fields.assignee.displayName
    if issue.fields.timespent: # timespent 값 입력 된 경우만 처리
        timespentByUser[assignee] += issue.fields.timespent
    issuesByUser[assignee] += 1

for user in timespentByUser:
    print(user, timespentByUser[user] / 60 / 60)
    print(user, issuesByUser[user])
