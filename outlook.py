# https://www.codeforests.com/2020/06/05/how-to-send-email-from-outlook/

import win32com.client
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")

# 6이 Inbox임. Inbox에서 메일 제목들만 출력하기
inbox = mapi.GetDefaultFolder(6)
for message in inbox.Items:
    print(message.Subject)

# 메일 보내기
mail = outlook.CreateItem(0)
mail.To = 'SENDER@company.com'
mail.Subject = 'job family 현황 보고'
#html로 보내기도 가능. 본문에 엑셀 데이터의 주요 숫자를 가져와서 만들어서 보낼 수도 있음.
#mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = """안녕하세요
어쩌구 저쩌구
자세한건 첨부파일 참고바랍니다.

감사합니다.""";

mail.Attachments.Add('c:\\python examples/samples/data1.xlsx') #절대경로를 넣어야함
#mail.CC = 'somebody@company.com'

#mail.Send() # Send()는 바로 보내기
mail.Save() # Save()는 Draft폴더에 저장. 이후에 검토/편집 후에 보내기 가능

# 휴가 메일 보내기
mail = outlook.CreateItem(0)
mail.To = 'all@company.com'
# 오늘 날짜 구하기
from datetime import date
today = date.today()
todayString = str(today.month) + "월" + str(today.day) + "일"

mail.Subject = '[근태] ' + todayString + ' Ed Jeong 연차'
mail.Body = "업무에 참고해 주세요. 감사합니다."
mail.Save() # 테스트니 Draft로
