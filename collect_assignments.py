"""
"""

import os, io, re, base64, time
import email
from email.header import decode_header
import imaplib
import getpass

import pandas as pd
from PIL import Image


_EMAIL = "wenh06@buaa.edu.cn"
_SERVER = "mail.buaa.edu.cn"
_PORT = 993
_PATTERN = "^(?P<id>[\d]{8})-(?P<name>[\w]{2,10})-第(?P<no>[\d一二三四五六七八九十]{1,2})次作业"

_zh2num = {k:v for k,v in zip("一二三四五六七八九十", range(1,11))}
for k in "一二三四五六七八九":
    _zh2num[f"十{k}"] = 10 + _zh2num[k]

_PWD = os.path.abspath(os.path.curdir)
_STATS_FILE = os.path.join(_PWD, "统计.csv")
_COLS = ["学号", "姓名",] + [f"第{i}次作业" for i in range(1,20)]


def collect():
    """
    """
    start = time.time()
    # connect to the server and go to its inbox
    mail = imaplib.IMAP4_SSL(_SERVER, _PORT)
    mail.login(_EMAIL, getpass.getpass())

    # we choose the inbox but you can select others
    mail.select("inbox")
    # we"ll search using the ALL criteria to retrieve
    # every message inside the inbox
    # it will return with its status and a list of ids
    status, data = mail.search(None, "ALL")

    mail_ids = []
    # then we go through the list splitting its blocks
    # of bytes and appending to the mail_ids list
    for block in data:
        # the split function called without parameter
        # transforms the text or bytes into a list using
        # as separator the white spaces:
        # b"1 2 3".split() => [b"1", b"2", b"3"]
        mail_ids += block.split()
    mail_ids = mail_ids[::-1]

    if os.path.exists(_STATS_FILE):
        df_stats = pd.read_csv(_STATS_FILE)
    else:
        df_stats = pd.DataFrame(columns=_COLS)

    for i in mail_ids:
        # fetch the email message by ID
        res, msg = mail.fetch(i, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it"s a bytes, decode to str
                    try:
                        subject = subject.decode(encoding)
                    except:
                        pass
                if not isinstance(subject, str) or not re.search(_PATTERN, subject):
                    continue
                subject_content = list(re.finditer(_PATTERN, subject))[0].groupdict()
                student_id = int(subject_content["id"])
                student_name = subject_content["name"]
                assignment_no = subject_content["no"]
                assignment_no = _zh2num.get(assignment_no, assignment_no)
                
                df_assignment = df_stats[(df_stats["学号"]==student_id) & (~df_stats[f"第{assignment_no}次作业"].isna())]
                
                if not df_assignment.empty:
                    print(f"{student_name}({student_id}) 第{assignment_no}次作业 already collected.")
                    print("Continue.")
                    continue
                
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    try:
                        From = From.decode(encoding)
                    except:
                        pass
                try:
                    From_email = re.findall("\<(?P<email>[\w\d\_\-]+@[\w\d\.\_\-]+)\>", msg.get("From"))[0]
                except:
                    From_email = ""
                print("Subject:", subject)
                print("From:", From)
                print("Email address:", From_email)
                
                folder_name = os.path.join(_PWD, "attachments", f"{student_id}-{student_name}")
                save_folder_name = os.path.join(folder_name, f"第{assignment_no}次作业")
                os.makedirs(save_folder_name, exist_ok=True)
                
                if student_id not in df_stats.学号.values.tolist():
                    df_stats = df_stats.append({
                    "学号": student_id,
                    "姓名": student_name,
                    f"第{assignment_no}次作业": -1,
                }, ignore_index=True)
                else:
                    df_stats.loc[df_stats["学号"]==student_id, f"第{assignment_no}次作业"] = -1
                
                # if the email message is multipart
                if msg.is_multipart():
                    print("is multipart")
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except Exception as e:
                            pass
                        if content_type == "multipart/related":  # inline image
                            body = part.get_payload()
                            img_no = 1
                            for item in body:
                                if item.get("Content-Type").startswith("image") and item.get("Content-Transfer-Encoding") == "base64":
                                    imgdata = base64.b64decode(item.get_payload())
                                    img = Image.open(io.BytesIO(imgdata))
                                    filepath = os.path.join(save_folder_name, f"image-{img_no}.jpg")
                                    img.save(filepath)
                                    img_no += 1
                        elif content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            print(body)
                        elif "attachment" in content_disposition:
                            # download attachment
                            filename = part.get_filename()
                            if filename:
                                filepath = os.path.join(save_folder_name, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:
                    print("not multipart")
                print("="*100)
    df_stats.to_csv(_STATS_FILE, index=False)
    print(f"collection used {time.time()-start:.2f} seconds")


if __name__ == "__main__":
    collect()
